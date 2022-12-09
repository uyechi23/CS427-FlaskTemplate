# **[CS427 - Internet of Things] Flask Template**

### **Authors**
Jake Uyechi (uyechi23@up.edu, jake.uyechi@gmail.com)\
Surj Patel (patels@up.edu)

## **Description**
This is a simple Flask app with the minimum required functionality for an Internet of Things (IoT) project. This includes Flask routing, URL parameters, 
Jinja2 HTML templating, and a simple local database using the sqlite3 Python library. Visit the related link to the supplementary ESP32 libraries to find
the wifi_client library that is compatible with this Flask template.

### **Related**
Supplementary CS427 ESP32 IoT Libraries - https://github.com/uyechi23/CS427-IoTLibraries

<br>

## **Setup**

### **Prerequisites**
- Python
- pip

### **Cloning the repository**
This Flask application will be run on a computer - it will be the server that will host the web application. Any device connected to the same Wi-Fi network can 
connect to the web application, which includes other laptops, phones, and IoT devices.

First, clone this repository:
```
git clone https://github.com/uyechi23/CS427-FlaskTemplate.git
```

### **Setting up a Virtual Environment**
We will need to set up a virtual environment - this allows us to easily set up annd run a lightweight application without needing to always install packages
through pip on every computer. The dependencies for the Flask application are listed in requirements.txt. The following commands are for Windows Command Prompt
and assume you already have Python and pip installed.
```
py -m pip install --user virtualenv
py -m virtualenv env
env\Scripts\activate
pip install -r requirements.txt
```

### **Running and Accessing the Flask App**
Finally, run the Flask app using the following command:
```
flask run -h 0.0.0.0 -p 5000
```

Your Flask app should now be running on a certain socket - you can use a smartphone or other device to verify the Flask app is running by typing the IP address
and port number into a web browser (i.e., 10.17.154.215:5000). Access routes in the Flask app by adding onto the end of the socket (i.e., 10.17.154.215:5000/route1).

To stop the Flask app, either exit the terminal or press CTRL-C.

## **Working with ESP32/Arduino**

### **Supplementary ESP32 Libraries**
Visit https://github.com/uyechi23/CS427-IoTLibraries to find the ESP32 library files that can be used with this Flask app. Use the wifi_client library to connect to
the Flask app.
