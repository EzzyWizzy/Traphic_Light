import cv2
from traffic_light import *
#img = cv2.imread('person.jpg')
threshold=0.6
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

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
off_all(0, 0, 0)
traffic_state(0, 1, 0)
count =0;
while True:
    success, img =cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=threshold)
    #print(classIds,bbox)
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0,255,0), thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2) 
            print(classNames[classId-1])
            cv2.putText(img,str(confidence),(box[0]+10,box[1]+70), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2) 
            print(classNames[classId-1])
            count =count+ 1
            print(count)
            
            print('EAST WEST ROAD')
            traffic_state(0, 1, 0)
            traffic_state4(0, 1, 0)
            traffic_state2(1, 0, 0)
            traffic_state3(1, 0, 0)
            if count==5:
                off_all(0, 0, 0)
                traffic_state(0, 0, 1)
                traffic_state4(0, 0, 1)
                traffic_state2(1, 0, 0)
                traffic_state3(1, 0, 0)
            if count==15:
                print('SOUTH NORTH ROAD')
                off_all(0, 0, 0)
                traffic_state(1, 0, 0)
                traffic_state4(1, 0, 0)
                traffic_state2(0, 1, 0)
                traffic_state3(0, 1, 0)
            if count==20:
                traffic_state(1, 0, 0)
                traffic_state4(1, 0, 0)
                traffic_state2(0, 0, 1)
                traffic_state3(0, 0, 1)
            if count==25:
                count=0
                off_all(0, 0, 0)
            if classNames[classId-1] == 'car':
                off_all(0, 0, 0)
                traffic_state(0, 1, 0)
                traffic_state4(0, 1, 0)
                traffic_state2(1, 0, 0)
                traffic_state3(1, 0, 0) 
            else:
                off_all(0, 0, 0)
                traffic_state(1, 0, 0)
                traffic_state4(1, 0, 0)
                traffic_state2(0, 1, 0)
                traffic_state3(0, 1, 0)
                           
    cv2.imshow("output",img)
    cv2.waitKey(1)

