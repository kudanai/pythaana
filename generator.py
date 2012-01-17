# -*- encoding: utf-8 -*-
#!/usr/bin/env python

# -----------------------------------------------
# A simple helper script which generates a sequence map
# generated string of thaana text for testing purposes,
# based off a demostration in the pyQuick google training
# videos.
# 
# This is part of the pyThaana library.
#
# 2011 - Naail Abdul Rahman
# ------------------------------------------------

from random import choice
import pickle
import conversions

class ThaanaGenerator():
    def __init__(self):
        self.resourceFileRef='genMapSource'
        self.mapJar='genPatterns'
    

    
    def generateLipsumAscii(self,limit):
        """
            generate a random string consisting of
            limit words.
        """
        with open(self.mapJar,"r") as f:        # we're loading a pickled dictionary map
            mimicMap = pickle.load(f)
        
        word = choice(mimicMap.keys())
        spam=''
        count = 0
        
        while count <= limit:
            spam = spam + ' ' + word
            next_words = mimicMap.get(word)
            if next_words == None or len(next_words) == 0:
                next_words = mimicMap['']
            word = choice(next_words)
            count += 1
            
        return spam.strip()


  
    
    def generateLipsumUtf8(self,limit):
        """
            shall return a utf8 string of the generated string.
        """
        converter = conversions.ThaanaConversions()
        return converter.ConvertAsciiToUtf8(self.generateLipsumAscii(limit))
    
 
 
    
    def makeMap(self):
        try:
            with open(self.resourceFileRef,"r") as f:
                wordlist = f.read().split()
        except IOError:
            return
            
        dict_map = {}
        prev_word = ''
        
        for word in wordlist:
            next_words = dict_map.get(prev_word)
            if not next_words:
                next_words=[]
                dict_map[prev_word] = next_words
                
            next_words.append(word)
            prev_word=word
        
        #and just for good measure
        dict_map[''] = wordlist
        
        with open(self.mapJar,"w") as f:    
            pickle.dump(dict_map,f)
    
    
if __name__ == "__main__":
    g = ThaanaGenerator()
    print g.generateLipsumUtf8(100)
    #g.makeMap()                 # if we run from the command line, lets
                                # assume we're trying to rebuild the map
                                # but it should actually run a generate I guess
    