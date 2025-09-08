import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

# For webcam input:
cap = cv2.VideoCapture(0) # Use 0 for webcam, or provide a video file path for a video file
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    
    # Drawing Landmarks
    landmark_cords = []
    

    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = image.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            landmark_cords.append([cx, cy])
            cv2.putText(image, str(id), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
        

###################################################        

        # Defining coordinates for the left elbow angle
        left_fist_cords = landmark_cords[mp_pose.PoseLandmark.LEFT_WRIST.value]
        left_shoulder_cords = landmark_cords[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        left_elbow_cords = landmark_cords[mp_pose.PoseLandmark.LEFT_ELBOW.value]
        
        #defining coordinates for the right elbow angle
        right_fist_cords = landmark_cords[mp_pose.PoseLandmark.RIGHT_WRIST.value]
        right_shoulder_cords = landmark_cords[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
        right_elbow_cords = landmark_cords[mp_pose.PoseLandmark.RIGHT_ELBOW.value]
        
        
        # Function to calculate angle between three points
        def calculate_angle(a, b, c):
        
            # Convert to NumPy arrays
            a = np.array(a)
            b = np.array(b)
            c = np.array(c)

            # Vectors
            ba = a - b
            bc = c - b

            # Dot product and norms
            dot_product = np.dot(ba, bc)
            norm_product = np.linalg.norm(ba) * np.linalg.norm(bc)

            # Avoid division by zero
            if norm_product == 0:
                return 0.0

            # Calculate cosine of the angle
            cos_angle = dot_product / norm_product

            # Ensure the value is in the range [-1, 1]
            cos_angle = np.clip(cos_angle, -1.0, 1.0)
            
            angle = np.degrees(np.arccos(cos_angle))
            
            if angle < 0:
                angle += 360
            # Return angle in degrees
            return angle

        left_elbow_angle = calculate_angle(left_shoulder_cords, left_elbow_cords, left_fist_cords)
        right_elbow_angle = calculate_angle(right_shoulder_cords, right_elbow_cords, right_fist_cords)
        
        # Draw lines and circles for the left elbow angle
        cv2.line(image, (left_fist_cords[0], left_fist_cords[1]), (left_shoulder_cords[0], left_shoulder_cords[1]), (255, 0, 0), 2)
        cv2.line(image, (left_elbow_cords[0], left_elbow_cords[1  ]), (left_shoulder_cords[0], left_shoulder_cords[1]), (255, 0, 0), 2)
        cv2.circle(image, (left_shoulder_cords[0], left_shoulder_cords[1]), 5, (0, 255, 0), -1)
        
        # Draw lines and circles for the right elbow angle
        cv2.line(image, (right_fist_cords[0], right_fist_cords[1]), (right_shoulder_cords[0], right_shoulder_cords[1]), (255, 0, 0), 2)
        cv2.line(image, (right_elbow_cords[0], right_elbow_cords[1  ]), (right_shoulder_cords[0], right_shoulder_cords[1]), (255, 0, 0), 2)
        cv2.circle(image, (right_shoulder_cords[0], right_shoulder_cords[1]), 5, (0, 255, 0), -1)

        # Draw angles
        flipped = cv2.flip(image, 1, image)  # Flip the image horizontally for a selfie-view display.
        cv2.putText(image, f'Left Elbow Angle: {int(left_elbow_angle)}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2) 
        cv2.putText(image, f'Right Elbow Angle: {int(right_elbow_angle)}', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

###################################################


    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', flipped)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()