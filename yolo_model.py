import numpy as np
import argparse
import imutils
import time
import cv2
import os

yolo ="D:\\College Stuff\\4th Year Project\\research\\yolo-object-detection\\yolo-coco\\"
confi = 0.5
threshold = 0.3
count =0
def call_yolo():
    global yolo 
    # derive the paths to the YOLO weights and model configuration
    weightsPath = os.path.join(yolo, "yolov3.weights")
    configPath = os.path.join(yolo, "yolov3.cfg")

    # load our YOLO object detector trained on COCO dataset (80 classes)
    # and determine only the *output* layer names that we need from YOLO
    print("[INFO] loading YOLO from disk...")
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
    return net 

def colors():
    # load the COCO class labels our YOLO model was trained on
    global yolo 
    labelsPath = os.path.join(yolo, "coco.names")
    LABELS = open(labelsPath).read().strip().split("\n")

    # initialize a list of colors to represent each possible class label
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
        dtype="uint8")
    return COLORS


def get_video_streams():
    i=0
    ip="D:\\College Stuff\\4th Year Project\\research\\yolo-object-detection\\videos\\"
    vs=[]
    while i<4 :
        vs.append(cv2.VideoCapture(os.path.join(ip, str(i+1)+".mp4")))
        i=i+1
    return vs

def get_vehicles(frame , net):
    global confi
    global threshold
    global yolo
    global count
    count=0 
    labelsPath = os.path.join(yolo, "coco.names")
    LABELS = open(labelsPath).read().strip().split("\n")
    
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
            swapRB=True, crop=False)

    (H, W) = frame.shape[:2]
    net.setInput(blob)
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    layerOutputs = net.forward(ln)
    boxes = []
    confidences = []
    classIDs = []
    for output in layerOutputs:
        # loop over each of the detections
        for detection in output:
            # extract the class ID and confidence (i.e., probability)
            # of the current object detection
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            # filter out weak predictions by ensuring the detected
            # probability is greater than the minimum probability
            if confidence > confi:
                # scale the bounding box coordinates back relative to
                # the size of the image, keeping in mind that YOLO
                # actually returns the center (x, y)-coordinates of
                # the bounding box followed by the boxes' width and
                # height
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                # use the center (x, y)-coordinates to derive the top
                # and and left corner of the bounding box
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                

                # update our list of bounding box coordinates,
                # confidences, and class IDs
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # apply non-maxima suppression to suppress weak, overlapping
    # bounding boxes
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confi,threshold)
    cv2.destroyWindow("Frame")
    if len(idxs) > 0:
        # loop over the indexes we are keeping
        for i in idxs.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            COLORS=colors()
            color = [int(c) for c in COLORS[classIDs[i]]]
            if(x>W/2):
                if LABELS[classIDs[i]]== "car" or LABELS[classIDs[i]]== "bicycle" or LABELS[classIDs[i]]== "motorbike" or LABELS[classIDs[i]]== "bus" or LABELS[classIDs[i]]== "truck" :
                    count+=1
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    text = "{}: {:.4f}".format(LABELS[classIDs[i]],
                        confidences[i])
                    cv2.putText(frame, text, (x, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.putText(frame, "Vehicle Count = " +str(count) , ( 20,20) , cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0) , 2)
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
    return count



