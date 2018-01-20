#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:37:50 2017

@author: mayank
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob
import re
import json

# ckey= 
# csecret=  
# atoken= 
# asecret= 
auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

global positive
global negative
global overall 

class listener(StreamListener):
    
    def on_status(self, status):
       
        if status.text.startswith('RT'):
            return True
        else: 
            text= status.text.encode("utf-8")
            print(text)
            text=" ".join(re.findall("[a-zA-Z]+", text))
            blob= TextBlob(text)
    
            global positive
            global negative
            global overall 
            
            senti=0
            for sen in blob.sentences:
                senti+=sen.sentiment.polarity
            print(senti)
            
            if senti>0 :
                positive+= senti
            else:
                negative+= senti
            
            overall+= senti
            
            print(positive)
            print(negative)
                    
            data={ 'Text': status.text , 'Sentiments': senti}
            with open('Tweets.txt',mode='a') as f:
                json.dump(data, f)
            return True
          
    def on_error(self, status_code):
        if status_code == 420:
            return False

twitterStream=  Stream(auth, listener())
twitterStream.filter(track=["SurvivorSeries"])