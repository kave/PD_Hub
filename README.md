PD Hub Project 

=======================


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


Heroku Deployment Commands
-----
* heroku create {nameOfHerokuApp}
* heroku config:add BUILDPACK_URL=https://github.com/ddollar/heroku-buildpack-multi.git
* git push heroku master
* heroku addons:add heroku-postgresql
* heroku ps:scale web=1
* heroku run python manage.py syncdb
