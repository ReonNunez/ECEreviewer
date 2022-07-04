from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import kivy
import bs4 as bs
import lxml
import random
import xmlparser as xml
import os

def questionrandomizer(self):
    numq = 0
    for x in questionbank:
        numq = numq + 1
    questionnum = random.randrange(0,numq)
    questions = questionbank[questionnum]
    answer = questions.get("answer")
    answer = int(answer)
    choices1 = questions.find("option1").text
    choices2 = questions.find("option2").text
    choices3 = questions.find("option3").text
    choices4 = questions.find("option4").text
    question = questions.find("question").text
    return question, answer, choices1, choices2, choices3, choices4

class Menu(Screen):

    def loadquestions(self):
        self.manager.get_screen('electronicscategory')

class Quiz(Screen):
    
    def button1_action(self):
        global questionbank, x, gamevar
        y=1
        if gamevar[1] != y:
            wrongadd = int(self.wrongLabel.text)
            wrongadd = wrongadd + 1
            self.wrongLabel.text = str(wrongadd)
        if gamevar[1] == y:
            scoreadd = int(self.sccoreLabel.text)
            scoreadd = scoreadd + 1
            self.sccoreLabel.text = str(scoreadd)

        if gamevar[1] == 1:
                self.correctLabel.text = "Previous Correct Answer: " + self.button1.text
        elif gamevar[1] == 2 :
                self.correctLabel.text = "Previous Correct Answer: " + self.button2.text
        elif gamevar[1] == 3 :
                self.correctLabel.text = "Previous Correct Answer: " + self.button3.text
        else:
                self.correctLabel.text = "Previous Correct Answer: " + self.button4.text

        gamevar = questionrandomizer(self)
        self.questionLabel.text = str(gamevar[0])
        self.button1.text = str(gamevar[2])
        self.button2.text = str(gamevar[3])
        self.button3.text = str(gamevar[4])
        self.button4.text = str(gamevar[5])

        print("Confirmed")

    def button2_action(self):
        global gamevar, questionbank, x
        y=2
        if gamevar[1] != y:
            wrongadd = int(self.wrongLabel.text)
            wrongadd = wrongadd + 1
            self.wrongLabel.text = str(wrongadd)
        if gamevar[1] == y:
            scoreadd = int(self.sccoreLabel.text)
            scoreadd = scoreadd + 1
            self.sccoreLabel.text = str(scoreadd)

        if gamevar[1] == 1:
                self.correctLabel.text = "Previous Correct Answer: " + self.button1.text
        elif gamevar[1] == 2 :
                self.correctLabel.text = "Previous Correct Answer: " + self.button2.text
        elif gamevar[1] == 3 :
                self.correctLabel.text = "Previous Correct Answer: " + self.button3.text
        else:
                self.correctLabel.text = "Previous Correct Answer: " + self.button4.text

        gamevar = questionrandomizer(self)
        self.questionLabel.text = str(gamevar[0])
        self.button1.text = str(gamevar[2])
        self.button2.text = str(gamevar[3])
        self.button3.text = str(gamevar[4])
        self.button4.text = str(gamevar[5])

        print("Confirmed")

    def button3_action(self):
        global gamevar, questionbank, x
        y=3
        if gamevar[1] != y:
            wrongadd = int(self.wrongLabel.text)
            wrongadd = wrongadd + 1
            self.wrongLabel.text = str(wrongadd)
        if gamevar[1] == y:
            scoreadd = int(self.sccoreLabel.text)
            scoreadd = scoreadd + 1
            self.sccoreLabel.text = str(scoreadd)

        if gamevar[1] == 1:
                self.correctLabel.text = "Previous Correct Answer: " + self.button1.text
        elif gamevar[1] == 2 :
                self.correctLabel.text = "Previous Correct Answer: " + self.button2.text
        elif gamevar[1] == 3 :
                self.correctLabel.text = "Previous Correct Answer: " + self.button3.text
        else:
                self.correctLabel.text = "Previous Correct Answer: " + self.button4.text

        gamevar = questionrandomizer(self)
        self.questionLabel.text = str(gamevar[0])
        self.button1.text = str(gamevar[2])
        self.button2.text = str(gamevar[3])
        self.button3.text = str(gamevar[4])
        self.button4.text = str(gamevar[5])

        print("Confirmed")
    
    def button4_action(self):
        global gamevar, questionbank, x
        y=4
        if gamevar[1] != y:
            wrongadd = int(self.wrongLabel.text)
            wrongadd = wrongadd + 1
            self.wrongLabel.text = str(wrongadd)
        if gamevar[1] == y:
            scoreadd = int(self.sccoreLabel.text)
            scoreadd = scoreadd + 1
            self.sccoreLabel.text = str(scoreadd)

        if gamevar[1] == 1:
                self.correctLabel.text = "Previous Correct Answer: " + self.button1.text
        elif gamevar[1] == 2 :
                self.correctLabel.text = "Previous Correct Answer: " + self.button2.text
        elif gamevar[1] == 3 :
                self.correctLabel.text = "Previous Correct Answer: " + self.button3.text
        else:
                self.correctLabel.text = "Previous Correct Answer: " + self.button4.text

        gamevar = questionrandomizer(self)
        self.questionLabel.text = str(gamevar[0])
        self.button1.text = str(gamevar[2])
        self.button2.text = str(gamevar[3])
        self.button3.text = str(gamevar[4])
        self.button4.text = str(gamevar[5])

        print("Confirmed")
    
