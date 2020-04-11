import face_recognition
import cv2
import numpy as np
import os

def run():
    # Loading the net from gender classification
    gender_net = cv2.dnn.readNetFromCaffe('deploy_gender.prototxt', 'gender_net.caffemodel')
    MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

    # Labels of Gender
    gender_list = ['Male', 'Female']

    # Function to predict the gender
    def predictGender(image_path):
        face_img = cv2.imread(image_path)
        blob = cv2.dnn.blobFromImage(face_img, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        gender_net.setInput(blob)
        gender_preds = gender_net.forward()
        gender = gender_list[gender_preds[0].argmax()]
        return gender

    # Get a reference to webcam video
    webcam_video = cv2.VideoCapture(0)

    # Create arrays of known face encodings, their names and their genders
    known_face_encodings = []
    known_face_names = []
    known_gender = []

    # Path of folder who contains images of each person
    persons_path = "./persons"
    persons = os.listdir(persons_path)

    # Manipulates each image in the folder of persons
    for person in persons:
        image_path = persons_path + '/' + person
        filename = person[:-4]

        person_image = face_recognition.load_image_file(image_path)
        person_face_encoding = face_recognition.face_encodings(person_image)[0]
        person_name = filename 
        person_gender = predictGender(image_path)
        
        known_face_encodings.append(person_face_encoding)
        known_face_names.append(person_name)
        known_gender.append(person_gender)
        

    # Check genders
    print(known_gender)

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    gender_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = webcam_video.read()
        font = cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(frame, "Press q to quit.", (0, 30), font, 0.8, (255, 255, 255), 1)

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            gender_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                gender = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]
                #     gender = known_gender[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    gender = known_gender[best_match_index]

                face_names.append(name)
                gender_names.append(gender)
            
        process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

            # Draw a label with a name and gender below the face
            cv2.rectangle(frame, (left, bottom), (right, bottom + 56), (255, 0, 0), cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom + 24), font, 0.8, (255, 255, 255), 1)
            cv2.putText(frame, gender, (left + 6, bottom + 52), font, 0.8, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Face Recognition', frame)

        # Hit 'q' on the keyboard to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    webcam_video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()

else:
    print("running by module")