citi_digits
===========

MIT Citi Digits


Development Environment
======================

    install virtualenv
    create virtualenv
    run python setup.py install


Inital Setup
============

    python manage.py syncdb
    python manage.py migrate citi_digits
    python manage.py import_old_data