"""
   Filename: oo_resale_shop.py
Description: An OOP approach to creating the Resale Shop class for A2 in CSC 120.
     Author: Logan Hankla (@loganhankla)
       Date: 7 February 2023
"""
from computer import *

class ResaleShop:
    """This class represents a given Resale Shop that can buy, sell, and refurbish computers."""
    # What attributes will it need?
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
    # What methods will you need?
    
    def buy(self, c:Computer):
        self.inventory.append(c)
       
    def sell(self, c:Computer):
        # check if in inventory
        if c in self.inventory:
            self.inventory.remove(c)
        else:    
            print("Sorry, computer not found in store inventory.")
        
    def refurbish(self, c:Computer):
        #update OS
        c.operating_system = "LatestOS" 
        # update price
        c.price = c.price + 300 

    def getInventory(self):
        print("Inventory with details:")
        for c in self.inventory:
            c.printDetails() 


def main():
    # testing methods
    c = Computer("Desktop", "M1", 64, 68, "Cool OS", 2018, 2500)
    c1 = Computer("My Desktop", "M2", 100, 68, "Older OS", 2010, 2000)
    print("First bought computer:", c)
    store = ResaleShop()
    store.buy(c)
    store.refurbish(c)
    store.buy(c1)
    store.refurbish(c1)
    c1.printDetails()
    print("Full Inventory:", store.inventory)
    store.getInventory()
    store.sell(c)
    store.getInventory()

main()

