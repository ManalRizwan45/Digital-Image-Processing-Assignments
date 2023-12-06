import cv2
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import filedialog


def add_salt_pepper_noise(oldimg):
   
   newimg=np.empty(shape=oldimg.shape)
   newimg.fill(255)

   probabilities=[0.01,0.02,0.03,0.04,0.05]


   for i in probabilities:
      
      threshold=1-i

      for j in range(0,len(oldimg),1):
         
         for k in range(0,len(oldimg[0]),1):
             
             rand=np.random.random()

             if(rand<i):
              newimg[j][k]=0

             elif(rand>threshold):
               newimg[j][k]=255

             else:
               newimg[j][k]=oldimg[j][k]
   return newimg


            
def AdaptiveMedianFilter():
   
   #getting the window size
   n=int(entry1.get())

   #getting The Image
   file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
   oldimg=cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)

   #intializing the noisy image
   noisy_img=np.empty(shape=oldimg.shape)
   noisy_img.fill(255)

   #intializing the reconstructed image
   newimg=np.empty(shape=oldimg.shape)
   newimg.fill(255)

   #adding salt and pepper noise
   noisy_img=add_salt_pepper_noise(oldimg)
   
   #applying the adaptive median filter

   i=0
   j=0
   m=n
   p=n

   while(m<=len(oldimg)):
    j=0
    p=n
    while(p<=len(oldimg[0])):
         
         window=oldimg[i:m,j:p]
         flat_window=window.flatten()
         median=np.median(flat_window)
         minimum=np.min(flat_window)
         maximum=np.max(flat_window)

         if(minimum < median < maximum):
           
           if(minimum < oldimg[i+(n//2)][j+(n//2)] < maximum):
             
             newimg[i+(n//2)][j+(n//2)]=oldimg[i+(n//2)][j+(n//2)]
           else:
             
             newimg[i+(n//2)][j+(n//2)]=median
         else:

            new_i=i-1
            new_j=j-1
            

            if(new_i<0 or new_j<0):
               new_i=new_i+1
               new_j=new_j+1
               newimg[new_i+(n//2)][new_j+(n//2)]=oldimg[new_i+(n//2)][new_j+(n//2)]
            else:
             new_m=m+1
             new_p=p+1
             new_n=n+2
             check=False

             while(check==False):
            
                 if(new_m>len(oldimg) or new_p>len(oldimg[0])):

                  newimg[new_i+(new_n//2)][new_j+(new_n//2)]=oldimg[new_i+(new_n//2)][new_j+(new_n//2)]
                  check=True

                 else:
                  window=oldimg[new_i:new_m,new_j:new_p]
                  flat_window=window.flatten()
                  median=np.median(flat_window)
                  minimum=np.min(flat_window)
                  maximum=np.max(flat_window)
                  if(minimum < median < maximum):
           
                      if(minimum < oldimg[new_i+(new_n//2)][new_j+(new_n//2)] < maximum):
             
                         newimg[new_i+(new_n//2)][new_j+(new_n//2)]=oldimg[new_i+(new_n//2)][new_j+(new_n//2)]
                         check=True
                      else:
             
                         newimg[new_i+(new_n//2)][new_j+(new_n//2)]=median
                         check=True
                  else:
                     new_i=new_i-1
                     new_j=new_j-1

                     if(new_i<0 or new_j<0):
                        new_i=new_i+1
                        new_j=new_j+1
                        newimg[new_i+(new_n//2)][new_j+(new_n//2)]=oldimg[new_i+(new_n//2)][new_j+(new_n//2)]
                        check=True
                     else:
                      new_m=new_m+1
                      new_p=new_p+1
                      new_n=new_n+2
         j=j+1
         p=p+1

    i=i+1
    m=m+1
   
   #displaying the images
   fig, axs = plt.subplots(1, 2, figsize=(8, 4))

   axs[0].imshow(noisy_img,cmap='gray')
   axs[0].set_title('Image With Added Salt and Pepper Noise')

   axs[1].imshow(newimg,cmap='gray')
   axs[1].set_title('Image After Removing Salt and Pepper Noise')

   for ax in axs.flat:
     ax.set(xticks=[], yticks=[])
  
   plt.show()


#GUI

window= tk.Tk()
button1=tk.Button(window,text="Adaptive Median Filter",font=('Arial',16),command= lambda: AdaptiveMedianFilter())
button1.place(x=750,y=20)
label1=tk.Label(window, text = "Window Size:",font=('Arial',14))
label1.place(x=650, y=70)
entry1=tk.Entry(window)
entry1.place(x=800,y=75)

window.mainloop()
 