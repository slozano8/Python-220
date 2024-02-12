# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:23:33 2024

@author: Santo
"""

class Profile():
    
    def feet_to_meter(feet):
        meter = feet * 0.3048
        return meter
    
    
    def __init__(self, name, age, ethnicity, gender, height):
        self.name = name
        self._age = age
        self._ethnicity = ethnicity
        self._gender = gender
        self._height = height/Profile.feet_to_meter  # confert feet to meeter
        
    def get_name(self):
          return self.name
      
    def set_name(self):
          return self.name
        
    def get_age(self):
        return self._age
        
    def set_age(self):
        return self._age 
        
    def get_ethnicity(self):
        return self._ethnicity
    
    def set_ethnicity(self):
        return self._ethnicity 
    
    def get_gender(self):
        return self._gender
    
    def set_gender(self):
        return self._gender 
    
    def get_weight(self):
      return self._height 
      
    
    def __eq__(self, text):
        if isinstance(text, Profile):
           return self._height == text.get_height()
              
    
           
        return f"{self.get_name()} is {self.get_age()} from {self.get_ethnicity()}  + {self.get_height()}"
    
   
    
    if __name__=="__main__":
     pass