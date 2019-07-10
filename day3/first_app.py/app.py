from flask import Flask
import random
import requests
import bs4 
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/name")
def myname() :
    return "hello you!"

@app.route("/hello/<person>")
def hello2(person) : 
    #return "hello" + person
    return f"hello {person}"

#return 뒤에는 글자만 허용됨
#cube/2 ->8 cube/3 -> 27
@app.route("/cube/<num>")
def cube(num) : 
    result = int(num) **3 
    return str(result)

@app.route("/lotto")
def lotto() :
    numbers = random.sample(range(1,46),6)
    result = ""
    for i in numbers : 
        result += (str(i) + " ")
    
    #return str(sorted(random.sample(rnage(1,46),6)))
    return result


@app.route("/menu")
def menu() :
    menu = ["돼지국밥","순대볶음","피자", "떡"]
    return random.choice(menu)

@app.route("/kospi")
def kospi() : 
    url = "https://finance.naver.com/sise"
    response = requests.get(url).text
    document = bs4.BeautifulSoup(response, "html.parser")
    kospi = document.select_one("#KOSPI_now").text
    kosdaq = document.select_one("#KOSDAQ_now").text
    kospistr = f"Kospi : {kospi}"

    return kospistr

@app.route("/newyear")
def newyear() :
    #만약 오늘이 1.1
    month = datetime.now().month
    day = datetime.now().day
    
    if month == 1 and day == 1:
        print("안뇽")
        return "<h1>yes</h1>"
    else : 
        print("안뇽2")
        return "<h2>no<h2>"

@app.route("/index")
def index() : 
    return "<html><head></head><body><h1>홈페이지</h1><p>이건 내용</p></body></html>"