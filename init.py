from flask import Flask, flash, redirect, render_template, request, session, abort
import requests, json
app = Flask(__name__)

@app.route("/")
def GetCats():
    GetMeCats = requests.get("https://api.thecatapi.com/v1/images/search")
    CatsJson = GetMeCats.json()
    CatImage = CatsJson[0]["url"]
    return render_template('cats.html',cat_pic=CatImage)

if __name__ == "__main__":
    #TODO: Use environment variables for this!
    app.run(host='0.0.0.0', port=5000)