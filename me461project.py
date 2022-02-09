'''
Greedy code
1-recognize color red and your location
2-write an algortyhm to go only red
3-implement other colors
'''

import numpy as np
import time
class backspacex:
    '''
    This is the random player used in the colab example.
    Edit this file properly to turn it into your submission or generate a similar file that has the same minimal class structure.
    You have to replace the name of the class (ME461Group) with one of the following (exactly as given below) to match your group name
        atlas
        backspacex
        ducati
        hepsi1
        mechrix
        meturoam
        nebula
        ohmygroup
        tulumba
    After you edit this class, save it as groupname.py where groupname again is exactly one of the above
    '''
    def __init__(self, userName, clrDictionary, maxStepSize, maxTime):
        self.name = userName # your object will be given a user name, i.e. your group name
        self.maxStep = maxStepSize # maximum length of the returned path from run()
        self.maxTime = maxTime # run() is supposed to return before maxTime

  
    def run(self, img, info):
        myinfo = info[self.name]
        Y,X = np.where(np.all(img==[225,1,1],axis=2))
        Y,X=[round((Y[0]+Y[-1])/2),round((X[0]+X[-1])/2)]
        # get current location 
        loc, game_point = info[self.name]
        y,x = loc # get current y,x coordinates
        # a very simple randomizer
        nx=X
        ny=Y
        nx2=X        
        return [[y,nx],[ny,nx]]

