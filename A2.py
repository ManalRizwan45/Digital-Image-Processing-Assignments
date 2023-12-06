import cv2
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from itertools import accumulate
import operator
from tkinter import filedialog

def cumulative_sum(input_list):
    cumulative_sum_iter = accumulate(input_list, operator.add)
    return list(cumulative_sum_iter)

def histogram_equalization(img,newimg,oldimg,option):
 
# finding the gray level values in the image
 glv=np.unique(img)
 oldglv=glv.tolist()
 img1=img.tolist()
 fre=[]
 nglv=[]
 maxglv=max(oldglv)
 k=0
 
 # intializing the frequencies array
 for i in range(0,len(oldglv),1):
    fre.append(0)
 
 # calculating the frequency of gray level values
 for i in range(0,len(glv),1):
  for j in range(0,len(img),1):
   if(oldglv[i]==img1[j]):
    fre[i]=fre[i]+1
    
# calculating the cumulative frequencies
 nglv=cumulative_sum(fre)
 
# calculating the new gray level values
 for i in range(0,len(nglv),1):
    nglv[i]=nglv[i]/len(img1)
    nglv[i]=nglv[i]*maxglv
    nglv[i]=round(nglv[i])

 
 # creating a dictionary of old gray level values and new gray level values
 gray_level_map = dict(zip(oldglv, nglv))

# Loop through the old gray level values and replace them with the corresponding new gray level values

 newimg = [[gray_level_map[oldglv] for oldglv in row] for row in oldimg]

 if(option==1):
# displaying the images
 
  fig, axs = plt.subplots(1, 2, figsize=(8, 4))

  axs[0].imshow(oldimg,cmap='gray')
  axs[0].set_title('Image Before Histogram Equalization')

  axs[1].imshow(newimg,cmap='gray')
  axs[1].set_title('Image After Histogram Equalization')

  for ax in axs.flat:
    ax.set(xticks=[], yticks=[])
  
  plt.show()
 return newimg
  


def Histogram_Stretch(img,newimg,option):
   min=img[0][0]
   max=-1
   #finding the min gray level value
   for i in range(0,len(img),1):
        for j in range(0,len(img[0]),1):
           if min > img[i][j]:
              min=img[i][j]
   
    #finding the max gray level value
   for i in range(0,len(img),1):
        for j in range(0,len(img[0]),1):
           if max < img[i][j]:
              max=img[i][j]
  
    #Applying the Formula
   rmax=255
   rmin=0
   
   for i in range(0,len(img),1):
        for j in range(0,len(img[0]),1):
          newimg[i][j]=(((img[i][j]-min)/(max-min))*(rmax-rmin))+rmin
          
    
   if (option==1):
   # displaying the images
  
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
    axs[0].imshow(img,cmap='gray')
    axs[0].set_title('Image Before Histogram Stretch')

    axs[1].imshow(newimg,cmap='gray')
    axs[1].set_title('Image After Histogram Stretch')

    for ax in axs.flat:
     ax.set(xticks=[], yticks=[])
  
    plt.show()
   return newimg
  
 
