import numpy as np
class backspacex:
   def __init__(self, userName, clrDictionary, maxStepSize, maxTime):
      self.name = userName # your object will be given a user name, i.e. your group name
   def run(self, img, info):
      loc, game_point = info[self.name]
      y,x = loc # get current y,x coordinates
      a=0
      colorpoint=0
      rang=50
      i=0
      goal=[[y,x+1],[y+1,x+1]]
      if all(img[y,x]==[255,255,255]):
          pass
      elif all(img[y,x]==[1,1,1]):
          pass
      elif all(img[y,x]==[225,1,1]):
          game_point=game_point-100
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[1,255,1]):
          game_point=game_point-50
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[1,1,255]):
          game_point=game_point-30
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[200,200,1]):
          game_point=game_point-20
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[255,1,255]):
          game_point=game_point-10
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[1,255,255]):
          game_point=game_point-9
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[1,1,150]):
          game_point=game_point-8
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[120,120,40]):
          game_point=game_point-7
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[150,1,150]):
          game_point=game_point-6
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[1,150,150]):
          game_point=game_point-5
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[222,55,222]):
          game_point=game_point-4
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[1,99,55]):
          game_point=game_point-3
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[200,100,10]):
          game_point=game_point-2
          if game_point==0:
              return [[y,x],[y,x]]
      elif all(img[y,x]==[100,10,200]):
          game_point=game_point-1
          if game_point==0:
              return [[y,x],[y,x]]
      while i<13:
         i=i+1
         
         if i==1:
            if y-rang<0 or x-rang<0:
               continue
            if all(img[y-rang,x-rang]==[255,255,255]):
               colorpoint=0
            elif all(img[y-rang,x-rang]==[1,1,1]):
               colorpoint=0            
            elif all(img[y-rang,x-rang]==[225,1,1]):
               colorpoint=100
               a=100
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
            elif all(img[y-rang,x-1]==[1,1,1]):
               colorpoint=0            
            elif all(img[y-rang,x-1]==[225,1,1]):
               colorpoint=100
               a=100
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
            if x+rang>=750 or y-rang<0:
               continue
            if all(img[y-rang,x+rang]==[255,255,255]):
               colorpoint=0
            elif all(img[y-rang,x+rang]==[1,1,1]):
               colorpoint=0               
            elif all(img[y-rang,x+rang]==[225,1,1]):
               colorpoint=100
               a=100
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
               if x+rang>=750:
                  continue
               if all(img[y,x+rang]==[255,255,255]):
                  colorpoint=0
               elif all(img[y,x+rang]==[1,1,1]):
                  colorpoint=0            
               elif all(img[y,x+rang]==[225,1,1]):
                  colorpoint=100
                  a=100
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
               if (x+rang>=750) or (y+rang>=750):
                  continue
               if all(img[y+rang,x+rang]==[255,255,255]):
                  colorpoint=0
               elif all(img[y+rang,x+rang]==[1,1,1]):
                  colorpoint=0
               elif all(img[y+rang,x+rang]==[225,1,1]):
                  colorpoint=100
                  a=100
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
            if y+rang>=750:
               continue
            if all(img[y+rang,x]==[255,255,255]):
               colorpoint=0
            elif all(img[y+rang,x]==[1,1,1]):
               colorpoint=0            
            elif all(img[y+rang,x]==[225,1,1]):
               colorpoint=100
               a=100
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
            if y+rang>=750 or x-rang<0:
               continue
            if all(img[y+rang,x-rang]==[255,255,255]):
               colorpoint=0
            elif all(img[y+rang,x-rang]==[1,1,1]):
               colorpoint=0            
            elif all(img[y+rang,x-rang]==[225,1,1]):
               colorpoint=100
               a=100
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
            elif all(img[y,x-rang]==[1,1,1]):
               colorpoint=0            
            elif all(img[y,x-rang]==[225,1,1]):
               colorpoint=100
               a=100
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
            if y-rang-50<0:
               continue
            if all(img[y-rang-50,x]==[255,255,255]):
               colorpoint=0
            elif all(img[y-rang-50,x]==[1,1,1]):
               colorpoint=0            
            elif all(img[y-rang-50,x]==[225,1,1]):
               colorpoint=100
               a=100
               goal=[[y,x-1],[y-rang-50,x-1]]
               break
               
            elif all(img[y-rang-50,x]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
            
            elif all(img[y-rang-50,x]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
              
            elif all(img[y-rang-50,x]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
             
            elif all(img[y-rang-50,x]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
            
            elif all(img[y-rang-50,x]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
            
            elif all(img[y-rang-50,x]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
                  
            elif all(img[y-rang-50,x]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
            
            elif all(img[y-rang-50,x]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
                  
            elif all(img[y-rang-50,x]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
                  
            elif all(img[y-rang-50,x]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
            
            elif all(img[y-rang-50,x]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
            
            elif all(img[y-rang-50,x]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
            
            elif all(img[y-rang-50,x]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y-rang-50,x-1]]
            
         elif i==10:
            if x+rang+50>=750:
               continue
            if all(img[y,x+rang+50]==[255,255,255]):
               colorpoint=0
            elif all(img[y,x+rang+50]==[1,1,1]):
               colorpoint=0            
            elif all(img[y,x+rang+50]==[225,1,1]):
               colorpoint=100
               a=100
               goal=[[y,x+rang+50],[y+1,x+rang+50]]
               break
               
            elif all(img[y,x+rang+50]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
            
            elif all(img[y,x+rang+50]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
              
            elif all(img[y,x+rang+50]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
             
            elif all(img[y,x+rang+50]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
            
            elif all(img[y,x+rang+50]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
            
            elif all(img[y,x+rang+50]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
                  
            elif all(img[y,x+rang+50]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
            
            elif all(img[y,x+rang+50]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
                  
            elif all(img[y,x+rang+50]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
                  
            elif all(img[y,x+rang+50]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
            
            elif all(img[y,x+rang+50]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
            
            elif all(img[y,x+rang+50]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
            
            elif all(img[y,x+rang+50]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x+rang+50],[y+1,x+rang+50]]
            
         elif i==11:
            if y+rang+50>=750:
               continue
            if all(img[y+rang+50,x]==[255,255,255]):
               colorpoint=0
            elif all(img[y+rang+50,x]==[1,1,1]):
               colorpoint=0            
            elif all(img[y+rang+50,x]==[225,1,1]):
               colorpoint=100
               a=100
               goal=[[y,x-1],[y+rang+50,x-1]]
               break
               
            elif all(img[y+rang+50,x]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
            
            elif all(img[y+rang+50,x]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
              
            elif all(img[y+rang+50,x]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
             
            elif all(img[y+rang+50,x]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
            
            elif all(img[y+rang+50,x]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
            
            elif all(img[y+rang+50,x]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
                  
            elif all(img[y+rang+50,x]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
            
            elif all(img[y+rang+50,x]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
                  
            elif all(img[y+rang+50,x]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
                  
            elif all(img[y+rang+50,x]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
            
            elif all(img[y+rang+50,x]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
            
            elif all(img[y+rang+50,x]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
            
            elif all(img[y+rang+50,x]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-1],[y+rang+50,x-1]]
            
         elif i==12:
            if x-rang-50<0:
               continue
            if all(img[y,x-rang-50]==[255,255,255]):
               colorpoint=0
            elif all(img[y,x-rang-50]==[1,1,1]):
               colorpoint=0            
            elif all(img[y,x-rang-50]==[225,1,1]):
               colorpoint=100
               a=100
               goal=[[y,x-rang-50],[y-1,x-rang-50]]
               break
               
            elif all(img[y,x-rang-50]==[1,255,1]):
               colorpoint=50
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
            
            elif all(img[y,x-rang-50]==[1,1,255]):
               colorpoint=30
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
              
            elif all(img[y,x-rang-50]==[200,200,1]):
               colorpoint=20
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
             
            elif all(img[y,x-rang-50]==[255,1,255]):
               colorpoint=10
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
            
            elif all(img[y,x-rang-50]==[1,255,255]):
               colorpoint=9
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
            
            elif all(img[y,x-rang-50]==[1,1,150]):
               colorpoint=8
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
                  
            elif all(img[y,x-rang-50]==[120,120,40]):
               colorpoint=7
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
            
            elif all(img[y,x-rang-50]==[150,1,150]):
               colorpoint=6
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
                  
            elif all(img[y,x-rang-50]==[1,150,150]):
               colorpoint=5
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
                  
            elif all(img[y,x-rang-50]==[222,55,222]):
               colorpoint=4
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
            
            elif all(img[y,x-rang-50]==[1,99,55]):
               colorpoint=3
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
            
            elif all(img[y,x-rang-50]==[200,100,10]):
               colorpoint=2
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
            
            elif all(img[y,x-rang-50]==[100,10,200]):
               colorpoint=1
               if colorpoint>a:
                  a=colorpoint
                  goal=[[y,x-rang-50],[y-1,x-rang-50]]
           
         if a==0 and i==13:
            i=0
            rang=rang+50
         if rang >= 700:
            break
      check=1
      if (game_point-a)<0:
         colorpoint = 0
         renkler=(((1,1,1), 0),((225, 1, 1), 100),((1, 255, 1), 50),((1, 1, 255), 30),((200, 200, 1), 20),((255, 1, 255), 10),((1, 255, 255), 9),((1,1,150), 8),((120,120,40), 7),((150,1,150), 6),((1,150,150), 5),((222,55,222), 4),((1, 99, 55), 3),((200, 100, 10),2),((100, 10, 200),1))
         a=0
         kisa_islemler1 = [0,50,-50,100,-100]
         goal=0
         if rang<700 :
            for sayi1 in kisa_islemler1:
               if y+sayi1<50 or y+sayi1>700 : continue
               for sayi2 in kisa_islemler1:
                  if x+sayi2<50 or x+sayi2>700 : continue
                  if sayi1==0 and sayi2==0 : continue
                  if sayi1==100 and sayi2==100 : continue
                  if sayi1==100 and sayi2==-100 : continue
                  if sayi1==-100 and sayi2==100 : continue
                  if sayi1==-100 and sayi2==-100 : continue
                  if sayi1==100 and sayi2==50 : continue
                  if sayi1==100 and sayi2==-50 : continue
                  if sayi1==50 and sayi2==100 : continue
                  if sayi1==50 and sayi2==-100 : continue
                  if sayi1==-100 and sayi2==50 : continue
                  if sayi1==-100 and sayi2==-50 : continue
                  if sayi1==-50 and sayi2==100 : continue
                  if sayi1==-50 and sayi2==-100 : continue
                  if all(img[y+sayi1, x+sayi2] == [255,255,255]):continue
                  if all(img[y+sayi1, x+sayi2] == [1,1,1]):continue
                  for i in range(len(renkler)):
                     if (tuple(img[y+sayi1, x+sayi2]) == renkler[i][0]):
                        colorpoint=renkler[i][1]
                        if colorpoint>a and colorpoint<=game_point:
                           a=colorpoint
                           goal=[[y+sayi1, x],[y+sayi1,x+sayi2]]
                        break
         if goal==0:
            check=0
      if rang>=700 or check==0 :
         kisa_islemler1 = [0,50,-50,100,-100]
         chaos=[]
         for sayi1 in kisa_islemler1:
            if y+sayi1<50 or y+sayi1>700 : continue
            for sayi2 in kisa_islemler1:
               if x+sayi2<50 or x+sayi2>700 : continue
               if sayi1==0 and sayi2==0 : continue
               if sayi1==100 and sayi2==100 : continue
               if sayi1==100 and sayi2==-100 : continue
               if sayi1==-100 and sayi2==100 : continue
               if sayi1==-100 and sayi2==-100 : continue
               if sayi1==100 and sayi2==50 : continue
               if sayi1==100 and sayi2==-50 : continue
               if sayi1==50 and sayi2==100 : continue
               if sayi1==50 and sayi2==-100 : continue
               if sayi1==-100 and sayi2==50 : continue
               if sayi1==-100 and sayi2==-50 : continue
               if sayi1==-50 and sayi2==100 : continue
               if sayi1==-50 and sayi2==-100 : continue
               if all(img[y+sayi1, x+sayi2] == [255,255,255]):continue
               if all(img[y+sayi1, x+sayi2] == [1,1,1]):
                  chaos.append([[y+sayi1, x],[y+sayi1,x+sayi2]])
               elif all(img[y+sayi1, x+sayi2]== [0,0,0]):
                  chaos.append([[y+sayi1, x],[y+sayi1,x+sayi2]])
         len_chaos=len(chaos)  
         if len_chaos!=0:
            goal=chaos[np.random.randint(len_chaos)]
         else:
            c=np.random.randint(4)
            if c==0:
               if all(img[y+50,x]==[255,255,255]):
                  goal=[[y,x+1],[y+50,x+1]]
               elif all(img[y+50,x]==[1,1,1]):
                  goal=[[y,x+1],[y+50,x+1]]
               elif all(img[y+50,x]==[0,0,0]):
                  goal=[[y,x+1],[y+50,x+1]]
               else:
                  goal=[[y,x+50],[y+1,x+50]]
            
            elif c==1:
               if all(img[y-50,x]==[255,255,255]):
                  goal=[[y,x+1],[y-50,x+1]]
               elif all(img[y-50,x]==[1,1,1]):
                  goal=[[y,x+1],[y-50,x+1]]
               elif all(img[y-50,x]==[0,0,0]):
                  goal=[[y,x+1],[y-50,x+1]]
               else:
                  goal=[[y,x-50],[y+1,x-50]]
            
            elif c==2:
               if all(img[y,x-50]==[255,255,255]):
                  goal=[[y,x-50],[y+1,x-50]]
               elif all(img[y,x-50]==[1,1,1]):
                  goal=[[y,x-50],[y+1,x-50]]
               elif all(img[y,x-50]==[0,0,0]):
                  goal=[[y,x-50],[y+1,x-50]]
               else:
                  goal=[[y,x+1],[y+50,x+1]]
               
            elif c==3:
               if all(img[y,x+50]==[255,255,255]):
                  goal=[[y,x+50],[y+1,x+50]]
               elif all(img[y,x+50]==[1,1,1]):
                  goal=[[y,x+50],[y+1,x+50]]
               elif all(img[y,x+50]==[0,0,0]):
                  goal=[[y,x+50],[y+1,x+50]]
               else:
                  goal=[[y,x+1],[y-50,x+1]]
               
      return goal
