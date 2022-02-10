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
      
      for i in range(1,9):
         if i==1:
            pass
            #goal=[[y,x-50],[y-50,x-50]]
         elif i==2:
            if any(img[y-50,x-1]==[225,1,1]):
               goal=[[y,x-1],[y-50,x-1]]
         #elif i==3:
            #goal=[[y,x+50],[y-50,x+50]]
         elif i==4:
            if any(img[y,x+50]==[225,1,1]):
               goal=[[y,x+50],[y+1,x+50]]
         #elif i==5:
            #goal=[[y,x+50],[y+50,x+50]]
         elif i==6:
            if any(img[y+50,x-1]==[225,1,1]):
               goal=[[y,x-1],[y+50,x-1]]
         #elif i==7:
            #goal=[[y,x-50],[y+50,x-50]]
         elif i==8:
            if any(img[y,x-50]==[225,1,1]):
               goal=[[y,x-50],[y+1,x-50]]   
      return goal
