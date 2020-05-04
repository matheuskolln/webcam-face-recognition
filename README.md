<h1 align="center">Webcam Face and Gender Recognition</h1>
<div align="center"><img src="./images/header.jpg" alt="header"></div>
<p>This Python script aims to recognize people and their genders. It works with OpenCV and Face Recognition API. By facial recognition, a person is predicted and sex is estimated using Deep Neural Network from OpenCV. The script must analyze an image within a specific folder (with one or n people) and will return 128-dimension face encoding for each face in the image. Then, predict sex using the neural network.</b></p>
<h2>Requirements</h2>
<ul>
    <h3>I run the code in this config:</h3>
    <ul>
        <li>Python 3.6.10</li>
        <li>OpenCV 4.2.0</li>
        <li>Face Recognition 1.2.3</li>
        <li>Dlib 19.8.1</li>
        <li>Numpy 1.18.1</li>
    </ul>
    <h3>You can get it here:</h3>
    <li>
        <a href="https://www.python.org/downloads/">Python 3.6</a>
    </li><br>
    <li>
        <a href="https://docs.opencv.org/master/d6/d00/tutorial_py_root.html">OpenCV</a>
        <pre><code>pip install opencv-python</code></pre>
    </li>
    <li>
        <a href="https://github.com/ageitgey/face_recognition">Face Recognition</a>
        <pre><code>pip install face_recognition</code></pre>
    </li>
    <li>
        <a href="http://dlib.net/">Dlib</a>
        <pre><code>pip install dlib</code></pre>
        <p>If you are in Windows and the first method does not do, try this:</p>
        <pre><code>python -m pip install https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf</code></pre>
    </li>
    <li>
        <a href="https://numpy.org/doc/">NumPy</a>
        <pre><code>pip install numpy</code></pre>
    </li>
    <li>
        <a href="https://matplotlib.org/3.2.1/contents.html">Matplotlib(optional)</a>
    <pre><code>pip install matplotlib</code></pre>
    </li>
</ul>
<h2>How to run?</h2>
<img src="./images/menu.jpg" alt="menu">
<p>First of all, you need to run in terminal
    <pre><code>python menu.py</code></pre>
    After that you can press the button "Put Images", which will open a window to select the people’s images, then you can press the button "Find Faces" and the program will start. 
    The name of the person’s image must be with their name, otherwise, the program will recognize the person with the image name. </p>
<p>  This will open a window called Face Recognition, which will recognize and distinguish people according to the photos in the people folder. If you want to close the window just press <b>"q"</b>.</p>
<h2>Examples:</h2>
<h3>One person recognitions</h3>
<img src="./images//one_person.jpg" alt="one-person">

<h3>Two persons recognitions</h3>
<img src="./images//two_persons.jpg" alt="two-persons">

<h2>Questions or Issues</h2>
<p>If you have any question or are getting any issue, contact-me.</p>
<a href="mailto:matheuzhenrik@gmail.com">E-mail</a><br>
<a href="www.linkedin.com/in/matheuskolln">LinkedIn</a>