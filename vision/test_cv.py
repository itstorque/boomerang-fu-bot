import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('test3.png')
img2 = img.copy()
template = cv.imread('watermelon.png')
w, h, _ = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF_NORMED']
# 'cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            # 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()

# import cv2

# method = cv2.TM_SQDIFF_NORMED

# # Read the images from the file
# small_image = cv2.imread('watermelon.png')
# large_image = cv2.imread('test3.png')

# result = cv2.matchTemplate(small_image, large_image, method)

# # We want the minimum squared difference
# mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# print(mn)

# # Draw the rectangle:
# # Extract the coordinates of our best match
# MPx,MPy = mnLoc

# # Step 2: Get the size of the template. This is the same size as the match.
# trows,tcols = small_image.shape[:2]

# # Step 3: Draw the rectangle on large_image
# cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# large_image = cv2.resize(large_image, (1000,650))

# # Display the original image with the rectangle around the match.
# cv2.imshow('output',large_image)

# # The image is only displayed if we call this
# cv2.waitKey(0)

# # import numpy as np
# # import cv2
  
     
# # # Read the query image as query_img
# # # and train image This query image
# # # is what you need to find in train image
# # # Save it in the same directory
# # # with the name image.jpg 
# # query_img = cv2.imread('watermelon.png')
# # train_img = cv2.imread('test1.png')
  
# # # Convert it to grayscale
# # query_img_bw = cv2.cvtColor(query_img,cv2.COLOR_BGR2GRAY)
# # train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)
  
# # # Initialize the ORB detector algorithm
# # orb = cv2.ORB_create()
  
# # # Now detect the keypoints and compute
# # # the descriptors for the query image
# # # and train image
# # queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw,None)
# # trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw,None)
 
# # # Initialize the Matcher for matching
# # # the keypoints and then match the
# # # keypoints
# # matcher = cv2.BFMatcher()
# # matches = matcher.match(queryDescriptors,trainDescriptors)
  
# # # draw the matches to the final image
# # # containing both the images the drawMatches()
# # # function takes both images and keypoints
# # # and outputs the matched query image with
# # # its train image
# # final_img = cv2.drawMatches(query_img, queryKeypoints,
# # train_img, trainKeypoints, matches[:20],None)
  
# # final_img = cv2.resize(final_img, (1000,650))
 
# # # Show the final image
# # cv2.imshow("Matches", final_img)
# # cv2.waitKey(0)