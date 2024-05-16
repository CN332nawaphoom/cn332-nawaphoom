from .AI_model import YOLOV8, YOLOV7


class Factory_Model():
    _instances = {}

    def __new__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
            cls._instances[cls].initialize()
        return cls._instances[cls]

    def initialize(self):
        # initial
        self.Model_YOLOV8 = None
        self.Model_YOLOV7 = None
        


    def get_model(self,model_name):
        # singleton
        if (model_name == "YOLOV8"):
            print(self.Model_YOLOV8 == None)
            if self.Model_YOLOV8 == None:
                self.Model_YOLOV8 = YOLOV8()
                return self.Model_YOLOV8
            else:   
                return self.Model_YOLOV8      

        elif(model_name == "YOLOV7"):
            print(self.Model_YOLOV7 == None)
            if self.Model_YOLOV7 == None:
                self.Model_YOLOV7 = YOLOV7()
            else:   
                return self.Model_YOLOV7


Factory = Factory_Model()