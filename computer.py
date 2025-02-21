"""
   Filename: computer.py
Description: An OOP approach to creating the computer class for A2 in CSC 120.
     Author: Logan Hankla (@loganhankla)
       Date: 7 February 2023
"""

class Computer:
    """This class represents the type Computer that stores all the information about a given computer."""
    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, descrip:str, procType:str, HDCap:int, mem:int, OS:str, year:int, price:int):
        self.description = descrip
        self.processor_type = procType
        self.hard_drive_capacity = HDCap
        self.memory = mem
        self.operating_system = OS
        self.year_made = year
        self.price = price

        
    # What methods will you need?
    def printDetails(self):
        print(self.description + ",", self.processor_type + ",",  
        self.hard_drive_capacity, ",", self.memory, ",", self.operating_system +
        ",", self.year_made, ",", self.price)

def main():
    c = Computer("Desktop", "M1", 64, 68, "Cool OS", 2018, 2500)
    c.printDetails()

if __name__ == "__main__":
    main()