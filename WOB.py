import cv2
import argparse
import numpy as np
import transform

class WOB:
    def process_image(image):
        kernel = np.ones((6, 6), np.uint8)
        binary_img = cv2.erode(image, kernel, iterations = 1)
        return binary_img
    
    def getWOB(image):
        
        imagecopy = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,41,11)
        
        cv2.imshow("thresh", thresh)
        
        # Filter out all numbers and noise to isolate only boxes
        cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        max_area = 0
        c = 0
        s = 0
        for i in cnts:
            area = cv2.contourArea(i)
            if area > 8000:
                    if area > max_area:
                        max_area = area
                        best_cnt = i
                        image = cv2.drawContours(image, cnts, c, (0, 255, 0), 3)
                        s = s+1
            c+=1
        if s == 0:
            return False
        alist = best_cnt.reshape(best_cnt.shape[0], best_cnt.shape[2])
        xmax, ymax = np.max(alist, axis = 0)
        xmin, ymin = np.min(alist, axis = 0)
        rect = [[xmax, ymin], [xmin, ymin], [xmax, ymax], [xmin, ymax]]
        mask = np.zeros((gray.shape),np.uint8)
        cv2.drawContours(mask,[best_cnt],0,255,-1)
        cv2.drawContours(mask,[best_cnt],0,0,2)
        result = transform.perspective_transform(mask, imagecopy, rect)
        result = result[ymin:ymax, xmin:xmax]
        cv2.imshow("mask", result)
        cv2.destroyWindow("thresh")
        cv2.destroyWindow("mask")
        result = cv2.resize(result,(1000,1000))
        
        return result, max_area
    
    def sort_grid(image, items):
        x = []
        y = []
        name = []
        for i in range(len(items)):
            x.append(items[i][0])
            y.append(items[i][1])
            name.append(items[i][2])

        print(x,y,name)
        print(items)
        rows = 4
        cols = 6
        deliver = []
        deliver = [[0 for i in range(cols)] for j in range(rows)] 
        rows = 2
        ret = []
        ret = [[0 for i in range(cols)] for j in range(rows)] 
        rows = 6
        order = [[0 for i in range(cols)] for j in range(rows)] 
        w,h,c = np.shape(image)
        colsize = w/7
        rowsize = h/7
        count = len(items)
        for i in range(0, cols):
            for j in range(0, rows):
                for counts in range(count):
                    if x[counts] > colsize*(i+1) and x[counts] < colsize*(i+2) and y[counts] > rowsize*(j+1) and y[counts] < rowsize*(j+2):
                        order[j][i] = name[counts]

        for i in range(4):
            deliver[i] = order[i]
        for i in range(2):
            ret[i] = order[i+4]
        with open('debug.txt', 'w') as f:
            f.write(str(deliver))
            f.write(str(ret))
        return deliver, ret
