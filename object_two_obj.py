import cv2
import imutils
import time

#img = cv2.imread('person.jpg')
threshold=0.5
classNames=[]
classFile='model_data/coco.names'

with open(classFile, 'rt') as f:
    classNames=f.read().rstrip('\n').split('\n')
#print(classNames)

configPath='model_data/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath='model_data/frozen_inference_graph.pb'

net=cv2.dnn_DetectionModel(weightPath,configPath)

net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap1 = cv2.VideoCapture(1)
cap1.set(3,640)
cap1.set(4,480)


def show_img0(img):
    classIds, confs, bbox = net.detect(img,confThreshold=threshold)
    #print(classIds,bbox)
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0,255,0), thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2) 
            print(classNames[classId-1])
            cv2.putText(img,str(confidence),(box[0]+10,box[1]+70), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2) 
            print(classNames[classId-1])

def show_img1(img):
    classIds, confs, bbox = net.detect(img,confThreshold=threshold)
    #print(classIds,bbox)
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0,255,0), thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2) 
            print(classNames[classId-1])
            cv2.putText(img,str(confidence),(box[0]+10,box[1]+70), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2) 
            print(classNames[classId-1])
            
while True:
    #success, img =cap.read()
    ret0, img = cap.read()
    assert ret0 # succeeds
    # success, img1 =cap1.read()
    ret1, img1 = cap1.read()
    assert ret1 # fails?!
    
    show_img0(img)
    show_img1(img1)
    cv2.imshow("output 1",img)
    cv2.imshow("output 2",img1)
    cv2.waitKey(1)
    
    
   
    
    

