# Import necessary libraries
from scipy.spatial import distance as dist  # For calculating Euclidean distance (EAR computation)
from imutils import face_utils  # Helper functions for facial landmarks
import imutils  # Image processing library
import dlib  # Facial landmark detection
import cv2  # OpenCV for real-time video processing
import winsound  # Windows-only: Beep sound alert for drowsiness detection

# Sound Alert Configuration
frequency = 2500  # Frequency of the beep sound (Hz)
duration = 1000  # Duration of the beep sound (milliseconds)

# Function to calculate Eye Aspect Ratio (EAR) based on eye landmarks
def eyeAspectRatio(eye):
    A = dist.euclidean(eye[1], eye[5])  # Vertical distance between eye landmarks
    B = dist.euclidean(eye[2], eye[4])  # Vertical distance between eye landmarks
    C = dist.euclidean(eye[0], eye[3])  # Horizontal distance between eye landmarks
    ear = (A + B) / (2.0 * C)  # EAR formula
    return ear

# Initialize parameters
count = 0  # Frame counter for eye closure duration
earThresh = 0.3  # EAR threshold for drowsiness detection
earFrames = 48  # Number of consecutive frames required to trigger an alert

# Load the facial landmark predictor model
shapePredictor = "code/shape_predictor_68_face_landmarks.dat"  # Path to the model file

# Initialize the webcam
cam = cv2.VideoCapture(0)  # 0 refers to the default camera

# Check if the camera is opened successfully
if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

# Load the face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()  # Face detection model
predictor = dlib.shape_predictor(shapePredictor)  # Facial landmark model

# Get the indices for left and right eyes from the 68 facial landmarks
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# Start real-time video processing
while True:
    _, frame = cam.read()  # Read frame from the webcam
    frame = imutils.resize(frame, width=450)  # Resize frame for better processing speed
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale

    rects = detector(gray, 0)  # Detect faces in the frame

    for rect in rects:  # Loop over detected faces
        shape = predictor(gray, rect)  # Get facial landmarks
        shape = face_utils.shape_to_np(shape)  # Convert to NumPy array

        # Extract left and right eye coordinates
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        # Calculate EAR for both eyes
        leftEAR = eyeAspectRatio(leftEye)
        rightEAR = eyeAspectRatio(rightEye)

        # Compute the average EAR for both eyes
        ear = (leftEAR + rightEAR) / 2.0

        # Draw the eye landmarks on the frame
        leftEyeHull = cv2.convexHull(leftEye)  # Convex hull for left eye
        rightEyeHull = cv2.convexHull(rightEye)  # Convex hull for right eye
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 0, 255), 1)  # Draw red contour
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 0, 255), 1)  # Draw red contour

        # Check if EAR is below the threshold
        if ear < earThresh:
            count += 1  # Increase drowsiness frame count

            # If eyes are closed for too many frames, trigger an alarm
            if count >= earFrames:
                cv2.putText(frame, "DROWSINESS DETECTED", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                winsound.Beep(frequency, duration)  # Play alarm sound
        else:
            count = 0  # Reset counter if eyes are open

    # Display the processed video frame
    cv2.imshow("Frame", frame)

    # Press 'q' to exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release the webcam and close OpenCV windows
cam.release()
cv2.destroyAllWindows()
