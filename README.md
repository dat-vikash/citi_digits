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



