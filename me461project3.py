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
      for i in range(1,9):
         if i==1:
            if any(img[y-50,x-50]==[255,255,255]):
               pass
            
            elif any(img[y-50,x-50]==[225,1,1]):
               goal=[[y,x-50],[y-50,x-50]]
               break
               
            elif any(img[y-50,x-50]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]]
            
            elif any(img[y-50,x-50]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]]
              
            elif any(img[y-50,x-50]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]] 
             
            elif any(img[y-50,x-50]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]]
            
            elif any(img[y-50,x-50]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]]
            
            elif any(img[y-50,x-50]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]]
                  
            elif any(img[y-50,x-50]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]]
            
            elif any(img[y-50,x-50]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]]
                  
            elif any(img[y-50,x-50]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]]
                  
            elif any(img[y-50,x-50]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]]
            
            elif any(img[y-50,x-50]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]]
            
            elif any(img[y-50,x-50]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]]
            
            elif any(img[y-50,x-50]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y-50,x-50]]
               
         elif i==2:
     
            if any(img[y-50,x-1]==[255,255,255]):
               pass
            
            elif any(img[y-50,x-1]==[225,1,1]):
               goal=[[y,x-1],[y-50,x-1]]
               break
               
            elif any(img[y-50,x-1]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
            
            elif any(img[y-50,x-1]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
              
            elif any(img[y-50,x-1]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
             
            elif any(img[y-50,x-1]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
            
            elif any(img[y-50,x-1]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
            
            elif any(img[y-50,x-1]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
                  
            elif any(img[y-50,x-1]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
            
            elif any(img[y-50,x-1]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
                  
            elif any(img[y-50,x-1]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
                  
            elif any(img[y-50,x-1]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
            
            elif any(img[y-50,x-1]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
            
            elif any(img[y-50,x-1]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
            
            elif any(img[y-50,x-1]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-50,x-1]]
               
         elif i==3:
            if x+50>740:
               continue
            else:
               
               if any(img[y-50,x+50]==[255,255,255]):
                  pass

               elif any(img[y-50,x+50]==[225,1,1]):
                  goal=[[y,x+50],[y-50,x+50]]
                  break
               
               elif any(img[y-50,x+50]==[1,255,1]):
                  colorpoint=50
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]

               elif any(img[y-50,x+50]==[1,1,255]):
                  colorpoint=30
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]

               elif any(img[y-50,x+50]==[200,200,1]):
                  colorpoint=20
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]

               elif any(img[y-50,x+50]==[255,1,255]):
                  colorpoint=10
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]

               elif any(img[y-50,x+50]==[1,255,255]):
                  colorpoint=9
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]

               elif any(img[y-50,x+50]==[1,1,150]):
                  colorpoint=8
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]

               elif any(img[y-50,x+50]==[120,120,40]):
                  colorpoint=7
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]

               elif any(img[y-50,x+50]==[150,1,150]):
                  colorpoint=6
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]

               elif any(img[y-50,x+50]==[1,150,150]):
                  colorpoint=5
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]

               elif any(img[y-50,x+50]==[222,55,222]):
                  colorpoint=4
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]

               elif any(img[y-50,x+50]==[1,99,55]):
                  colorpoint=3
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]

               elif any(img[y-50,x+50]==[200,100,10]):
                  colorpoint=2
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]

               elif any(img[y-50,x+50]==[100,10,200]):
                  colorpoint=1
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y-50,x+50]]
              
         elif i==4:
            if x+50>740:
               continue
            else:
               if any(img[y,x+50]==[255,255,255]):
                  pass
            
               elif any(img[y-50,x-50]==[225,1,1]):
                  goal=[[y,x+50],[y+1,x+50]]
                  break

               elif any(img[y,x+50]==[1,255,1]):
                  colorpoint=50
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]

               elif any(img[y,x+50]==[1,1,255]):
                  colorpoint=30
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]

               elif any(img[y,x+50]==[200,200,1]):
                  colorpoint=20
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]

               elif any(img[y,x+50]==[255,1,255]):
                  colorpoint=10
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]

               elif any(img[y,x+50]==[1,255,255]):
                  colorpoint=9
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]

               elif any(img[y,x+50]==[1,1,150]):
                  colorpoint=8
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]

               elif any(img[y,x+50]==[120,120,40]):
                  colorpoint=7
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]

               elif any(img[y,x+50]==[150,1,150]):
                  colorpoint=6
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]

               elif any(img[y,x+50]==[1,150,150]):
                  colorpoint=5
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]

               elif any(img[y,x+50]==[222,55,222]):
                  colorpoint=4
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]

               elif any(img[y,x+50]==[1,99,55]):
                  colorpoint=3
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]

               elif any(img[y,x+50]==[200,100,10]):
                  colorpoint=2
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]

               elif any(img[y,x+50]==[100,10,200]):
                  colorpoint=1
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+1,x+50]]
               
         elif i==5:
            if x+50>740:
               continue
            else:
            
               if any(img[y+50,x+50]==[255,255,255]):
                  pass

               elif any(img[y-50,x-50]==[225,1,1]):
                  goal=[[y,x+50],[y+50,x+50]]
                  break

               elif any(img[y+50,x+50]==[1,255,1]):
                  colorpoint=50
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]

               elif any(img[y+50,x+50]==[1,1,255]):
                  colorpoint=30
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]

               elif any(img[y+50,x+50]==[200,200,1]):
                  colorpoint=20
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]

               elif any(img[y+50,x+50]==[255,1,255]):
                  colorpoint=10
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]

               elif any(img[y+50,x+50]==[1,255,255]):
                  colorpoint=9
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]

               elif any(img[y+50,x+50]==[1,1,150]):
                  colorpoint=8
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]

               elif any(img[y+50,x+50]==[120,120,40]):
                  colorpoint=7
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]

               elif any(img[y+50,x+50]==[150,1,150]):
                  colorpoint=6
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]

               elif any(img[y+50,x+50]==[1,150,150]):
                  colorpoint=5
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]

               elif any(img[y+50,x+50]==[222,55,222]):
                  colorpoint=4
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]

               elif any(img[y+50,x+50]==[1,99,55]):
                  colorpoint=3
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]

               elif any(img[y+50,x+50]==[200,100,10]):
                  colorpoint=2
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]

               elif any(img[y+50,x+50]==[100,10,200]):
                  colorpoint=1
                  if colorpoint>a:
                     a=colorpoint
                     goal=[[y,x+50],[y+50,x+50]]        
            
         elif i==6:
            
            if any(img[y+50,x]==[255,255,255]):
               pass
            
            elif any(img[y-50,x-50]==[225,1,1]):
               goal=[[y,x-1],[y+50,x-1]]
               break
               
            elif any(img[y+50,x]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]]
            
            elif any(img[y+50,x]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]]
              
            elif any(img[y+50,x]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]]
             
            elif any(img[y+50,x]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]]
            
            elif any(img[y+50,x]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]]
            
            elif any(img[y+50,x]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]]
                  
            elif any(img[y+50,x]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]]
            
            elif any(img[y+50,x]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]]
                  
            elif any(img[y+50,x]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]]
                  
            elif any(img[y+50,x]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]]
            
            elif any(img[y+50,x]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]]
            
            elif any(img[y+50,x]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]]
            
            elif any(img[y+50,x]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+50,x-1]] 
               
         elif i==7:
            
            if any(img[y+50,x-50]==[255,255,255]):
               pass
            
            elif any(img[y+50,x-50]==[225,1,1]):
               goal=[[y,x-50],[y+50,x-50]]
               break
               
            elif any(img[y+50,x-50]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
            
            elif any(img[y+50,x-50]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
              
            elif any(img[y+50,x-50]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
             
            elif any(img[y+50,x-50]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
            
            elif any(img[y+50,x-50]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
            
            elif any(img[y+50,x-50]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
                  
            elif any(img[y+50,x-50]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
            
            elif any(img[y+50,x-50]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
                  
            elif any(img[y+50,x-50]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
                  
            elif any(img[y+50,x-50]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
            
            elif any(img[y+50,x-50]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
            
            elif any(img[y+50,x-50]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
            
            elif any(img[y+50,x-50]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+50,x-50]]
                  
         elif i==8:
            
            if any(img[y,x-50]==[255,255,255]):
               pass
            
            elif any(img[y-50,x-50]==[225,1,1]):
               goal=[[y,x-50],[y+1,x-50]]
               break
               
            elif any(img[y,x-50]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
            
            elif any(img[y,x-50]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
              
            elif any(img[y,x-50]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
             
            elif any(img[y,x-50]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
            
            elif any(img[y,x-50]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
            
            elif any(img[y,x-50]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
                  
            elif any(img[y,x-50]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
            
            elif any(img[y,x-50]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
                  
            elif any(img[y,x-50]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
                  
            elif any(img[y,x-50]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
            
            elif any(img[y,x-50]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
            
            elif any(img[y,x-50]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
            
            elif any(img[y,x-50]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-50],[y+1,x-50]]
                 
      return goal
