import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import os
from draw import draw_landmarks_on_image  #to draw on image input given to verify
from get_anglesList import get_angle #to get angles from co-ordinates

model_path = 'hand_landmarker.task'

#model settings
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path), running_mode = VisionRunningMode.IMAGE)

#loading image
# img = cv2.imread('cheers.jpg')
# image = mp.Image.create_from_file('cheers.jpg')


#to run model and get results into it
#function to return co-ordinates of landmarks
def runModel(img_path):
    image = mp.Image.create_from_file(img_path)
    with HandLandmarker.create_from_options(options) as landmarker:
        detection_result = landmarker.detect(image)
    result = detection_result.hand_landmarks[0]
    nLandMarks = len(result)
    op = []
    for i in range(nLandMarks):
        mark = result[i]
        op.append((mark.x, mark.y, mark.z))
    return op, detection_result

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
    with open('co-ordinates.txt', 'w') as f:
        for i in range(1, 9):
            img_path = 'images/' + str(i) + '.jpg'
            op, detection_result = runModel(img_path)
            f.write(str(op) + '\n')
            drawLandMarks(i,img_path, detection_result)

iterateImages()
#saving co-ords into txt file
