from .AI_model import YOLOV8, YOLOV7


class Factory_Model():
    # _instances = {}

    # def __new__(cls):
    #     if cls not in cls._instances:
    #         cls._instances[cls] = super().__new__(cls)
    #         cls._instances[cls].initialize()
        
    #     return cls._instances[cls]

    # def initialize(self):
    #     # Initialize your models here
    #     self.Model_YOLOV8 = None
    #     self.Model_YOLOV7 = None



    def get_model(self,model_name):
        
        if (model_name == "YOLOV8"):
            return YOLOV8()    

        elif(model_name == "YOLOV7"):
            pass


Factory = Factory_Model()