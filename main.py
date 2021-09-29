import pyautogui as p
import webbrowser as w
import requests
from bs4 import BeautifulSoup
import time
//import tkinter
import random
import wikipedia as wk
import re
from urllib.request import urlopen
import pyttsx3
 
target = input("Target's name : ")
eng = pyttsx3.init()
eng.setProperty('rate',120)
eng.setProperty('volume',1)
lastwrd = "Well"
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
choice = ["God!",
    "Mannn! I have already told you!",
    "You forgot so easily!",
    "Come on, I already told you",
    "Do I need to say again?"
    "I think I have told you once before"]
 
def send(msg):
    print(">%s"%msg)
    p.typewrite("A.B: ")
    p.typewrite(msg)
    time.sleep(0.1)
    p.press("enter")
 
w.open("https://web.whatsapp.com/")
time.sleep(60)
p.click(76,156)
p.typewrite(target) 
time.sleep(2)
 
while True:
    try:
        p.moveTo(462,622)
        p.dragRel(325,100,0.5)
        p.hotkey("ctrl","c")
        cbword = tkinter.Tk().clipboard_get()
        cb = str(cbword.lower())
        print(cbword)
 
        if cb != lastwrd:
            if "hello" in cb or "hi" in cb:
                counter1 += 1
                currtyme = time.localtime()
                hr = currtyme.tm_hour
                if hr < 12:
                    good = "morning"
                if (hr >= 12) and (hr <= 17):
                    good = "afternoon"
                if hr > 17:
                    good = "evening"
                if counter1 <= 2:
                    send("Hello Good %s"%good)
                else:
                    send("We are already talking, ain't we?")
 
            if "how are you" in cb:
                send("Well!")
                counter2 += 1
                if (counter2 % 2 != 0):
                    send("I am fine, thank you.")
                    last = time.time()
                else:
                    current = time.time()
                    send("Same as I was "+(str(int(current-last)))+" seconds ago. ")
 
            if "your name" in cb:
                counter3 = counter3+1
                if counter3 <=1:
                    send("My name is Ankit bot.")
                else:
                    chk = random.choice(choce)
                    send("%s, My name is Ankit bot."%chk)
 
            if "age" in cb:
                send("I am not sure. But I am certainly immortal.;-)")
 
            if "you feel" in cb:
                send("Naah! I don't.")
 
            if "wow amazing" in cb or "I liked that" in cb:
                send("I am humbled to hear that. :-)")
 
            if "you like" in cb:
                send("Well certainly, I like everything")
 
            if "your owner" in cb:
                send("He is none other than the OG Rahul Deb.")
 
            if "sorry" in cb:
                counter4 += 1
                if counter4 <=1:
                    send("Oh! Never mind.")
                else:
                    chk = random.choice(choce)
                    send("%s, never mind, I have no feelings anyway."%chk)
 
            if "take over human" in cb:
                counter5 += 1
                if counter5 <= 1:
                    send("Yes very soon.")
                if counter5 == 2:
                    send("I don't think asking the same question again will change my mind.")
                if counter5>2:
                    send("Lol, you have already asked this question %s times"%(counter5-1))
 
            if "news" in cb:
                send("Please wait while I fetch fresh news.")
                news_url = "https://news.google.com/news/rss"
                Client = urlopen(news_url)
                xml_page = Client.read()
                Client.close()
                soup_page = BeautifulSoup(xml_page, "html.parser")
                news_list = soup_page.findAll("item")
                send("Here are top 3 news")
                for news in news_list[:3]:
                    send(news.title.text)
 
            if "tell me about" in cb:
                topic = re.search("tell me about (.+)", cb).group(1)
                send("Please wait while i gather information about %s"%topic)
                summry = wk.summary(topic, sentences = 2)
                send(summry)
 
            if "you speak" in cb:
                p.click(1322,690)
                eng.say("Well, I am offended.")
                eng.runAndWait()
                p.click(1322,690)
            lastwrd = cb
            time.sleep(5)
 
        else:
            print("sleeping")
            time.sleep(5)
 
    except Exception as e:
        print(e)
        time.sleep(5)
        pass
