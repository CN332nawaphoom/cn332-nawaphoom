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
        fourcc = cv2.VideoWriter_fourcc(*'avc1')
        out = cv2.VideoWriter(filename, fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(3)), int(cap.get(4))))

        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(frame_width)
        print(frame_height)
        
        #region_rect = [[(0, 800), (600, 700), (600, 900), (0, 900)],[(1000, 800), (1600, 700), (1600, 900), (1000, 900)]]
        region_rect = coordinate
        for l in region_rect:
            for idx in range(len(l)):
                l[idx] = ( (l[idx][0]*frame_width)//960,(l[idx][1]*frame_height)//540)

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
            i = 1
            for r in region_rect:
                pts = np.array(r, np.int32).reshape((-1, 1, 2))
                centroid_x = sum(pt[0] for pt in r) // len(r)
                centroid_y = sum(pt[1] for pt in r) // len(r)
                cv2.putText(frame, f'road{i}', (centroid_x, centroid_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
                i+=1
            # track = frame.copy()
            for counter in counters:
                counter.start_counting(frame, results)
            
            out.write(frame)       
           

        cap.release()
        out.release()

        data = {}
        i = 1
        for counter in counters:
            data[f"roadlane{i}"] = counter.in_counts
            i+=1
        data["all_detected"] = len(counters[0].counting_dict)  # get all object was deteced

        return data
        

    
    

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