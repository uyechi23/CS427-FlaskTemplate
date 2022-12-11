"""
Simple Flask Application

This Flask app was written for the CS427 course at the University of Portland.
This should be used as a very basic Flask app with minimal implementation. This app will
use and explain the various tools needed to build a Flask application that may be useful
in the projects for the CS427 class.

Additionally, read the Jinja2 documentation for making HTML documents. Jinja2 is useful
when writing HTML documents that have constantly changing data, such as reading data
from a database. An example of this is included in the Flask Demo, under the "templates"
folder.

@Authors: Surj Patel, Jake Uyechi
@Date: December 6, 2022
"""

""" Importing Libraries

flask - the basis of Flask; includes the necessary libraries and modules for a Flask app
sqlite3 - a simplified database that integrates with python
"""
from flask import Flask, render_template
import sqlite3

""" Initializing your Flask App

The line app = Flask(__name__) defines this file as the main application
"""
app = Flask(__name__)

""" Routes

Routes are the center of your web application; Flask has several utilities to help you
build your webpage for many different IoT applications. 

Flask URL Parameters

Flask can use data from a URL to render a webpage. You can write this in your routes
by using <angle brackets>. Your IoT device can "visit" one of these routes with different
URL parameters, and the route can take that value and add it to a database (for example).
"""

# define a simple home route
@app.route('/')
def hello_world():
    return 'Hello World!'

# By default, Flask treats input parameters as strings
@app.route('/input/<value>')
def input(value):
    return f'The value passed to this URL is: {value}'

# You can specify the URL Parameter data types as well
# If you try to pass a non-integer value, an error 404 is returned
# Acceptable datatypes:
#   int, string, float, path
@app.route('/integerinput/<int:data>')
def integerinput(data):
    return f'The integer input has a value of: {data}'

""" Interacting with a database

sqlite3 is a python package that allows you to interface with SQL databases directly
from a python script. While it's not the best option for databases, it's the easiest
to set up and configure for starters. For the example application, we'll take some
data in a route and pass it to a database.

If you're using VSCode, there is a helpful extension called "SQLite Viewer" that
lets you easily see the contents of a database

IMPORTANT: This will not work for PythonAnywhere; they have their own way of setting
up databases using SQLAlchemy (similar, but requires more Python code). Link is here:
https://blog.pythonanywhere.com/121/
"""
@app.route('/addtodb/<string:name>/<int:value>')
def addtodb(name,value):
    # create a database connection/cursor
    con = sqlite3.connect('database.sqlite3')
    cur = con.cursor()
    
    # create a SQL query to create a database table;
    # CREATE TABLE - create a table
    # IF NOT EXISTS - if the table exists, ignore this entire query
    # dummydata(...) - the name of the table, followed by the column information
    # Column information format: column_name data_type options
    #   column_name - the name of the table column
    #   data_type - the type of data (INTEGER, TEXT, REAL, BLOB, NULL)
    #   options -   PRIMARY KEY: (one per table) a unique value for each row
    #               UNIQUE: like primary key, but there can be multiple UNIQUE columns
    #               NOT NULL: force this column to have valid data
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
    # the question marks are placeholders for values that can change the query
    # since column "id" was specified as an INTEGER PRIMARY KEY, it will automatically
    # increment itself for each piece of data inserted into the table
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
    # the first parameter is the .html file that will be rendered when the user visits the route
    # the second parameter is the context (or set of variables) that Jinja can use. You'll see
    # more of how the context is used by Jinja.
    return render_template('database.html', data=res)
