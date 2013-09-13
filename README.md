citi_digits
===========

MIT Citi Digits


Development Environment
======================

    install virtualenv
    create virtualenv city_digits
    run python setup.py install


Inital Setup
============

    python manage.py syncdb
    python manage.py migrate citi_digits
    mkdir media/backup
    python manage.py import_old_data



Production setup
================

    The production environment for this application is ghostmap.mit.edu. The home directory will be '/afs/athena.mit.edu/user/v/d/vdat' ($HOME_DIRECTORY). The installation
    directions below are specific to this production instance and may need to be altered for another server.

    2013_09_07 : Created ssh key-pair for client's github account
                    $ ssh-keygen -t rsa -C "sew.williams@gmail.com"

               : Added generated key-pair to client's github SSH Keys

               : created virtual environment directory at $HOME_DIRECTORY/.virtualenv

               : made virtual environment for project
                    $ virtualenv --no-site-packages city_digits

               : Checked out application from client's github to '$HOME_DIRECTORY/app/'
                    $ git clone git@github.com:sw2279/citi_digits.git

               : Activate virtual environment and install app dependencies
                    $ source $HOME_DIRECTORY/.virtualenv/city_digits/bin/activate

               : Install needed mysql configs
                    $ sudo apt-get install libmysqlclient-dev python-dev

               : install app dependencies
                    $ python setup.py install

               : install mod_wsgi for apache
                    $ sudo aptitude install libapache2-mod-python libapache2-mod-wsgi

               : create media directory and backup directory
                    $ mkdir media; mkdir media/backup ; chmod a+rw media

               : add project apache config (below)

               : install mysql (pw: citydigits)
                    $ sudo apt-get install mysql-server

               : secure mysql server (answer yes to all questions)
                    $ mysql_secure_installation

               : create database and project user
                    $ mysql -u root -p
                    mysql> create database citi_digits;
                    mysql> grant all on citi_digits.* to 'city_user' identified by 'Eo@_rKR7)ZohFWT';

               : update settings.py with db user and password

               : set upstream repo (this will allow client to fetch updates from developers github)
                    $ git remote add upstream https://github.com/datvikash/citi_digits.git

                : install dateutil.parser
                    $ sudo pip install python-dateutil --upgrade

               : do initial setup
                    $ python manage.py syncdb
                    $ python manage.py migrate citi_digits
                    $ python manage.py import_old_data




Apache config
=============

##############################
## City Digits WSGI         ##
##############################

Alias /favicon.ico /afs/athena.mit.edu/user/v/d/vdat/app/citi_digits/mit_civic/citi_digits/static/favicon.ico

AliasMatch ^/([^/]*\.css) /afs/athena.mit.edu/user/v/d/vdat/app/citi_digits/mit_civic/citi_digits/static/css/$1

Alias /media/  /afs/athena.mit.edu/user/v/d/vdat/app/citi_digits/mit_civic/media/
Alias /static/ /afs/athena.mit.edu/user/v/d/vdat/app/citi_digits/mit_civic/citi_digits/static/

<Directory /afs/athena.mit.edu/user/v/d/vdat/app/citi_digits/mit_civic/citi_digits/static>
Order deny,allow
Allow from all
</Directory>

<Directory /afs/athena.mit.edu/user/v/d/vdat/app/citi_digits/mit_civic/media>
Order deny,allow
Allow from all
</Directory>

WSGIScriptAlias /citydigits /afs/athena.mit.edu/user/v/d/vdat/app/citi_digits/mit_civic/mit_civic/wsgi.py
WSGIPythonPath /afs/athena.mit.edu/user/v/d/vdat/app/citi_digits/mit_civic:/afs/athena.mit.edu/user/v/d/vdat/.virtualenv/city_digits/lib/python2.6/site-packages
#WSGIPythonPath /afs/athena.mit.edu/user/v/d/vdat/app/citi_digits/mit_civic


<Directory /afs/athena.mit.edu/user/v/d/vdat/app/citi_digits/mit_civic/mit_civic>
<Files wsgi.py>
Order deny,allow
Allow from all
</Files>
</Directory>



pip uninstall PIL
apt-get install libjpeg-dev
apt-get install zlib1g-dev
apt-get install libpng12-dev
pip install PIL
