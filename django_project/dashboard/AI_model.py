from ultralytics import YOLO
import numpy as np
import cv2
from .sort import Sort


class Model_AI:
    def train(self,path_input):
        pass


    def detect(self,path_input):
        pass


def check_intersection(pt1, pt2, line):
        """Check if a line segment intersects with another line."""
        x1, y1 = pt1
        x2, y2 = pt2
        x3, y3 = line[0]
        x4, y4 = line[1]

        # Calculate the determinant
        det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        # If the determinant is 0, the lines are parallel
        if det == 0:
            return False

        # Calculate the intersection point
        intersect_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
        intersect_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det

        # Check if the intersection point is within the line segments
        if min(x1, x2) <= intersect_x <= max(x1, x2) and min(x3, x4) <= intersect_x <= max(x3, x4) and \
           min(y1, y2) <= intersect_y <= max(y1, y2) and min(y3, y4) <= intersect_y <= max(y3, y4):
            return True

        return False


class YOLOV8(Model_AI):
    
    model = YOLO("weights/yolov8n.pt")
    

    def train(self, path_input):
        return 
    
    
    def detect(self, path_input):
        tracker = Sort() 

        cap = cv2.VideoCapture(path_input)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('detection/video_with_boxes.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
        line = [((300, 500), (700, 500))] #((x1,y1),(x2,y2))
        object_count = [0]*len(line)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Perform detection
            results = self.model(frame, stream=True)
            detections = []
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    conf = box.conf[0]
                    cls = int(box.cls[0])
                    detections.append([x1, y1, x2, y2, conf,cls])
                    
            trackers = tracker.update(np.array(detections))

            for tracked_object  in trackers:
                x1, y1, x2, y2,obj_id = map(int, tracked_object )
                
                # Draw bounding box
                label = f'{"car"} {conf:.2f}'
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    
                for l in range(len(line)):
                    if check_intersection((x1, y1), (x2, y2), line[l]):
                        object_count[l] += 1
            
            for l in line:
                cv2.line(frame, l[0], l[1], (0, 0, 255), 2)

            # Write frame with bounding boxes to output video
            out.write(frame)

        cap.release()
        out.release()

        print(object_count)

    
    

class YOLOV7(Model_AI):
    
    model = YOLO("weights/yolov8n.pt")

    def train(self, path_input):
        return 
    
    def detect(self, path_input):
        
        return self.model (path_input, stream=True)