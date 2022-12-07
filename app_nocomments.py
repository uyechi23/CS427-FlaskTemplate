"""
Simple Flask Application

This Flask app was written for the CS427 course at the University of Portland.
This should be used as a very basic Flask app with minimal implementation. This app will
use and explain the various tools needed to build a Flask application that may be useful
in the projects for the CS427 class.

Additionally, read the Jinja2 documentation for making HTML documents. Jinja2 is useful
when writing HTML documents that have constantly changing data, such as reading data
from a database. An example of this is included in the Flask Demo

@Authors: Surj Patel, Jake Uyechi
@Date: December 6, 2022
"""

""" Importing Libraries """
from flask import Flask, render_template
import sqlite3

""" Initializing your Flask App """
app = Flask(__name__)

""" Routes """

# define a simple home route
@app.route('/')
def hello_world():
    return 'Hello World!'

# By default, Flask treats input parameters as strings
@app.route('/input/<value>')
def input(value):
    return f'The value passed to this URL is: {value}'

# data types can be specified for route parameters
@app.route('/integerinput/<int:data>')
def integerinput(data):
    return f'The integer input has a value of: {data}'

""" Interacting with a database """
@app.route('/addtodb/<string:name>/<int:value>')
def addtodb(name,value):
    # create a database connection/cursor
    con = sqlite3.connect('database.sqlite3')
    cur = con.cursor()
    
    # create a SQL query to create a database table
    query = """
        CREATE TABLE IF NOT EXISTS dummydata (
            id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            value INTEGER NOT NULL
        )
    """
    
    # execute the create table query
    cur.execute(query)
    
    # create another SQL query, but this time insert a row of data into the table
    query = """INSERT INTO dummydata (name, value) VALUES (?, ?)"""
    
    # execute the insert query
    cur.execute(query, (name, value))
    
    # commit to the database - this "saves" your changes
    con.commit()
    
    # create another SQL query to retrieve data from database
    query = """SELECT * FROM dummydata"""
    
    # execute the select query; fetchall() returns a list of the results
    res = cur.execute(query).fetchall()
    
    # render an HTML page using Jinja2
    return render_template('database.html', data=res)
