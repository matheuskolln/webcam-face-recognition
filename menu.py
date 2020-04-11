from tkinter import *
from tkinter import filedialog
import os
import shutil
import webcamfacerecogntion

def open_files():
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A Image", filetype =
    (("jpeg files","*.jpg"),("png files","*.png*")) )
    shutil.move(filename, "./persons/" + os.path.split(filename)[1])

window = Tk()

window.title("Face Recognition")
window.geometry("400x600+760+200")

images_button = Button(window, text="PUT IMAGES", command=lambda: open_files())
images_button.pack()

run_button = Button(window, text="RUN", command=lambda: webcamfacerecogntion.run())
run_button.pack()

quit_button = Button(window, text="QUIT", command=lambda: window.destroy())
quit_button.pack()
window.mainloop()