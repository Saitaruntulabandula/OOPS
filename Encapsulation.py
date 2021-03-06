# -*- coding: utf-8 -*-
"""Encapsulation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mqoYEQCr_dCOZ34cSyHf3EIeqE0T-kLV
"""

#mechanism of wrapping the data (variables) and code acting on the data(methods) together as a single unit. 
#In encapsulation, the variables of a class will be hidden from other classes.
#it is a protective shield that prevents the data from being accessed by the code outside this shield. 
#And can be accessed only through the methods of their current class. 
#Therefore, it is also known as data hiding

class Tarun:
    def __init__(self):
        self.a=45              #Public Variable
        self._b=60             #Private Variable Accessible outside the class
        self.__c=75            #Strictly Private Variable Not Accesible(Access with Name Mangling Method)
        
t=Tarun()
print(t.a)
print(t._b)
#t.__c
#t._Tarun__c                     #Name Mangling Method

class Sai:
  def __init__(self):
    self.__privatemethod()
  def __privatemethod(self):                 #Private Method.
    print('Private Method Gets Called')
  def Name(self):                            #Public Method.
    print('Sai')

s=Sai()
s.Name()
#s.__privatemethod()    #cant access outside the class

