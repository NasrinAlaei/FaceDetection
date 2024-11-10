## Face Detection using Haar Cascade
This repository contains a Python script that performs face detection on images using the Haar Cascade Classifier from OpenCV. The model used is the pre-trained Haar Cascade Classifier for frontal face detection which is included in the OpenCV library. The script processes all the images in a specified input folder, detects faces in each image, and saves the processed images with rectangles drawn around the detected faces in an output folder.

### Requirements
To run the code, you need to have the following installed:

Python 3.x
OpenCV (cv2 module)
You can install OpenCV using pip if it is not already installed:

"pip install opencv-python"

### Workflow:
1. Load Haar Cascade Model: 
The script uses a pre-trained Haar Cascade model (haarcascade_frontalface_default.xml) for detecting frontal faces in images. This model is provided by OpenCV and trained to detect faces in a wide range of image data.

2. Input Folder: 
All images that need to be processed should be placed in the ./input_images folder. The script will process all .jpg and .png images in this directory.

3. Face Detection:
Each image is converted to grayscale, which improves the efficiency and accuracy of the face detection.
The detectMultiScale function is used to detect faces in the image. It returns a list of rectangles that correspond to detected faces.

4. Output Folder:
The processed images, where faces are highlighted with red rectangles, are saved in the ./output_images1 folder.
The output images are saved with the prefix detected_ in their filename to indicate that the face detection has been applied.

5. Parameters:
scaleFactor=1.1: This compensates for faces appearing larger or smaller depending on their distance from the camera.
minNeighbors=9: This defines how many neighbors each rectangle should have to retain it.
minSize=(30, 30): Minimum size of faces to be detected.


### Haar Cascade Classifier:
The Haar Cascade Classifier is a machine learning-based approach to object detection. The classifier used in this script is pre-trained on a large dataset of images containing frontal faces, and works by analyzing patterns of pixel intensities that correspond to face-like structures.

### How it Works:
The algorithm works by detecting specific features of faces such as eyes, nose, and mouth, and combines these features to recognize the face as a whole.
The detectMultiScale method scans the image at multiple scales, checking for face-like patterns at various sizes.

### Usage
Place your images in the ./input_images directory.
Run the script.
After the script finishes, check the ./output_images folder for the images with detected faces.

"python FaceDetection_Haarcascade.py"

### Output
After running the script, the processed images will be saved in the output_images folder. Each processed image will have a red rectangle drawn around the detected face(s).


You can easily modify the parameters or improve the script for your specific use case. This algorithm does not perform well under more complex conditions or at different angles (both in images and in real-time). Therefore, you may consider using more advanced models or techniques, such as deep learning-based methods, to improve performance.


I also have a face detection model based on a DNN (Deep Neural Network) on my page, which detects faces in real-time with acceptable speed and accuracy at different angles.#   F a c e D e t e c t i o n  
 #   F a c e D e t e c t i o n  
 #   F a c e D e t e c t i o n  
 #   F a c e D e t e c t i o n  
 #   F a c e D e t e c t i o n  
 #   F a c e D e t e c t i o n  
 