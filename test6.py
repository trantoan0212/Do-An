import os
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser as wb
from time import strftime
import pyttsx3
import time
import re

wikipedia.set_lang('en')
language = 'en'

def speak(text):
    print("Trợ Lý Ảo :" + text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume - 0.0) 
    engine.setProperty('rate', rate - 50)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        print("Trợ Lý Ảo: ... I'm listening ...")
        audio = ear_robot.listen(source, phrase_time_limit=10)
        try:
            text = ear_robot.recognize_google(audio, language="en")
            print("Tôi: ", text)
            return text
        except:
            print("------Error!!!------")
            return 0
        

def stop():
    speak("Bye, see you again")

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("I can't hear you, try again!!") #tôi không thể nghe thấy bạn, vui lòng thử lại
    stop()
    return 0 


    

def welcome(name):
    time = int(strftime('%H'))
    if 5<= time <=11:
        speak(f"Good morning {name}")
    elif 12<= time <=18:
        speak(f"Good afternoon {name}")
    elif 18<= time <=24:
        speak(f"Good night {name}")
    
def stop():
    speak("Bye, see you again")
def get_time(text):
    now = datetime.datetime.now()
    if "time" in text:
        speak(f"It's {now.hour} Hour {now.minute} Minute {now.second} Second")

def get_day(text):
    today = datetime.datetime.now()
    if "today" in text:
        speak(f"Today is {today.day}/{today.month}/{today.year}")

def open_app(text):
    if "browser" in text:
        speak("Open Cốc Cốc")
        os.system(r"C:\Users\Administrator\AppData\Local\CocCoc\Browser\Application\browser.exe")
    elif "zalo" in text:
        speak("Open Zalo")
        os.system(r"C:\Users\Administrator\Desktop\Zalo.lnk")
    elif "unikey" in text:
        speak("Open Unikey")
        os.system(r"C:\Users\Administrator\Desktop\Unikey.lnk")
    elif "video" in text:
        video =(r"C:\Users\Administrator\Downloads\X2Convert.com son_tung_m_tp_muon_roi_ma_sao_con_official_music_video_-1374262026034213603.mp4")
        os.startfile(video)
        time.sleep(30)
    elif "the song" in text:
        song =(r"C:\Users\Administrator\Downloads\thang_dien_justatee_x_phuong_ly_official_mv_-5252447269763228750.mp3")
        os.startfile(song)
        time.sleep(30)
    else:
        speak("The app is not installed, please try again later") #ứng dụng chưa được cài đặt, vui lòng thử lại sau
def open_website(text):
    search = re.search('(.+)', text)
    if search:
        domain = reg_ex.group(1)
        url = "https://www." + domain
        wb.open(url)
        speak("The website you requested has been opened ") #trang web bạn yêu cầu đã được mở
        time.sleep(3)

def search_google(text):
    search_for = str(text).split("search", 1)[1]
    url = f"https://www.google.com/search?q={search_for}"
    wb.get().open(url)
    speak("This is the infomation need you find") #đây là thông tin bạn cần tìm
    time.sleep(3)

def search_google_2():
    speak("Say what you need to find on Google") #nói những gì bạn cần tìm trên google
    search = str(get_text()).lower()
    url = f"https://www.google.com/search?q={search}"
    wb.get().open(url)
    speak("This is the infomation need you find")  #Đây là thông tin bạn cần tìm
    time.sleep(3)

def search_youtube():
    speak("Say what you need to find on Youtube") ##nói những gì bạn cần tìm trên youtube
    search = str(get_text()).lower()
    url = f"https://www.youtube.com/search?q={search}"
    wb.get().open(url)
    speak("This is the infomation need you find") #Đây là thông tin bạn cần tìm
    time.sleep(3)

def music():
    speak("What song do you want to listen to?") 
    search = str(get_text()).lower()
    url = f"https://soundcloud.com/search?q={search}"
    wb.get().open(url)
    speak("This is the song you requested to be played on soundcloud")
    time.sleep(5)

def game():
    url = "https://vi.y8.com/"
    wb.get().open(url)
    speak("Game page you requested ")
    time.sleep(3)
def weather():
    url = "https://coccoc.com/search?query=th%E1%BB%9Di%20ti%E1%BA%BFt%20vinh%207%20ng%C3%A0y"
    wb.get().open(url)
    speak("Vinh city weather 7 days")
    time.sleep(3)
    



def main_brain():
    speak("Hello, what your name ?")
    name = get_text()
    if name:
        speak(f'Hello {name}')
        welcome(name)
        speak('How can I help you ?')
        while True:
            text = get_text()
            if not text:
                break
            elif ("thank" in text) or ("see you again" in text) or ("bye" in text):
                stop()
                break
            elif "time" in text:
                get_time(text)
            elif "today" in text:
                get_day(text)
            elif "youtube" in text:
                search_youtube()
            elif "google" in text:
                    search_google_2()
            elif "search" in text:
                search_google(text)
            elif "game" in text:
                game()
            elif "weather" in text:
                weather()
            elif "open" in text:    
                open_app(text)
            elif "music" in text:
                music()
            elif "." in text:
                open_website(text)
            elif "" in text:
                speak("Do you want me to search on google?")
                search = get_text()
                if ("yes" in search) or ("ok" in search) or ("yeah" in search):
                    wb.get().open(f"https://www.google.com/search?q={text}")
                    speak("Here are the results i found")
                    time.sleep(3)
                elif "no" in search:
                    speak("ok, How can I help you?")

            else:
                speak('Function not available, please try again') #chưcs năng chưa có, vui lòng thử lại

main_brain()

        

     