import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("mask_detection_model.h5")  # Load trained model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

labels = ["No Mask", "Mask"]
cap = cv2.VideoCapture(0)  # Open webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        face = cv2.resize(face, (128, 128))  # Resize to match model input size
        face = face / 255.0  # Normalize
        face = np.expand_dims(face, axis=0)

        prediction = model.predict(face)[0][0]  
        print("Model Prediction:", prediction)  # Debugging

        label = labels[int(prediction > 0.5)]
        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Mask Detection", frame)  # Show output in OpenCV window

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit when 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()
