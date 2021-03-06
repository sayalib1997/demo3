Quick installation
------------------

1. Clone the repository::

    git svn clone https://svn.eionet.europa.eu/repositories/Python/flis_django/
    cd flis_django


2. Create & activate a virtual environment::

    virtualenv sandbox
    echo '*' > sandbox/.gitignore
    source sandbox/bin/activate


3. Install prerequisites if missing::
    python2.7 or higher
    apt-get install python-setuptools python-dev
    apt-get install mysql-client-5.5 mysql-common mysql-server-5.5


4. Install dependencies::

    pip install -r requirements-dev.txt


5. Create a instance folder::
     mkdir -p instance


6. Create local_settings.py ::
    touch flis/local_settings.py
     # Check local.settings.example for configuration details


7. Set up the:
   a. MySQL database::
    mysql > CREATE SCHEMA flis CHARACTER SET utf8 COLLATE utf8_general_ci;
    postgres > CREATE DATABASE flis WITH ENCODING 'UTF-8';
    ./manage.py syncdb
    ./manage.py migrate
   b. Postgresql database::
    root # su - postgres;
    postgres $ psql template1
    template1=# CREATE USER edw WITH PASSWORD 'edw';
    template1=# GRANT ALL PRIVILEGES ON DATABASE reportdb TO edw;
    ./manage.py syncdb
    ./manage.py migrate


Create a migration after changes in models.py
---------------------------------------------
::
    ./manage.py schemamigration flis --auto
    ./manage.py migrate


Load countries from fixture
---------------------------
::
    ./manage.py loaddata countries