class ElectronicsCategory(Screen):
    def button_DCCircuits(self):
        global gamevar, x, questionbank
        questionbank = xml.DCCircuits()
        gamevar = questionrandomizer(self)
        self.manager.get_screen('quiz').questionLabel.text = str(gamevar[0])
        self.manager.get_screen('quiz').button1.text = str(gamevar[2])
        self.manager.get_screen('quiz').button2.text = str(gamevar[3])
        self.manager.get_screen('quiz').button3.text = str(gamevar[4])
        self.manager.get_screen('quiz').button4.text = str(gamevar[5])
        x=0
    def button_ACCircuits(self):
        global gamevar, x, questionbank
        questionbank = xml.ACCircuits()
        gamevar = questionrandomizer(self)
        self.manager.get_screen('quiz').questionLabel.text = str(gamevar[0])
        self.manager.get_screen('quiz').button1.text = str(gamevar[2])
        self.manager.get_screen('quiz').button2.text = str(gamevar[3])
        self.manager.get_screen('quiz').button3.text = str(gamevar[4])
        self.manager.get_screen('quiz').button4.text = str(gamevar[5])
        x=0
    def button_SolidState(self):
        global gamevar, x, questionbank
        questionbank = xml.SolidState()
        gamevar = questionrandomizer(self)
        self.manager.get_screen('quiz').questionLabel.text = str(gamevar[0])
        self.manager.get_screen('quiz').button1.text = str(gamevar[2])
        self.manager.get_screen('quiz').button2.text = str(gamevar[3])
        self.manager.get_screen('quiz').button3.text = str(gamevar[4])
        self.manager.get_screen('quiz').button4.text = str(gamevar[5])
        x=0
    def button_Amplifiers(self):
        global gamevar, x, questionbank
        questionbank = xml.Amplifiers()
        gamevar = questionrandomizer(self)
        self.manager.get_screen('quiz').questionLabel.text = str(gamevar[0])
        self.manager.get_screen('quiz').button1.text = str(gamevar[2])
        self.manager.get_screen('quiz').button2.text = str(gamevar[3])
        self.manager.get_screen('quiz').button3.text = str(gamevar[4])
        self.manager.get_screen('quiz').button4.text = str(gamevar[5])
        x=0
class CommunicationCategory(Screen):
    pass
class MathematicsCategory(Screen):
    pass
class GEASCategory(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("ece.kv")

class ECEApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    ECEApp().run()