import cv2 as cv
import numpy as np
#s -> normal
#rgb -> RGB color

R = 6 * [0]
normR = 6 * [0]
normG = 6 * [0]
normB = 6 * [0]

for i in range(6):
    rgb_file = 'rgb000' + str(i) + '.exr'
    norm_file = 'normal000' + str(i) + '.exr'
    
    myimg = cv.imread(rgb_file,-1)
    mynorm = cv.imread(norm_file,-1)

    R[i] = myimg[:,:,2]
    normR[i] = mynorm[:,:,2] 
    normG[i] = mynorm[:,:,1]
    normB[i] = mynorm[:,:,0]

R = np.array(R)

#Use [0] only ?
normR = np.array(normR)
normG = np.array(normG)
normB = np.array(normB)
#print (normR,normG,normB)

#print (R[0].shape,normR[0].shape)
#print ('in1,in2,in3,in4,in5,in6')

for i in range(R[0].shape[0]):
    for j in range(R[0].shape[1]):
        print (str(R[0][i][j]) + ',' + str(R[1][i][j]) + ',' + str(R[2][i][j]) + ',' + str(R[3][i][j]) + ',' + str(R[4][i][j]) + ',' + str(R[5][i][j]) + ',' + str(normR[0][i][j]) + ',' + str(normG[0][i][j]) + ',' + str(normB[0][i][j]))       