from flask import Flask, request, render_template, redirect, url_for, Response
from sqlalchemy import create_engine
import pandas as pd
import time

# connect to SQL server
SERVER = ''
DATABASE = ''
DRIVER = ''
USERNAME = ''
PASSWORD = ''
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'

engine = create_engine(DATABASE_CONNECTION)
connection = engine.raw_connection()
cursor = connection.cursor()

# create flask app
app = Flask(__name__)
# app.static_folder = 'static'

@app.route("/")
# define homepage
def home_page():
    return render_template("index.html")

@app.route("/database", methods=["POST", "GET"])
# define export page
def database():
    sample_name = request.form.get("sample_name")
    print(sample_name) 
    cursor = connection.cursor()
    #cursor.execute(f"SELECT Label, DataFloat, DataInt, DataText, SpecimenId, SampleId, Name FROM Complete_Dataset WHERE Name = {sample_name}")
    cursor.execute("SELECT Label, DataFloat, DataInt, DataText, SpecimenId, SampleId, Name FROM Complete_Dataset")
    data = cursor.fetchall()
    cursor.close()
    return render_template("database.html", samples = data)

@app.route("/import")
#define import page
def importing():
    return render_template("import.html")

# run flask app
if __name__ == "__main__":
    app.run(debug=True)
