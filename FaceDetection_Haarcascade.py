import cv2
import os

# Loading the Haar Cascade model for face recognition
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# The path of the input and output images folder
input_folder = './input_images'
output_folder = './output_images'
# Create the output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"): 
        # Read image from file
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # preprocessing
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Recognition of faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9, minSize=(30, 30))

        # Draw a rectangle on the identified faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Save the image with the specified faces in the output folder
        output_path = os.path.join(output_folder, "detected_" + filename)
        cv2.imwrite(output_path, image)
        print(f"The processed image is saved: {output_path}")

print("All images were processed.")