# **[CS427 - Internet of Things] Flask Template**

### **Authors**
Jake Uyechi (uyechi23@up.edu, jake.uyechi@gmail.com)\
Surj Patel (patels@up.edu)

## **Description**
This is a simple Flask app with the minimum required functionality for an Internet of Things (IoT) project. This includes Flask routing, URL parameters, 
Jinja2 HTML templating, and a simple local database using the sqlite3 Python library. Visit the related link to the supplementary ESP32 libraries to find
the wifi_client library that is compatible with this Flask template.

### **Related**
Supplementary CS427 ESP32 IoT Libraries - https://github.com/uyechi23/CS427-IoTLibraries \
Documentation for SQLite3 - https://docs.python.org/3/library/sqlite3.html \
Alternative SQLAlchemy Database for PythonAnywhere - https://blog.pythonanywhere.com/121/ \
Jinja Templating Primer - https://realpython.com/primer-on-jinja-templating/ 

<br>

## **Setup - Windows**

### **Prerequisites**
- Python (https://www.python.org/downloads/)
- git (https://git-scm.com/download/win)

### **Cloning the repository**
This Flask application will be run on a computer - it will be the server that will host the web application. Any device connected to the same Wi-Fi network can 
connect to the web application, which includes other laptops, phones, and IoT devices.

First, open the Windows Command Prompt. Substitute [username] with your own username. Run the set of following commands to clone the git repository into a local
folder (this can be wherever you want to save your Flask application, but for this example, I chose my desktop):
```
C:\Users\[username]> chdir C:\Users\[username]\Desktop
C:\Users\[username]\Desktop> git clone https://github.com/uyechi23/CS427-FlaskTemplate.git
C:\Users\[username]\Desktop> chdir "CS427-FlaskTemplate.git"
```

Once the files are cloned, you have two choices: remove the git repository, or (if you're familiar with git) change the remote to a personal GitHub repository.

To remove the git repository, run the following command:
```
C:\Users\[username]\Desktop\CS427-FlaskTemplate> rmdir /s .git
```

Once the original .git repository is deleted, you can add it to your own GitHub repository (note that you will need to create a completely empty directory
in GitHub first, then retrieve the address of the repository and use it to replace [GitHub repository address]):
```
C:\Users\[username]\Desktop\CS427-FlaskTemplate> git init
C:\Users\[username]\Desktop\CS427-FlaskTemplate> git add .
C:\Users\[username]\Desktop\CS427-FlaskTemplate> git commit -m "Initial Commit"
C:\Users\[username]\Desktop\CS427-FlaskTemplate> git branch -M main
C:\Users\[username]\Desktop\CS427-FlaskTemplate> git remote add origin [GitHub repository address]
C:\Users\[username]\Desktop\CS427-FlaskTemplate> git push -u origin main
```

NOTE: GitHub discontinued logging in through HTTPS username/password combinations back in August 2021.
To get around this issue, view the article below to set up a personal access token to be able to push to your GitHub repository: \
https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

Alternatively, view these articles to create an SSH key and connect it to your GitHub account: \
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent \
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account 

### **Setting up a Virtual Environment**
We will need to set up a virtual environment - this allows us to easily set up annd run a lightweight application without needing to always install packages
through pip on every computer. The dependencies for the Flask application are listed in requirements.txt. The following commands are for Windows Command Prompt
and assume you already have Python and pip installed. Once the virtual environment is activated, you should see an (env) before the directory on the command prompt.
```
C:\Users\[username]\Desktop\CS427-FlaskTemplate> py -m pip install --user virtualenv
C:\Users\[username]\Desktop\CS427-FlaskTemplate> py -m virtualenv env
C:\Users\[username]\Desktop\CS427-FlaskTemplate> env\Scripts\activate
C:\Users\[username]\Desktop\CS427-FlaskTemplate> py -m pip install -r requirements.txt
```

### **Running and Accessing the Flask App**
Finally, run the Flask app using the following command:
```
C:\Users\[username]\Desktop\CS427-FlaskTemplate> flask run -h 0.0.0.0 -p 5000
```

Your Flask app should now be running on a certain socket - you can use a smartphone or other device to verify the Flask app is running by typing the IP address
and port number into a web browser (i.e., 10.17.154.215:5000). Access routes in the Flask app by adding onto the end of the socket (i.e., putting
"10.17.154.215:5000/input/10" in your browser would access the Flask route described by the @app.route("/input/\<value\>") decorator).

To stop the Flask app, either exit the terminal or press CTRL-C.

<br>

## **Setup - Linux**

### **Prerequisites**
- Python (https://www.python.org/downloads/)
- git (https://git-scm.com/download/win)

### **Cloning the repository**
This Flask application will be run on a computer - it will be the server that will host the web application. Any device connected to the same Wi-Fi network can 
connect to the web application, which includes other laptops, phones, and IoT devices.

First, open a Linux terminal. Run the set of following commands to clone the git repository into a local folder (this can be wherever you want to save your
Flask application, but for this example, I chose my desktop):
```
~$ cd ~/Desktop
~/Desktop$ git clone https://github.com/uyechi23/CS427-FlaskTemplate.git
~/Desktop$ cd "CS427-FlaskTemplate.git"
```

Once the files are cloned, you have two choices: remove the git repository, or (if you're familiar with git) change the remote to a personal GitHub repository.

To remove the git repository, run the following command:
```
~/Desktop/CS427-FlaskTemplate$ rm -rf .git
```

Once the original .git repository is deleted, you can add it to your own GitHub repository (note that you will need to create a completely empty directory
in GitHub first, then retrieve the address of the repository use it to replace [GitHub repository address]):
```
~/Desktop/CS427-FlaskTemplate$ git init
~/Desktop/CS427-FlaskTemplate$ git add .
~/Desktop/CS427-FlaskTemplate$ git commit -m "Initial Commit"
~/Desktop/CS427-FlaskTemplate$ git branch -M main
~/Desktop/CS427-FlaskTemplate$ git remote add origin [GitHub repository address]
~/Desktop/CS427-FlaskTemplate$ git push -u origin main
```

NOTE: GitHub discontinued logging in through HTTPS username/password combinations back in August 2021.
To get around this issue, view the article below to set up a personal access token to be able to push to your GitHub repository: \
https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

Alternatively, view these articles to create an SSH key and connect it to your GitHub account: \
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent \
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account 

### **Setting up a Virtual Environment**
We will need to set up a virtual environment - this allows us to easily set up annd run a lightweight application without needing to always install packages
through pip on every computer. The dependencies for the Flask application are listed in requirements.txt. The following commands are for Windows Command Prompt
and assume you already have Python and pip installed. Once the virtual environment is activated, you should see an (env) before the directory on the command prompt.
```
~/Desktop/CS427-FlaskTemplate$ python3 -m pip install --user virtualenv
~/Desktop/CS427-FlaskTemplate$ python3 -m virtualenv env
~/Desktop/CS427-FlaskTemplate$ source env/bin/activate
~/Desktop/CS427-FlaskTemplate$ python3 -m pip install -r requirements.txt
```

### **Running and Accessing the Flask App**
Finally, run the Flask app using the following command:
```
~/Desktop/CS427-FlaskTemplate$ flask run -h 0.0.0.0 -p 5000
```

Your Flask app should now be running on a certain socket - you can use a smartphone or other device to verify the Flask app is running by typing the IP address
and port number into a web browser (i.e., 10.17.154.215:5000). Access routes in the Flask app by adding onto the end of the socket (i.e., putting
"10.17.154.215:5000/input/10" in your browser would access the Flask route described by the @app.route("/input/\<value\>") decorator).

To stop the Flask app, either exit the terminal or press CTRL-C.

## **Working with ESP32/Arduino**

### **Supplementary ESP32 Libraries**
Visit https://github.com/uyechi23/CS427-IoTLibraries to find the ESP32 library files that can be used with this Flask app. Use the wifi_client library to connect to
the Flask app, or the iot_demo library to see how the ESP32 interacts with the SQLite database through Flask.
