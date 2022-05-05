import numpy as np
import cv2


    
def perspective_transform(mask, img, rect):
    corners = find_corners(mask)
    print(corners)
    rows,cols = mask.shape
    print(mask.shape)
    # pts1 = np.float32([[corners[0,0],corners[0,1]],[corners[1,0],corners[1,1]],[corners[2,0],corners[2,1]],[corners[3,0],corners[3,1]]])
    pts1 = np.float32([corners[1], corners[2], corners[3], corners[4]])
    # pts2 = np.float32([[rows,0], [0, 0], [0,cols], [rows,cols]])
    pts2 = np.float32(rect)
    M = cv2.getPerspectiveTransform(pts1,pts2)
    # print(M)
    dst = cv2.warpPerspective(img,M,(1000,1000))
    return dst

def find_corners(img):
    cv2.destroyWindow('image')
    img = cv2.blur(img, (5,5))
    dst = cv2.cornerHarris(img,20,3,0.04)
    ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
    dst = np.uint8(dst)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(img,np.float32(centroids),(5,5),(-1,-1),criteria)
    x = 0
    for i in range(1, len(corners)):
        # print(corners[i])
        cv2.circle(img, (int(corners[i,0]), int(corners[i,1])), 7, (255,255,255), 2)
        cv2.putText(img, str(x), (int(corners[i,0]), int(corners[i,1])), cv2.FONT_HERSHEY_COMPLEX, 0.5, (125,125,125), 2)
        x = x+1
    
    cv2.imshow('image', img)
    
    return corners
