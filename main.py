from flask import Flask, redirect, url_for, render_template
from youtubesearchpython import SearchVideos
import requests
import lxml
import json

app = Flask(__name__,template_folder='templates')

@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/<variable>')
def daily(variable):
    youtubeUrl = "https://www.youtube.com/results?search_query="+variable 
    search = SearchVideos(variable,offset=1,mode="json",max_results=1)
    y = json.loads(search.result())
    link = y['search_result'][0]['link']
    print(link)
    return redirect(link)

    