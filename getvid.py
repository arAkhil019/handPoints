import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import os
import numpy as np
from draw import draw_landmarks_on_image  # To draw on image input given to verify
from get_anglesList import get_anglesList # To get angles from coordinates

model_path = 'hand_landmarker.task'

# Model settings
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path), 
    running_mode=VisionRunningMode.IMAGE, 
    num_hands=2
)

def get_cords(landmarks):
    cords = []
    for mark in landmarks:
        cords.append((mark.x, mark.y, mark.z))
    return cords

def extract_hand_landmarks(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
    with HandLandmarker.create_from_options(options) as landmarker:
        detection_result = landmarker.detect(mp_image)
    
    result = detection_result.hand_landmarks
    hand_landmarks = []

    nLandMarks = len(result)
    if nLandMarks == 0:
        print("No Landmarks Detected")
        return
    elif nLandMarks == 1:
        print("One Hand Detected")
        hand = detection_result.handedness[0]
        cords = get_cords(result[0])
        x0y0 = [int(cords[0][0] * 100), int(cords[0][1] * 100)]
        if hand[0].display_name == 'Right':
            full_result = [0] * 23
            full_result = full_result + get_anglesList(cords) + x0y0
        else:
            full_result = get_anglesList(cords) + x0y0 + [0] * 23
    else:
        print("Two Hands Detected")
        cords1, cords2 = get_cords(result[0]), get_cords(result[1])
        x0y0 = [int(cords1[0][0] * 100), int(cords1[0][1] * 100)]
        x1y1 = [int(cords2[0][0] * 100), int(cords2[0][1] * 100)]
        full_result = get_anglesList(cords1) + x0y0 + get_anglesList(cords2) + x1y1
    
    return full_result

# Load video
video_path = 'MVI_0008.MOV'
cap = cv2.VideoCapture(video_path)

# Get total number of frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
interval = total_frames // 10

hand_landmarks_list = []

for i in range(0, total_frames, interval):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()
    
    if not ret:
        break

    hand_landmarks = extract_hand_landmarks(frame)
    hand_landmarks_list.append(hand_landmarks)
    print(hand_landmarks)

# Release video capture
cap.release()
# Convert to numpy array for further processing

