# generate spatially-correlated heterogeneous sections from weibul distrubution using inverse transform method
import numpy as np
from PIL import Image
from random import *

a=45.
b=90.
x = np.arange(0.,a,1.)
y = np.arange(0.,b,1.)

[X, Y] = np.meshgrid(x,y)


m=3.
theta=1.

# producing data according to Weibul distribution
I=np.zeros((np.size(y),np.size(x)))
for i in range(np.size(y)):
    for j in range(np.size(x)):
        I[i,j]=(-np.log(1-random()))**(1/m)
# incorporating spatial correlation        
print([I.min(),I.max()])
I2=np.zeros((np.size(y),np.size(x)))
for i in range(np.size(y)):
    for j in range(np.size(x)):
        W=0.
        for k in range(np.size(y)):
            for l in range(np.size(x)):                
                I2[i,j]=I2[i,j]\
                         +I[k,l]*np.exp(-np.sqrt((X[i,j]-X[k,l])**2+(Y[i,j]-Y[k,l])**2)/theta)
                W=W+np.exp(-np.sqrt((X[i,j]-X[k,l])**2+(Y[i,j]-Y[k,l])**2)/theta)
        I2[i,j]=I2[i,j]/W
print([I2.min(),I2.max()])

I8 = (((I2 - I2.min()) / (I2.max() - I2.min())) * 255.9).astype(np.uint8)

img = Image.fromarray(I8)
img.save("theta=%2.1f.jpg"%theta)
img=Image.open("theta=%2.1f.jpg"%theta)
img = img.resize((int(10.*a),int(10.*b)))
img.save("theta=%2.1f.jpg"%theta)
