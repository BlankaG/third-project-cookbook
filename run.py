import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import database

app = Flask(__name__)

#app.config["MONGO_DBNAME"] = 'Recipes'
app.config["MONGO_URI"] = "mongodb+srv://blanka:blanka@cluster0.w783e.mongodb.net/Recipes?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("about.html", recipes=mongo.db.recipes.find())



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about") 
def about():
    return render_template("about.html")   


@app.route("/products") 
def products():
    return render_template("products.html")  


@app.route("/store") 
def store():
    return render_template("store.html")      


if __name__ == "__main__" :
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
