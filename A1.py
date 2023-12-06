import cv2
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

def digital_negative(img,row,newimg):
    max=-1
    #finding the max gray level value
    for i in range(0,row,1):
        for j in range(0,row,1):
            if(max<img[i][j]):
                max=img[i][j]
    #Applying the Formula
    for i in range(0,row,1):
        for j in range(0,row,1):
            newimg[i][j]=max-img[i][j]
    
    images=[img,newimg]
    for x in images:
     plt.imshow(x)
     plt.gray()
     plt.show()
    

def Linear_Mapping(img,newimg,row,col):
  #Getting x1,y1,x2,y2
  x1=entry1.get()
  x1=int(x1)
  y1=entry2.get()
  y1=int(y1)
  x2=entry3.get()
  x2=int(x2)
  y2=entry4.get()
  y2=int(y2)
  #Calculating m and b
  m=float((y2-y1)/(x2-x1))
  b=float(y1-(m*x1))
  #Applying the Formula
  for i in range(0,row,1):
        for j in range(0,col,1):
            if img[i][j]>=x1 and img[i][j]<=x2:
                y=(m*img[i][j])+b
                newimg[i][j]=y
            else:
              newimg[i][j]=img[i][j]

  images=[img,newimg]
  for x in images:
   plt.imshow(x)
   plt.gray()
   plt.show()

def Histogram_Stretch(img,newimg,row):
   min=img[0][0]
   max=-1
   #finding the min gray level value
   for i in range(0,row,1):
        for j in range(0,row,1):
           if min > img[i][j]:
              min=img[i][j]
   
    #finding the max gray level value
   for i in range(0,row,1):
        for j in range(0,row,1):
           if max < img[i][j]:
              max=img[i][j]
  
    #Applying the Formula
   rmax=entry5.get()
   rmin=entry6.get()
   rmax=int(rmax)
   rmin=int(rmin)
   
   
   for i in range(0,row,1):
        for j in range(0,row,1):
          newimg[i][j]=(((img[i][j]-min)/(max-min))*(rmax-rmin))+rmin
    
   images=[img,newimg]
   for x in images:
    plt.imshow(x)
    plt.gray()
    plt.show()

def Histogram_Shrink(img,newimg,row,col):
    min=10000000
    max=-1
   #finding the min gray level value
    for i in range(0,row,1):
        for j in range(0,col,1):
           if min > img[i][j]:
              min=img[i][j]
   
    #finding the max gray level value
    for i in range(0,row,1):
        for j in range(0,col,1):
           if max < img[i][j]:
              max=img[i][j]
    
    
     #Applying the Formula
    rmax=entry7.get()
    rmin=entry8.get()
    rmax=int(rmax)
    rmin=int(rmin)
    
    for i in range(0,row,1):
        for j in range(0,col,1):
           newimg[i][j]=(((rmax-rmin)/(max-min))*(img[i][j]-min))+rmin
          
     
    images=[img,newimg]
    for x in images:
     plt.imshow(x)
     plt.gray()
     plt.show()

def Gamma_Correction(img,newimg,row,col):
   
   
   gamma=entry10.get()
   
   gamma=int(gamma)

   for i in range(0,row,1):
        for j in range(0,col,1):
           newimg[i][j]=img[i][j]**gamma
           
   

   images=[img,newimg]
   for x in images:
     plt.imshow(x)
     plt.gray()
     plt.show()




  


#digital negative and Histogram Stretch sample image
img1=cv2.imread(r"C:\Users\92321\img2.bmp",cv2.IMREAD_GRAYSCALE)
row1=len(img1)
newimg1=np.empty(shape=img1.shape)
newimg1.fill(0)

#Mapping Linear Equation and Histogram Shrink sample image
img2=cv2.imread(r"C:\Users\92321\img2.bmp",cv2.IMREAD_GRAYSCALE)
row2=len(img2)
col2=len(img2[0])
newimg2=np.empty(shape=img2.shape)
newimg2.fill(0)

#Gamma Correction sample image
img3=cv2.imread(r"C:\Users\92321\img2.bmp",cv2.IMREAD_GRAYSCALE)
row3=len(img3)
col3=len(img3[0])
newimg3=np.empty(shape=img3.shape)
newimg3.fill(0)

#GUI
window= tk.Tk()
#Digital Negative Button
button1=tk.Button(window,text="Digital Negative",font=('Arial',16),command= lambda: digital_negative(img1,row1,newimg1))
button1.place(x=30,y=20)

#Mapping Linear Equations Button
label1 = tk.Label(window, text = "Enter Range:",font=('Arial',14))
label1.place(x=300,y=70)

#getting X1
label2 = tk.Label(window, text = "X1:",font=('Arial',14))
label2.place(x=300,y=100)
entry1=tk.Entry(window)
entry1.place(x=350,y=105)

#getting Y1
label3 = tk.Label(window, text = "Y1:",font=('Arial',14))
label3.place(x=300,y=130)
entry2=tk.Entry(window)
entry2.place(x=350,y=135)

#getting X2
label4 = tk.Label(window, text = "X2:",font=('Arial',14))
label4.place(x=300,y=160)
entry3=tk.Entry(window)
entry3.place(x=350,y=165)

#getting Y2
label5 = tk.Label(window, text = "Y2:",font=('Arial',14))
label5.place(x=300,y=190)
entry4=tk.Entry(window)
entry4.place(x=350,y=195)

#Calling the Function
button2=tk.Button(window,text="Mapping Linear Equation",font=('Arial',16),command= lambda: Linear_Mapping(img2,newimg2,row2,col2))
button2.place(x=300,y=20)

#Gamma Correction button
button3=tk.Button(window,text="Gamma Correction",font=('Arial',16),command= lambda: Gamma_Correction(img3,newimg3,row3,col3))
button3.place(x=700,y=20)

#getting Gamma
label12=tk.Label(window, text = "Gamma:",font=('Arial',14))
label12.place(x=650, y=70)
entry10=tk.Entry(window)
entry10.place(x=730,y=75)

#Histogram Stretching Button
button4=tk.Button(window,text="Histogram Stretching",font=('Arial',16),command= lambda: Histogram_Stretch(img1,newimg1,row1))
button4.place(x=1050,y=20)
label6 = tk.Label(window, text = "Enter Range:",font=('Arial',14))
label6.place(x=1050,y=70)

#getting MAX
label7=tk.Label(window,text="MAX:",font=("Arial",14))
label7.place(x=1050,y=100)
entry5=tk.Entry(window)
entry5.place(x=1105,y=105)

#getting MIN
label8=tk.Label(window,text="MIN:",font=("Arial",14))
label8.place(x=1050,y=130)
entry6=tk.Entry(window)
entry6.place(x=1105,y=135)

#Histogram Shrinking Button
button5=tk.Button(window,text="Histogram Shrinking",font=('Arial',16),command= lambda: Histogram_Shrink(img1,newimg1,row1,row1))
button5.place(x=1350,y=20)
label9 = tk.Label(window, text = "Enter Range:",font=('Arial',14))
label9.place(x=1350,y=70)

#getting MAX
label10=tk.Label(window,text="MAX:",font=("Arial",14))
label10.place(x=1350,y=100)
entry7=tk.Entry(window)
entry7.place(x=1405,y=105)

#getting MIN
label11=tk.Label(window,text="MIN:",font=("Arial",14))
label11.place(x=1350,y=130)
entry8=tk.Entry(window)
entry8.place(x=1405,y=135)


window.mainloop()


