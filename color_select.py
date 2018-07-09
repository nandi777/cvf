import matplotlib.pyplot as plt
import matplotlib.image as mping
import numpy as np
import cv2


# image = cv2.imread(r'./cvf/test.jpg')
image = mping.imread(r'./cvf/test.jpg')

print('This image is:', type(image), 'with dimensions:', image.shape)

# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)

# Define color selection criteria
###### MODIFY THESE VARIABLES TO MAKE YOUR COLOR SELECTION
red_threshold = 200
green_threshold = 200
blue_threshold = 200
######

rgb_threshold = [red_threshold, green_threshold, blue_threshold]

# Do a boolean or with the "|" character to identify
# pixels below the thresholds
thresholds = (image[:, :, 0] < rgb_threshold[0]) \
            | (image[:, :, 1] < rgb_threshold[1]) \
            | (image[:, :, 2] < rgb_threshold[2])
color_select[thresholds] = [0, 0, 0]

plt.imshow(color_select)
plt.show()