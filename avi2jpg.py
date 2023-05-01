import cv2
import math

cap = cv2.VideoCapture(r'F:\数据集\计设数据集\最终数据集视频\2023_4_19_数据集.avi')
frameRate = cap.get(5)  # frame rate
if not cap.isOpened():
    print('error')
    exit(-1)
while (cap.isOpened()):
    frameId = cap.get(1)  # current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if frameId % math.floor(frameRate) == 0:
        filename = 'img/image_4_' + str(int(frameId)) + ".png"
        try:
            cv2.imwrite(filename, frame)
        except:
            print('error occur, maybe img folder not exist')
cap.release()
print ("Done!")