def ACE_filter():

   #Getting k1,k2,N
   k1=float(entry1.get())
   k2=float(entry2.get())
   n=int(entry3.get())

   #Getting The Image
   file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
   oldimg=cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
   newimg=np.empty(shape=oldimg.shape)
   newimg.fill(255)


   mean=np.mean(oldimg)
   i=0
   j=0
   m=n
   p=n

   # copying the border of the old image
   for x in range(0,len(oldimg),1):
      for y in range(0,len(oldimg[0]),1):
         if (x==len(oldimg)-1) or (y==len(oldimg[0])-1) or x==0 or y==0:
            newimg[x][y]=oldimg[x][y]
            
   # applying the ACE filter
   while(m<=len(oldimg)):
    j=0
    p=n
    while(p<=len(oldimg[0])):
         
         window=oldimg[i:m,j:p]
         std=np.std(window)

         if(std!=0):
           local_mean=np.mean(window)
           product1=mean/std
           product1=product1*k1
           product1=product1*(oldimg[i+(n//2)][j+(n//2)]-local_mean)
           newimg[i+(n//2)][j+(n//2)]=product1+(k2*local_mean)
           newimg[i+(n//2)][j+(n//2)]=int(newimg[i+(n//2)][j+(n//2)])

         else:
           newimg[i+(n//2)][j+(n//2)]=oldimg[i+(n//2)][j+(n//2)]
           
         if(newimg[i+(n//2)][j+(n//2)]<0 ):
            newimg[i+(n//2)][j+(n//2)]=0

         if(newimg[i+(n//2)][j+(n//2)]>255):
            newimg[i+(n//2)][j+(n//2)]=255
         
         j=j+1
         p=p+1

    i=i+1
    m=m+1
    
   # post-processing

   flatimg=newimg.flatten()
   _newimg=np.empty(shape=newimg.shape)
   _newimg.fill(0)
   histogram_equalization(flatimg,_newimg,newimg,1)
   
def Color_Enhancement():

   #Getting the Desired Color Space
   space=entry4.get()

   if(space=='hsl' or space=='HSL'):
    
    #Getting The Image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    oldimg=cv2.imread(file_path,cv2.IMREAD_COLOR)
    oldimg = cv2.cvtColor(oldimg, cv2.COLOR_BGR2RGB)
    newimg=cv2.cvtColor(oldimg,cv2.COLOR_RGB2HLS)
    
    # Extracting the three channels
    H, S, L= cv2.split(newimg)
    
    
    #Applying Histogram Equalization on the Saturation Band
    flatS=S.flatten()
    newS=np.empty(shape=S.shape)
    newS.fill(0)
    newS=histogram_equalization(flatS,newS,S,0)
    newS=np.array(newS)

   #Applying Histogram Stretch on the Lightness Band
    newL=np.empty(shape=L.shape)
    newL.fill(0)
    newL=Histogram_Stretch(L,newL,0)
    newL=np.array(newL)
    
   #Typecasting 
    newS = newS.astype(np.uint8)
    newL = newL.astype(np.uint8)

   #Merging the three channels
    merge_img = cv2.merge((H,newS,newL))
    
   #Converting the color image back to RGB space
    enhanced_img = cv2.cvtColor(merge_img, cv2.COLOR_HLS2RGB)
    
   # displaying the images
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))

    axs[0].imshow(oldimg)
    axs[0].set_title('Image Before Color Enhancement in the HSL Space')

    axs[1].imshow(enhanced_img)
    axs[1].set_title('Image After Color Enhancement in the HSL Space')

    for ax in axs.flat:
      ax.set(xticks=[], yticks=[])
  
    plt.show()

   if(space=='hsv' or space=='HSV'):
    
    #Getting The Image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    oldimg=cv2.imread(file_path,cv2.IMREAD_COLOR)
    oldimg = cv2.cvtColor(oldimg, cv2.COLOR_BGR2RGB)
    newimg=cv2.cvtColor(oldimg,cv2.COLOR_RGB2HSV)
    
    # Extracting the three channels
    H, S, V= cv2.split(newimg)
    
    #Applying Histogram Equalization on the Saturation Band
    flatS=S.flatten()
    newS=np.empty(shape=S.shape)
    newS.fill(0)
    newS=histogram_equalization(flatS,newS,S,0)
    newS=np.array(newS)

   #Applying Histogram Stretch on the Lightness Band
    newV=np.empty(shape=V.shape)
    newV.fill(0)
    newV=Histogram_Stretch(V,newV,0)
    newV=np.array(newV)
    
   #Typecasting 
    newS = newS.astype(np.uint8)
    newV = newV.astype(np.uint8)

   #Merging the three channels
    merge_img = cv2.merge((H,newS,newV))
    
   #Converting the color image back to RGB space
    enhanced_img = cv2.cvtColor(merge_img, cv2.COLOR_HSV2RGB)
    
   # displaying the images
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))

    axs[0].imshow(oldimg)
    axs[0].set_title('Image Before Color Enhancement in the HSV Space')

    axs[1].imshow(enhanced_img)
    axs[1].set_title('Image After Color Enhancement in the HSV Space')

    for ax in axs.flat:
      ax.set(xticks=[], yticks=[])
  
    plt.show()
    
    


#GUI
window= tk.Tk()

#ACE Filter Button

#Getting K1
label1 = tk.Label(window, text = "k1:",font=('Arial',14))
label1.place(x=300,y=100)
entry1=tk.Entry(window)
entry1.place(x=350,y=105)

#Getting K2
label2 = tk.Label(window, text = "k2:",font=('Arial',14))
label2.place(x=300,y=130)
entry2=tk.Entry(window)
entry2.place(x=350,y=135)

#Getting Window Size N
label3 = tk.Label(window, text = "N:",font=('Arial',14))
label3.place(x=300,y=160)
entry3=tk.Entry(window)
entry3.place(x=350,y=165)

#Calling the Function
button1=tk.Button(window,text="ACE Filter",font=('Arial',16),command= lambda: ACE_filter())
button1.place(x=350,y=20)

# Color Enhancement Button

#Getting the Desired Color Space
label4=tk.Label(window,text="Enter Color Space:",font=("Arial",14))
label4.place(x=925,y=100)
entry4=tk.Entry(window)
entry4.place(x=1105,y=105)

#Calling the Function
button2=tk.Button(window,text="Color Enhancement",font=('Arial',16),command= lambda: Color_Enhancement())
button2.place(x=1050,y=20)


window.mainloop()



