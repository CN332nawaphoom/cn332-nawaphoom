from .AI_model import YOLOV8, YOLOV7
import threading

class Factory_Model:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Factory_Model, cls).__new__(cls)
                cls._instance.initialize()
        return cls._instance

    def initialize(self):
        if not hasattr(self, '_initialized'):
            # Initialize your models to None
            self.Model_YOLOV8 = None
            self.Model_YOLOV7 = None
            self._initialized = True

    def get_model(self, model_name):
        if model_name == "YOLOV8":
            if self.Model_YOLOV8 is None:
                self.Model_YOLOV8 = YOLOV8()
            # return self.Model_YOLOV8
            return YOLOV8()
        elif model_name == "YOLOV7":
            pass
        else:
            raise ValueError(f"Unknown model name: {model_name}")

# Singleton instance of the Factory_Model
Factory = Factory_Model()

# # Usage example
# model_v8 = Factory.get_model("YOLOV8")
# model_v7 = Factory.get_model("YOLOV7")
