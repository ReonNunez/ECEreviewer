import bs4 as bs
import lxml
import random
import os

def ACCircuits():
    with open("Electronics/ACCircuits.XML", "r") as file:
        # Read each line in the file, readlines() returns a list of lines
        content = file.readlines()
        # Combine the lines in the list into a string
        content = "".join(content)
        bs_content = bs.BeautifulSoup(content, "lxml")
    questionbank = bs_content.find_all("challenge")
    return questionbank

def DCCircuits():
    with open("Electronics/DCCircuits.XML", "r") as file:
        # Read each line in the file, readlines() returns a list of lines
        content = file.readlines()
        # Combine the lines in the list into a string
        content = "".join(content)
        bs_content = bs.BeautifulSoup(content, "lxml")
    questionbank = bs_content.find_all("challenge")
    return questionbank

def SolidState():
    with open("Electronics/SolidStates.XML", "r") as file:
        # Read each line in the file, readlines() returns a list of lines
        content = file.readlines()
        # Combine the lines in the list into a string
        content = "".join(content)
        bs_content = bs.BeautifulSoup(content, "lxml")
    questionbank = bs_content.find_all("challenge")
    return questionbank

def Amplifiers():
    with open("Electronics/Op-amp and Mulltivibrator.xml", "r") as file:
        # Read each line in the file, readlines() returns a list of lines
        content = file.readlines()
        # Combine the lines in the list into a string
        content = "".join(content)
        bs_content = bs.BeautifulSoup(content, "lxml")
    with open("Electronics/op-amp II.xml", "r") as file:
        # Read each line in the file, readlines() returns a list of lines
        content = file.readlines()
        # Combine the lines in the list into a string
        content = "".join(content)
        bs_content2 = bs.BeautifulSoup(content, "lxml")
    questionbank = bs_content.find_all("challenge")
    questionbank.append(bs_content2.find_all("challenge"))
    print(questionbank)
    return questionbank