# Importing all necessary libraries
import cv2
import os
#import time

# Read the video from specified path  ####CHANGE1

#need to automate for all video
cam = cv2.VideoCapture("C:/Users/Naman Pundir/Documents/CSE700/Videos Dataset/VID (14).mp4")



try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0
count = 0
while (True):
    
    # reading from frame
    ret, frame = cam.read()
    count = count + 1
   
    
   ####CHANGE2
   ###########int( ( total minutes * 60 ) / (timestamps need) ) #######IMPORTANT
    if count % 220 == 0:
        
        
        if ret:
            # if video is still left continue creating images
            
            
            
            ####CHANGE3
            name = './data/imggggggggggggggggg' + str(currentframe) + '.jpg'
            print('Creating...' + name)
    
    
    
            # writing the extracted images
            cv2.imwrite(name, frame)
    
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
        
        
        
        ####CHANGE4 (total seconds in the video)
    elif count > 4740:
        
        
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()