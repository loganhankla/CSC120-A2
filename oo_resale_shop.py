"""
   Filename: oo_resale_shop.py
Description: An OOP approach to creating the Resale Shop class for A2 in CSC 120.
     Author: Logan Hankla (@loganhankla)
       Date: 7 February 2023
"""
from computer import *

class ResaleShop:

    # What attributes will it need?
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        pass # You'll remove this when you fill out your constructor
        self.inventory = []
    # What methods will you need?
        ## buy
    def buy(self, c:Computer):
        self.inventory.append(c)
        ## sell
   # def sell(self, c:Computer):
   #     self.inventory.remove(c)
        # update OS
   # def update_OS(self, c:Computer):

        # update price
        
        # print errors