from tflite_runtime.interpreter import Interpreter
import os
import time
import cv2
import numpy as np 

class detector2:

    def __init__(self, modelpath, labelpath):

        self.modelpath = os.path.join(os.getcwd(), modelpath)
        self.labelpath = os.path.join(os.getcwd(), labelpath)

        print('Loading model...')
        start_time = time.time()

        #load model
        self.interpreter = Interpreter(model_path=self.modelpath)
        self.interpreter.allocate_tensors()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Done! Took {} seconds'.format(elapsed_time))

        # Get model details
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.height = self.input_details[0]['shape'][1]
        self.width = self.input_details[0]['shape'][2]

        self.floating_model = (self.input_details[0]['dtype'] == np.float32)

        self.input_mean = 127.5
        self.input_std = 127.5

        # Check output layer name to determine if this model was created with TF2 or TF1,
        # because outputs are ordered differently for TF2 and TF1 models
        self.outname = self.output_details[0]['name']

        if ('StatefulPartitionedCall' in self.outname): # This is a TF2 model
            self.boxes_idx, self.classes_idx, self.scores_idx = 1, 3, 0
        else: # This is a TF1 model
            self.boxes_idx, self.classes_idx, self.scores_idx = 0, 1, 2


        with open(labelpath, 'r') as f:
            self.labels = [line.strip() for line in f.readlines()]
        

        def run(image):
            pass

