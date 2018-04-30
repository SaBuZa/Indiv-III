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
    norm_file = 's000' + str(i) + '.exr'
    #print (sidx, nidx)
    #myimg = cv.imread('s0000.exr',-1)
    #print (type(sidx),type('spc0000.exr'),sidx=='spc0000.exr')
    #nidx = ('s000%s' % i) + '.exr'
    #print (nidx)
    myimg = cv.imread(rgb_file,-1)
    mynorm = cv.imread(norm_file,-1)
    #myimg = cv.imread('s0000.exr',-1)
    
    #print (myimg)
    #print (mynorm)
    
    
    #B = myimg[:,:,0]
    #G = myimg[:,:,1]
    R[i] = myimg[:,:,2]
    normR[i] = mynorm[:,:,2] 
    normG[i] = mynorm[:,:,1]
    normB[i] = mynorm[:,:,0]

R = np.array(R)
normR = np.array(normR)
normG = np.array(normG)
normB = np.array(normB)

#print (R,len(normR),len(normG),len(normB))
#print (B.shape)
'''
for i in range(len(B)):
    for j in range(len(B[i])):
        print (R[i][j],G[i][j],B[i][j])
'''
#print (b)
#print (g)
#print (r)
#print (myimg.shape)