etdui
=====

prototype django etd web app in python/django

hacked together one Friday at GW Libraries in Washington, DC, USA



setup
=====

Presuming you have a clean ubuntu-12.04 instance.

Install Apache and other dependencies

        $ sudo apt-get install apache2 libapache2-mod-wsgi libaio-dev python-dev python-profiler git libxml2-dev libxslt-dev solr-jetty openjdk-6-jdk


Pull down the project from github:

        (GW staff only)
        $ git clone git@github.com:gwu-libraries/etdui.git
        (everyone else)
        $ git clone https://github.com/gwu-libraries/etdui.git

This will create a directory ```etdui```, which we'll refer to as <ETDUI_HOME>.

Create a Python virtual environment for the project:

        $ sudo apt-get install python-setuptools
        $ sudo easy_install virtualenv
        $ cd <ETDUI_HOME>/etdui
        $ virtualenv --no-site-packages ENV


This will create a directory ```etdui```, which we'll refer to as <ETDUI_HOME>.

Activate your virtual environment:

        $ source ENV/bin/activate

Note that your commandline prompt will change to include ```(ENV)```.

Install django, tastypie, and other python dependencies:

        (ENV)$ pip install -r requirements.txt
        
Set up Solr via jetty:

* Edit ```/etc/default/jetty``` to set ```NO_START=0```, set
  ```JAVA_HOME=/usr/lib/jvm/java-6-openjdk-amd64```, and consider
  changing ```JETTY_PORT``` to a port that won't be publicly exposed (do not use 8080 if you will be running the server on that port or else the port will be unavailable).
  In development and testing, exposing Solr might be helpful; never 
  expose it in production.

* Copy the solr ```schema.xml``` for etdui into system-wide solr config
  (making a backup of the original if you like):

        $ sudo cp /etc/solr/conf/schema.xml /etc/solr/conf/schema.xml.orig
        $ sudo cp <ETDUI_HOME>/etd/etd/solr-schema.xml /etc/solr/conf/schema.xml

* Start jetty:

        $ sudo service jetty start

Create a local settings file for etdui by copying the local settings 
template to an active file:

        $ cd <ETDUI_HOME>/etdui/etd
        $ cp local_settings.py.template local_settings.py

Update the values in the ```local_settings.py``` file:  set a 
```SECRET_KEY```, and ensure that the port number in ```SOLR_URL``` matches 
```JETTY_PORT``` configured earlier in ```/etc/default/jetty```.

        $ vim local_settings.py

Copy the WSGI file template to an active file:

        $ cp wsgi.py.template wsgi.py

Update the wsgi.py file (Change the value of ENV to your environment path):

        $ vim wsgi.py
        
Now run the server:

        $ cd <ETDUI_HOME>/etd
        $ python ./manage.py runserver 0.0.0.0:8080 [or try 8089 if that port is unavailable (e.g. being used by jetty)]
