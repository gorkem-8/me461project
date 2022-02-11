import numpy as np
import time
class backspacex:
   def __init__(self, userName, clrDictionary, maxStepSize, maxTime):
      self.name = userName # your object will be given a user name, i.e. your group name
      self.maxStep = maxStepSize # maximum length of the returned path from run()
      self.maxTime = maxTime # run() is supposed to return before maxTime
      
   def run(self, img, info):
      myinfo = info[self.name]
        # get current location 
      loc, game_point = info[self.name]
      y,x = loc # get current y,x coordinates
      a=0
      colorpoint=0
      rang=50
      i=0
      while i<12:
         i=i+1
         
         if i==1:
            if y-rang<0 or x-rang<0:
               continue
            if all(img[y-rang,x-rang]==[255,255,255]):
               colorpoint=0
            
            elif all(img[y-rang,x-rang]==[225,1,1]):
               colorpoint=100
               goal=[[y,x-rang],[y-rang,x-rang]]
               break
               
            elif all(img[y-rang,x-rang]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]]
            
            elif all(img[y-rang,x-rang]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]]
              
            elif all(img[y-rang,x-rang]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]] 
             
            elif all(img[y-rang,x-rang]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]]
            
            elif all(img[y-rang,x-rang]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]]
            
            elif all(img[y-rang,x-rang]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]]
                  
            elif all(img[y-rang,x-rang]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]]
            
            elif all(img[y-rang,x-rang]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]]
                  
            elif all(img[y-rang,x-rang]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]]
                  
            elif all(img[y-rang,x-rang]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]]
            
            elif all(img[y-rang,x-rang]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]]
            
            elif all(img[y-rang,x-rang]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]]
            
            elif all(img[y-rang,x-rang]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y-rang,x-rang]]
               
         elif i==2:
            if y-rang<0:
               continue
            if all(img[y-rang,x-1]==[255,255,255]):
               colorpoint=0
            
            elif all(img[y-rang,x-1]==[225,1,1]):
               colorpoint=100
               goal=[[y,x-1],[y-rang,x-1]]
               break
               
            elif all(img[y-rang,x-1]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
            
            elif all(img[y-rang,x-1]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
              
            elif all(img[y-rang,x-1]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
             
            elif all(img[y-rang,x-1]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
            
            elif all(img[y-rang,x-1]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
            
            elif all(img[y-rang,x-1]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
                  
            elif all(img[y-rang,x-1]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
            
            elif all(img[y-rang,x-1]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
                  
            elif all(img[y-rang,x-1]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
                  
            elif all(img[y-rang,x-1]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
            
            elif all(img[y-rang,x-1]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
            
            elif all(img[y-rang,x-1]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
            
            elif all(img[y-rang,x-1]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang,x-1]]
               
         elif i==3:
            if x+rang>750 or y-rang<0:
               continue
            if all(img[y-rang,x+rang]==[255,255,255]):
               colorpoint=0
               
            elif all(img[y-rang,x+rang]==[225,1,1]):
               colorpoint=100
               goal=[[y,x+rang],[y-rang,x+rang]]
               break
               
            elif all(img[y-rang,x+rang]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]

            elif all(img[y-rang,x+rang]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]

            elif all(img[y-rang,x+rang]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]

            elif all(img[y-rang,x+rang]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]

            elif all(img[y-rang,x+rang]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]

            elif all(img[y-rang,x+rang]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]

            elif all(img[y-rang,x+rang]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]

            elif all(img[y-rang,x+rang]==[150,1,150]):
               colorpoint=6
               if colorpoint>a: 
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]

            elif all(img[y-rang,x+rang]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]

            elif all(img[y-rang,x+rang]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]

            elif all(img[y-rang,x+rang]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]

            elif all(img[y-rang,x+rang]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]

            elif all(img[y-rang,x+rang]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang],[y-rang,x+rang]]
               
              
               
              
         elif i==4:
               if x+rang>750:
                  continue
               if all(img[y,x+rang]==[255,255,255]):
                  colorpoint=0
            
               elif all(img[y,x+rang]==[225,1,1]):
                  colorpoint=100
                  goal=[[y,x+rang],[y+1,x+rang]]
                  break

               elif all(img[y,x+rang]==[1,255,1]):
                  colorpoint=50
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]

               elif all(img[y,x+rang]==[1,1,255]):
                  colorpoint=30
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]

               elif all(img[y,x+rang]==[200,200,1]):
                  colorpoint=20
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]

               elif all(img[y,x+rang]==[255,1,255]):
                  colorpoint=10
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]

               elif all(img[y,x+rang]==[1,255,255]):
                  colorpoint=9
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]

               elif all(img[y,x+rang]==[1,1,150]):
                  colorpoint=8
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]

               elif all(img[y,x+rang]==[120,120,40]):
                  colorpoint=7
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]

               elif all(img[y,x+rang]==[150,1,150]):
                  colorpoint=6
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]

               elif all(img[y,x+rang]==[1,150,150]):
                  colorpoint=5
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]

               elif all(img[y,x+rang]==[222,55,222]):
                  colorpoint=4
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]

               elif all(img[y,x+rang]==[1,99,55]):
                  colorpoint=3
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]

               elif all(img[y,x+rang]==[200,100,10]):
                  colorpoint=2
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]

               elif all(img[y,x+rang]==[100,10,200]):
                  colorpoint=1
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+1,x+rang]]
               
         elif i==5:
               if (x+rang>750) or (y+rang>750):
                  continue
               if all(img[y+rang,x+rang]==[255,255,255]):
                  colorpoint=0

               elif all(img[y+rang,x+rang]==[225,1,1]):
                  colorpoint=100
                  goal=[[y,x+rang],[y+rang,x+rang]]
                  break

               elif all(img[y+rang,x+rang]==[1,255,1]):
                  colorpoint=50
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]

               elif all(img[y+rang,x+rang]==[1,1,255]):
                  colorpoint=30
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]

               elif all(img[y+rang,x+rang]==[200,200,1]):
                  colorpoint=20
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]

               elif all(img[y+rang,x+rang]==[255,1,255]):
                  colorpoint=10
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]

               elif all(img[y+rang,x+rang]==[1,255,255]):
                  colorpoint=9
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]

               elif all(img[y+rang,x+rang]==[1,1,150]):
                  colorpoint=8
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]

               elif all(img[y+rang,x+rang]==[120,120,40]):
                  colorpoint=7
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]

               elif all(img[y+rang,x+rang]==[150,1,150]):
                  colorpoint=6
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]

               elif all(img[y+rang,x+rang]==[1,150,150]):
                  colorpoint=5
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]

               elif all(img[y+rang,x+rang]==[222,55,222]):
                  colorpoint=4
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]

               elif all(img[y+rang,x+rang]==[1,99,55]):
                  colorpoint=3
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]

               elif all(img[y+rang,x+rang]==[200,100,10]):
                  colorpoint=2
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]

               elif all(img[y+rang,x+rang]==[100,10,200]):
                  colorpoint=1
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+rang],[y+rang,x+rang]]        
            
         elif i==6:
            if y+rang>750:
               continue
            if all(img[y+rang,x]==[255,255,255]):
               colorpoint=0
            
            elif all(img[y+rang,x]==[225,1,1]):
               colorpoint=100
               goal=[[y,x-1],[y+rang,x-1]]
               break
               
            elif all(img[y+rang,x]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]]
            
            elif all(img[y+rang,x]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]]
              
            elif all(img[y+rang,x]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]]
             
            elif all(img[y+rang,x]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]]
            
            elif all(img[y+rang,x]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]]
            
            elif all(img[y+rang,x]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]]
                  
            elif all(img[y+rang,x]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]]
            
            elif all(img[y+rang,x]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]]
                  
            elif all(img[y+rang,x]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]]
                  
            elif all(img[y+rang,x]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]]
            
            elif all(img[y+rang,x]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]]
            
            elif all(img[y+rang,x]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]]
            
            elif all(img[y+rang,x]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang,x-1]] 
               
         elif i==7:
            if y+rang>750 or x-rang<0:
               continue
            if all(img[y+rang,x-rang]==[255,255,255]):
               colorpoint=0
            
            elif all(img[y+rang,x-rang]==[225,1,1]):
               colorpoint=100
               goal=[[y,x-rang],[y+rang,x-rang]]
               break
               
            elif all(img[y+rang,x-rang]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
            
            elif all(img[y+rang,x-rang]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
              
            elif all(img[y+rang,x-rang]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
             
            elif all(img[y+rang,x-rang]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
            
            elif all(img[y+rang,x-rang]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
            
            elif all(img[y+rang,x-rang]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
                  
            elif all(img[y+rang,x-rang]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
            
            elif all(img[y+rang,x-rang]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
                  
            elif all(img[y+rang,x-rang]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
                  
            elif all(img[y+rang,x-rang]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
            
            elif all(img[y+rang,x-rang]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
            
            elif all(img[y+rang,x-rang]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
            
            elif all(img[y+rang,x-rang]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+rang,x-rang]]
                  
         elif i==8:
            if x-rang<0:
               continue
            if all(img[y,x-rang]==[255,255,255]):
               colorpoint=0
            
            elif all(img[y,x-rang]==[225,1,1]):
               colorpoint=100
               goal=[[y,x-rang],[y+1,x-rang]]
               break
               
            elif all(img[y,x-rang]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
            
            elif all(img[y,x-rang]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
              
            elif all(img[y,x-rang]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
             
            elif all(img[y,x-rang]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
            
            elif all(img[y,x-rang]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
            
            elif all(img[y,x-rang]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
                  
            elif all(img[y,x-rang]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
            
            elif all(img[y,x-rang]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
                  
            elif all(img[y,x-rang]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
                  
            elif all(img[y,x-rang]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
            
            elif all(img[y,x-rang]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
            
            elif all(img[y,x-rang]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
            
            elif all(img[y,x-rang]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang],[y+1,x-rang]]
         
         elif i==9:
            if y-rang*2<0:
               continue
            if all(img[y-rang*2,x]==[255,255,255]):
               colorpoint=0
            
            elif all(img[y-rang*2,x]==[225,1,1]):
               colorpoint=100
               goal=[[y,x-1],[y-rang*2,x-1]]
               break
               
            elif all(img[y-rang*2,x]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
            
            elif all(img[y-rang*2,x]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
              
            elif all(img[y-rang*2,x]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
             
            elif all(img[y-rang*2,x]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
            
            elif all(img[y-rang*2,x]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
            
            elif all(img[y-rang*2,x]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
                  
            elif all(img[y-rang*2,x]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
            
            elif all(img[y-rang*2,x]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
                  
            elif all(img[y-rang*2,x]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
                  
            elif all(img[y-rang*2,x]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
            
            elif all(img[y-rang*2,x]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
            
            elif all(img[y-rang*2,x]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
            
            elif all(img[y-rang*2,x]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang*2,x-1]]
            
         elif i==10:
            if x+rang*2>750:
               continue
            if all(img[y,x+rang*2]==[255,255,255]):
               colorpoint=0
            
            elif all(img[y,x+rang*2]==[225,1,1]):
               colorpoint=100
               goal=[[y,x+rang*2],[y+1,x+rang*2]]
               break
               
            elif all(img[y,x+rang*2]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
            
            elif all(img[y,x+rang*2]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
              
            elif all(img[y,x+rang*2]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
             
            elif all(img[y,x+rang*2]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
            
            elif all(img[y,x+rang*2]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
            
            elif all(img[y,x+rang*2]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
                  
            elif all(img[y,x+rang*2]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
            
            elif all(img[y,x+rang*2]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
                  
            elif all(img[y,x+rang*2]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
                  
            elif all(img[y,x+rang*2]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
            
            elif all(img[y,x+rang*2]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
            
            elif all(img[y,x+rang*2]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
            
            elif all(img[y,x+rang*2]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang*2],[y+1,x+rang*2]]
            
         elif i==11:
            if y+rang*2>750:
               continue
            if all(img[y+rang*2,x]==[255,255,255]):
               colorpoint=0
            
            elif all(img[y+rang*2,x]==[225,1,1]):
               colorpoint=100
               goal=[[y,x-1],[y+rang*2,x-1]]
               break
               
            elif all(img[y+rang*2,x]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
            
            elif all(img[y+rang*2,x]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
              
            elif all(img[y+rang*2,x]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
             
            elif all(img[y+rang*2,x]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
            
            elif all(img[y+rang*2,x]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
            
            elif all(img[y+rang*2,x]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
                  
            elif all(img[y+rang*2,x]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
            
            elif all(img[y+rang*2,x]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
                  
            elif all(img[y+rang*2,x]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
                  
            elif all(img[y+rang*2,x]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
            
            elif all(img[y+rang*2,x]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
            
            elif all(img[y+rang*2,x]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
            
            elif all(img[y+rang*2,x]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang*2,x-1]]
            
         elif i==12:
            if x-rang*2<0:
               continue
            if all(img[y,x-rang*2]==[255,255,255]):
               colorpoint=0
            
            elif all(img[y,x-rang*2]==[225,1,1]):
               colorpoint=100
               goal=[[y,x-rang*2],[y-1,x-rang*2]]
               break
               
            elif all(img[y,x-rang*2]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
            
            elif all(img[y,x-rang*2]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
              
            elif all(img[y,x-rang*2]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
             
            elif all(img[y,x-rang*2]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
            
            elif all(img[y,x-rang*2]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
            
            elif all(img[y,x-rang*2]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
                  
            elif all(img[y,x-rang*2]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
            
            elif all(img[y,x-rang*2]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
                  
            elif all(img[y,x-rang*2]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
                  
            elif all(img[y,x-rang*2]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
            
            elif all(img[y,x-rang*2]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
            
            elif all(img[y,x-rang*2]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
            
            elif all(img[y,x-rang*2]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang*2],[y-1,x-rang*2]]
         if a==0 and i==12:
            i=0
            rang=rang*2            
         
      return goal
