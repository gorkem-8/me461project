import numpy as np
import time
class backspacex:
    def __init__(self, userName, clrDictionary, maxStepSize, maxTime):
        self.name = userName # your object will be given a user name, i.e. your group name
        self.maxStep = maxStepSize # maximum length of the returned path from run()
        self.maxTime = maxTime # run() is supposed to return before maxTime
                                                                                                                                                                                                                
    def run(self, img, info):
        myinfo = info[self.name]

        #komsu renklerin puanlarini bul
        for tup in clrDictionary : #.values()
          try:
            if tuple(img[myinfo[0][0]+50,myinfo[0][1]]) in tup : puan1 = tup[1]
          except : pass
          try:
            if tuple(img[[myinfo[0][0], myinfo[0][1]+50]]) in tup : puan2 = tup[1]
          except : pass
          try:
            if tuple(img[myinfo[0][0]-50, myinfo[0][1]]) in tup : puan3 = tup[1]
          except : pass
          try:
            if tuple(img[myinfo[0][0], myinfo[0][1]-50]) in tup : puan4 = tup[1]
          except : pass
          try:
            if tuple(img[myinfo[0][0]+50,myinfo[0][1]+50]) in tup : puan5 = tup[1]
          except : pass
          try:
            if tuple(img[myinfo[0][0]-50,myinfo[0][1]-50]) in tup : puan6 = tup[1]
          except : pass
          try:
            if tuple(img[myinfo[0][0]+50,myinfo[0][1]-50]) in tup : puan7 = tup[1]
          except : pass
          try:
            if tuple(img[myinfo[0][0]-50,myinfo[0][1]+50]) in tup : puan8 = tup[1]
          except : pass
          try:
            if tuple(img[myinfo[0][0]+100,myinfo[0][1]]) in tup : puan9 = tup[1]
          except : pass
          try:
            if tuple(img[myinfo[0][0],myinfo[0][1]+100]) in tup : puan10 = tup[1]
          except : pass
          try:
            if tuple(img[myinfo[0][0]-100,myinfo[0][1]]) in tup : puan11 = tup[1]
          except : pass
          try:
            if tuple(img[myinfo[0][0],myinfo[0][1]-100]) in tup : puan12 = tup[1]
          except : pass

        #hedef noktasini bul ve oraya git  
        hedef = max(puan1,puan2,puan3,puan4,puan5,puan6,puan7,puan8,puan9,puan10,puan11,puan12)
        print(hedef)
        if hedef == puan1: 
            return  [ [ myinfo[0][0]+50 , myinfo[0][1] ] , [ myinfo[0][0]+50 , myinfo[0][1]+1 ] ]
        
        if hedef == puan2:
            return  [ [ myinfo[0][0] , myinfo[0][1]+50 ] , [ myinfo[0][0]+1 , myinfo[0][1]+50 ] ]
        
        if hedef == puan3: 
            return  [ [ myinfo[0][0]-50 , myinfo[0][1] ] , [ myinfo[0][0]-50 , myinfo[0][1]+1 ] ]
        
        if hedef == puan4:
            return  [ [ myinfo[0][0] , myinfo[0][1]-50 ] , [ myinfo[0][0]+1 , myinfo[0][1]-50 ] ]
        
        if hedef == puan5: 
            return  [ [ myinfo[0][0]+50 , myinfo[0][1] ] , [ myinfo[0][0]+50 , myinfo[0][1]+50 ]  ]
        
        if hedef == puan6:
            return  [ [ myinfo[0][0]-50 , myinfo[0][1] ] , [ myinfo[0][0]-50 , myinfo[0][1]-50 ] ]
        
        if hedef == puan7: 
            return  [ [ myinfo[0][0]+50 , myinfo[0][1] ] , [ myinfo[0][0]+50 , myinfo[0][1]-50 ]  ]
        
        if hedef == puan8:
            return  [ [ myinfo[0][0]-50 , myinfo[0][1] ] , [ myinfo[0][0]-50 , myinfo[0][1]+50 ]  ]
        
        if hedef == puan9:
            return  [ [ myinfo[0][0]+100 , myinfo[0][1] ] , [ myinfo[0][0]+100 , myinfo[0][1]+1 ] ]
        
        if hedef == puan10:
            return  [ [ myinfo[0][0] , myinfo[0][1]+100 ] , [ myinfo[0][0]+1 , myinfo[0][1]+100 ] ]
        
        if hedef == puan11:
            return  [ [ myinfo[0][0]-100 , myinfo[0][1] ] , [ myinfo[0][0]-100 , myinfo[0][1]+1 ] ]
        
        if hedef == puan12:
            return  [ [ myinfo[0][0] , myinfo[0][1]-100 ] , [ myinfo[0][0]+1 , myinfo[0][1]-100 ] ]
        
        else : 
            return  [ [ myinfo[0][0]+50 , myinfo[0][1] ] , [ myinfo[0][0]+50 , myinfo[0][1]+50 ] ]
