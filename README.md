Base Project 

=======================

An Empty Shell Project

Setup
-----

* Clone this repo
* Copy `PD_Hub/settings/local.py.example` to `PD_Hub/settings/local.py`
* Add your local configurations to `PD_Hub/settings/local.py`
* Install Vagrant and Virtualbox
* Initialize the vagrant box - `vagrant up`
* Log into the server - `vagrant ssh`
* Create a super user using the command `python manage.py createsuperuser`
* Launch the app - `./manage.py runserver 0.0.0.0:8000`
* Access the app in your browser - `http://localhost:8111`
