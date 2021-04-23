1- Install Python 3:

Most macOS operating systems come with the Python 2.7 version.  The system needs python 3.6 or newer to work correctly. Python3 should be installed alongside python(2) because some apps may still depend on older python(2). Here is the link to install Python3: https://www.python.org/downloads/. 
.

.

.

.

.

.

.

2- Install Pycharm:

This  is the link to install the Pycharm:  https://www.jetbrains.com/pycharm/download/#section=mac
The  minimum system requirements required before installing Pycharm: 

1- 4GB RAM minimum, 8 GB RAM recommended.

2- 1.5GB hard disk space + at least 1 GB for caches.

3- 1024×768 minimum screen resolution.

4- Python 2.7or newer.

.

.

.

.

.

.

.





3- Create a new project:

After installing Python and Pycharm, a new project can be created and named using the Pycharm. The project’s name in this project is “Onlinechat.”

After the creation of a new project ( Onlinechat ) has been done. Adding the Python interpreter to the new project is required. This process can be done by selecting Pycharm, Preferences, Project: Onlinechat , Python interpreter. 

.

.

.

.

.

.

.





4- Install Python libraries:

In this configuration step, some Python libraries have been added to the Python interpreter of the project. This process can be done by executing the following commands individually in the Pycharm terminal.



pip install azure (https://pypi.org/project/azure/)

pip install flask (https://pypi.org/project/Flask/)

pip install flask flask-cors simplejson (https://pypi.org/project/Flask-Cors/ )

pip install pusher (https://pypi.org/project/pusher/)
 
pip install virtualenv (https://pypi.org/project/virtualenv/)

pip install translate (https://pypi.org/project/translate/)

pip install vaderSentiment (https://pypi.org/project/vaderSentiment/)

pip install --upgrade nltk (https://pypi.org/project/nltk/)

pip install --upgrade vaderSentiment (https://pypi.org/project/vader-sentiment/) 

pip install requests (https://pypi.org/project/requests/) 

pip install matplotlib (https://pypi.org/project/matplotlib/)

pip install SDK (https://pypi.org/project/SDK/)

pip install Pillow (https://pypi.org/project/Pillow/)

pip install azure-ai-textanalytics (https://pypi.org/project/azure-ai-textanalytics/)

pip install matplotlib (https://pypi.org/project/matplotlib/)

pip install azure-cognitiveservices-vision-computervision (https://pypi.org/project/azure-cognitiveservices-vision-computervision/)

                   
To make sure that all Python libraries have been installed successfully, all these libraries should appear in the project’s python interpreter.  

.

.

.

.

.

.

.





5- Setting up Azure:

Azure services -- translate service and text analytics service--  have been used in this project by including Azure’s keys in the code. Getting the Azure’s keys can be done by creating an account on the Azure portal (https://azure.microsoft.com/en-us/account/), adding a resource, searching the marketplace, and creating.  After the creation of the service, its API key and the endpoint will be offered. 

Remember to replace the Azure keys with the keys in  in the following files:

1- translate.py

2- synthesize.py

3- sentiment.py

 .

.

.

.

.

.

.
 
 
6- Setting up Pusher:

The first step here will be to get a Pusher Channels application. We need the application credentials for our real time messaging to work.

Go to the Pusher website (https://pusher.com/) and create an account. After creating an account, you should create a new application. Follow the application creation wizard and then you should be given your application credentials.

There’s one more thing we need to do here on this dashboard; because we will directly be triggering the message events on the client side of the application, we need to turn on a special feature that is turned off by default for security reasons. To learn more about triggering events on the client side, you can read the documentation here (https://pusher.com/docs/client_api_guide/client_events#trigger-events).

On the dashboard, click on App settings and scroll to the bottom of the page then select the option that says Enable client events.

Remember to replace the PUSHER_* keys with the keys in your Pusher 
dashboard in the following files:

1- app.js

2- app.py 


.

.

.

.

.

.

.




7- Running the application:

you can test the application using this command:

   $ flask run
   

Now if we visit (http://127.0.0.1:5000/) and (http://127.0.0.1:5000/admin) we should test the application:
