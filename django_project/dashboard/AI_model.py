from ultralytics import YOLO
from ultralytics.solutions import object_counter
import numpy as np
import cv2
from .sort import Sort
import torch

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

    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YOLO("weights/yolov8n.pt").to(self.device)
    

    def train(self, path_input):
        return 
    
    
    def detect(self, path_input:str,coordinate):
        filename = "media/detection/"+ path_input.split("\\")[-1]
        print(f"output_path:{filename}")
        print(f"device:{self.device}")


        cap = cv2.VideoCapture(path_input)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(filename, fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(3)), int(cap.get(4))))

        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(frame_width)
        print(frame_height)
        
        #region_rect = [[(0, 800), (600, 700), (600, 900), (0, 900)],[(1000, 800), (1600, 700), (1600, 900), (1000, 900)]]
        region_rect = coordinate

        # Init Object Counter
        counters = [object_counter.ObjectCounter() for _ in range(len(region_rect))]
        print(counters)
        for c in range(len(counters)):
            counters[c].set_args(view_img=True,
                         view_in_counts =False,      
                         view_out_counts =False,
                         reg_pts=region_rect[c],
                         classes_names=self.model.names,
                         draw_tracks=True,
                         line_thickness=2)
        
        while cap.isOpened():
            ret, frame = cap.read()
        
            if not ret:
                break
        
            # Perform detection
            results = self.model.track(frame,  persist=True, conf=0.5,verbose=False)
            # for r in region_rect:
            #     pts = np.array(r, np.int32).reshape((-1, 1, 2))
            #     cv2.polylines(frame, [pts], isClosed=True, color=(255, 0, 255), thickness=5)
            # track = frame.copy()
            for counter in counters:
                counter.start_counting(frame, results)
            
            out.write(frame)       
           

        cap.release()
        out.release()

        # #print(counter.track_history)
        # print(len(counter.counting_dict))
        for counter in counters:
            print(counter.counting_dict)
            print(counter.in_counts)
        return [1,2,3]
        

    
    

class YOLOV7(Model_AI):
    
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YOLO().to(self.device)

    def train(self, path_input):
        return
    
    def detect(self, path_input):
        return 

    
            








# for result in results:
            #     boxes = result.boxes
            #     for box in boxes:
            #         x1, y1, x2, y2 = map(int, box.xyxy[0])
            #         conf = box.conf[0]
            #         cls = int(box.cls[0])

            # for tracked_object  in trackers:
            #     x1, y1, x2, y2,obj_id = map(int, tracked_object )
                
            #     # Draw bounding box
            #     label = f'{"car"} {conf:.2f}'
            #     cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            #     cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    
            #     for l in range(len(line)):
            #         if check_intersection((x1, y1), (x2, y2), line[l]):
            #             object_count[l] += 1
            
            #for l in line:
            #cv2.line(frame, l[0], l[1], (0, 0, 255), 2)

            # Write frame with bounding boxes to output video
            #out.write(frame)