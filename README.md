# CS427-FlaskTemplate
This is a supplementary Flask application for CS427 - Internet of Things at the University of Portland.
 
## Authors
Jake Uyechi (uyechi23@up.edu, jake.uyechi@gmail.com)
Surj Patel (patels@up.edu)

## Description
This is a simple Flask app with the minimum required functionality for an Internet of Things (IoT) project. This includes Flask routing, URL parameters, 
Jinja2 HTML templating, and a simple local database using the sqlite3 Python library.

## Setup

### Prerequisites
Python and pip installed on device.

### Cloning the repository
This Flask application will be run on a computer - it will be the server that will host the web application. Any device connected to the same Wi-Fi network can 
connect to the web application, which includes other laptops, phones, and IoT devices.

First, clone this repository:
```
git clone https://github.com/uyechi23/CS427-FlaskTemplate.git
```

### Setting up a Virtual Environment
We will need to set up a virtual environment - this allows us to easily set up annd run a lightweight application without needing to always install packages
through pip on every computer. The dependencies for the Flask application are listed in requirements.txt. The following commands are for Windows Command Prompt
and assume you already have Python and pip installed.
```
python3 -m pip install --user virtualenv
python3 -m virtualenv env
pip install -r requirements.txt
env\Scripts\activate
```

### Running and Accessing the Flask App
Finally, run the Flask app using the following command:
```
flask run -h 0.0.0.0 -p 5000
```

Your Flask app should now be running on a certain socket - you can use a smartphone or other device to verify the Flask app is running by typing the IP address
and port number into a web browser (i.e., 10.17.154.215:5000). Access routes in the Flask app by adding onto the end of the socket (i.e., 10.17.154.215:5000/route1).

To stop the Flask app, either exit the terminal or press CTRL-C.
