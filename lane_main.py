import cv2
import numpy as np
import matplotlib.pyplot  as plt

"""
This is the unit where magic happens.
"""

image = cv2.imread('road.jpg')

def grayimage(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#lower_yellow = np.array([20,100,100])
#upper_yellow = np.array([30,255,255])

#mask_yellow = cv2.inRange(gray_image,lower_yellow,upper_yellow)

def masking(gray_image):
    mask_white = cv2.inRange(gray_image,230,255)

    #mask_yw = cv2.bitwise_or(mask_white,mask_yellow)
    mask_yw_image = cv2.bitwise_and(gray_image,mask_white)
    return mask_yw_image

def gaussian(mask_yw_image):
    kernel_size = 5
    gauss_gray = cv2.GaussianBlur(mask_yw_image,(5,5),kernel_size) 
    return gauss_gray

def canny(gauss_gray):
    low_threshold = 50
    high_threshold = 150
    canny_edges = cv2.Canny(gauss_gray,low_threshold,high_threshold)
    return canny_edges

def roi(canny_img):
    height = canny_img.shape[0]
    width = canny_img.shape[1]
    #print(height,width)
    polygons = np.array([[(0,height-30),(550,height),(500,310)]])
    mask = np.zeros_like(canny_img)
    cv2.fillPoly(mask,polygons,255)
    return cv2.bitwise_and(canny_img,mask)
    
def tlines(edges,image):
#def tlines(edges):
    MinLineLength = 20
    MaxLineGap = 10
    #lines = cv2.HoughLinesP(masked_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
    lines = cv2.HoughLinesP(edges, 2, np.pi / 180,8,np.array([]),MinLineLength,MaxLineGap)
    print(lines[0])
    for coordinates in lines:
        #print(x1,y1,x2,y2)
        for x1,y1,x2,y2 in coordinates:
            cv2.line(image,(x1,y1),(x2,y2),(0,220,200),8)
        
def writeimage(image):
    cv2.imwrite("result.jpg",image)
##########################


"""


gray_image = grayimage(image)
mask_yw_image = masking(gray_image)
gauss_gray = gaussian(mask_yw_image)
canny_edges = canny(gauss_gray)
section = roi(canny_edges)

plt.imshow(canny_edges)
plt.show()


plt.imshow(image)
plt.show()
plt.imshow(section)
plt.show()

lines = tlines(section)

#writeimage();



plt.imshow(image)
plt.show()
"""