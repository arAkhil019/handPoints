import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import os
from draw import draw_landmarks_on_image  #to draw on image input given to verify
from get_anglesList import get_anglesList #to get angles from co-ordinates
# from plot_cords import plotangles, plotxy, plot_z #to plot co-ordinates

model_path = 'hand_landmarker.task'

#model settings
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path), running_mode = VisionRunningMode.IMAGE, num_hands = 2)

#loading image
# img = cv2.imread('cheers.jpg')
# image = mp.Image.create_from_file('cheers.jpg')

#to extract co-ordinates from list of normalised landmarks
def get_cords(landmarks):
    cords = []
    for mark in landmarks:
        cords.append((mark.x, mark.y, mark.z))
    return cords

#to get values that are required for the model output
def getValues(landmarks):
    values =[]
    
#to run model and get results into it
#function to return co-ordinates of landmarks
def runModel(img_path):
    image = mp.Image.create_from_file(img_path)
    with HandLandmarker.create_from_options(options) as landmarker:
        detection_result = landmarker.detect(image)
    # print(detection_result)
    result = detection_result.hand_landmarks
    # print(result)
    nLandMarks = len(result)
    if nLandMarks == 0:
        print("No Landmarks Detected")
        return
    elif nLandMarks == 1:
        print("One Hand Detected")
        hand = detection_result.handedness[0]
        cords = get_cords(result[0])
        x0y0 = [int(cords[0][0]*100), int(cords[0][1]*100)]
        if hand[0].display_name == 'Right':
            full_result = [0]*23
            full_result = full_result + get_anglesList(cords) + x0y0
        else:
            full_result = get_anglesList(cords) + x0y0 + [0]*23
        # print(full_result,len(full_result))
    else:
        print("Two Hands Detected")
        cords1, cords2 = get_cords(result[0]), get_cords(result[1])
        x0y0, x1y1 = [int(cords1[0][0]*100), int(cords1[0][1]*100)], [int(cords2[0][0]*100), int(cords2[0][1]*100)]
        full_result = get_anglesList(cords1) + x0y0 + get_anglesList(cords2) + x1y1
        # print(full_result,len(full_result))
    op = []
    # for i in range(len(result)):
    #     mark = result[i]
    #     op.append((mark.x, mark.y, mark.z))
    # plotxy(op)
    return full_result, detection_result

#to draw landmarks on image
def drawLandMarks(name,img_path, detection_result):
    pwd = os.getcwd()
    image = mp.Image.create_from_file(img_path)
    annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)
    annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(str(pwd)+'/output/Output' + str(name) + ".jpg", annotated_image)
    #uncomment below to view output and to close a window press 'q'
    while True:
        cv2.imshow("Output Mapping:",annotated_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#to iterate images in model and gather co-ordinates
def iterateImages():
    with open('final_set.txt', 'a') as f:
        for i in range(1, 26):
            img_path = 'images/' + str(i) + '.jpg'
            op, detection_result = runModel(img_path)
            f.write(str(op) + '\n')
            drawLandMarks(i,img_path, detection_result)

iterateImages()
#saving co-ords into txt file
