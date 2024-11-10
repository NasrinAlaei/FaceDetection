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
Face detection using the Haar Cascade algorithm is a traditional computer vision technique that detects faces by identifying specific features, such as edges and textures, within an image. The method is based on Haar-like features and uses a cascade classifier, which is a combination of many small classifiers (or stages) applied in a sequence to detect objects like faces.

#### How Haar Cascade Works
1. Haar-Like Features: Haar-like features are patterns of adjacent rectangular regions in an image. The algorithm calculates the difference in pixel intensities between these regions to identify features, such as eyes, nose, and mouth.

2. Cascade of Classifiers: Haar Cascade uses a series of classifiers, each focusing on different levels of detail. The process begins by scanning small regions of the image and progresses through multiple layers. If a region passes all stages, it is classified as containing a face; otherwise, the region is discarded.

3. Training with Positive and Negative Images: The model is trained using a large dataset of images containing faces (positive samples) and images without faces (negative samples). The cascade is trained to detect face-like features and to ignore non-face patterns.

#### Pros and Cons of Haar Cascade
Pros:
. Fast and Lightweight: Haar Cascade is computationally efficient, which makes it suitable for real-time face detection.
. Simple to Use: Haar Cascade models are easy to integrate and use with OpenCV.

Cons:
. Lower Accuracy: It is less accurate than modern deep learning models, especially under varying lighting and complex backgrounds.
. Sensitivity to Angles and Scale: Haar Cascade may struggle with detecting faces that are rotated or occluded.

### Usage
Place your images in the ./input_images directory.
Run the script.
After the script finishes, check the ./output_images folder for the images with detected faces.
"python FaceDetection_Haarcascade.py"

### Output
After running the script, the processed images will be saved in the output_images folder. Each processed image will have a red rectangle drawn around the detected face(s).


You can easily modify the parameters or improve the script for your specific use case. This algorithm does not perform well under more complex conditions or at different angles (both in images and in real-time). Therefore, you may consider using more advanced models or techniques, such as deep learning-based methods, to improve performance.


I also have a [face detection model based on a DNN (Deep Neural Network)](https://github.com/NasrinAlaei/FaceDetection_DNN) on my page, which detects faces in real-time with acceptable speed and accuracy at different angles.
