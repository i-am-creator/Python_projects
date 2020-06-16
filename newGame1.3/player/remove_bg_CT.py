
import cv2
import numpy as np
import time
import glob
tm =[]
#== Parameters           
BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 1
MASK_ERODE_ITER = 2
MASK_COLOR = (0,1,1) # In BGR format

### UPDATE PATH ###

paths = glob.glob("fill_size/*.png")
for path in paths:
  start_time = time.time()
  #-- Read image
  print(path)
  img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
  alpha = img[:,:,3]
  img = img[:,:,:3]
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

  #-- Edge detection 
  edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
  edges = cv2.dilate(edges, None)
  edges = cv2.erode(edges, None)
  cv2.imwrite("edges.jpg",edges)
  #-- Find contours in edges, sort by area 

  contour_info = []
  contours,_ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
  for c in contours:
      contour_info.append((
          c,
          cv2.isContourConvex(c),
          cv2.contourArea(c),
      ))
  contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
  max_contour = contour_info[0]
  
  ###  PLAY WITH THIS contour_info_top ###

  contour_info_top = contour_info
  mask = np.zeros(edges.shape)
  for max_contour in contour_info_top:
    #-- Create empty mask, draw filled polygon on it corresponding to largest contour ----
    # Mask is black, polygon is white
    cv2.fillConvexPoly(mask, max_contour[0], (255))
  
    cv2.imwrite("mask.jpg",mask)
  
  #-- Smooth mask, then blur it
  mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
  mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
  # mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
  mask_stack = np.dstack([mask]*3)    # Create 3-channel alpha mask
  cv2.imwrite("mask_.jpg",mask)

  #-- Blend masked img into MASK_COLOR background
  mask_stack  = mask_stack.astype('float32') / 255.0         
  #mask_stack2  = mask_stack2.astype('float32') / 255.0         
  img         = img.astype('float32') / 255.0    
  masked = (mask_stack * img) + ((1-mask_stack) * MASK_COLOR) 
  masked = (masked * 255).astype('uint8')                    
  masked = np.dstack([masked, mask])
  cv2.imwrite(path[:-4] + "_.png",masked)
  tm.append(time.time() - start_time)
  print("avg time pre pic is", sum(tm)/len(tm))
print("total time :", sum(tm))

