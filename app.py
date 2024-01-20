from flask import render_template, Flask
from bs4 import BeautifulSoup
import requests

app= Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():

       url="https://www.businesstoday.in/"

       req =requests.get(url)

       soup= BeautifulSoup(req.content,"html.parser")

       elem = soup.find_all("li",class_="lst_li",limit=6)
     
       finalnews = ""
       for data in elem:
         news =data.a["title"]
         finalnews+="\u2022 "+news+"\n"
       return render_template('index.html',News=finalnews) 
