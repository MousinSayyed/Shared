from flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.mydatabase

collection = db['mycollection']
app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.now()
    day = now.strftime("%A")
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M %p")

    return render_template('index.html', day=day, date=date, time=time)

@app.route('/submit', methods=['GET','POST'])
def submit():
    form_data = dict(request.form)
    collection.insert_one(form_data)
    return form_data


if __name__ == '__main__':
   app.run(debug=True)

#comment