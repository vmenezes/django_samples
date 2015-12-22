# Django GeoDjango Sample

This is a sample of GeoDjango, a way efficient way of dealing with geolocations inside a Django project.

GeoDjango relies on 3rd party solutions on the database/system layer. For this tutorial I will use Postgres with PostGIS running on a Linux Ubuntu 64bits machine.

For following along you will need to have installed Vagrant and VirtualBox (systems to manage virtual machines).

## Creating the virtual machine

Run the commands bellow to create your Linux/Ubuntu virtual machine:

- vagrant init ubuntu/trusty64
- vagrant up
- vagrant ssh

The first command creates a Vagrantfile inside your folder that contains instructions for setting up the virtual machine.

The second is the command to turn on the virtual machine(when running for the first time it will download/install the image).

The third command connects thru SSH to your virtual machine.

When you are done, you can run "exit" to quit the SSH session and "vagrant halt" to shutdown your virtual machine.


## Setup a shared folder between local and virtual machine

- Shutdown the virtual machine with `vagrant halt` command.
- Edit "Vagranfile" created inside your folder and add following lines:
```
config.vm.network "forwarded_port", guest: 8000, host: 8000
config.vm.synced_folder "./", "/home/vagrant"
```
-Now any file inside this folder will be available in the virtual machine at /home/vagrant

Ps: usually after this change vagrant asks for password when turning on, the default password is "vagrant".

Run a `vagrant up` and `vagrant ssh` to go back to the virtual machine. Now files created/edited on this folder will e available in the virtual machine.


## Installing system requirements on the Linux machine

- sudo apt-get update
- sudo apt-get install python-virtualenv
- sudo apt-get install python3-dev
- sudo apt-get install postgresql postgresql-contrib postgresql-server-dev-9.3
- sudo apt-get install postgis postgresql-9.3-postgis-2.1
- sudo apt-get install libproj-dev gdal-bin


## Create database nd add PostGIS to it

- sudo -u postgres createuser -P dbuser
- sudo -u postgres createdb sampledb
- sudo -u postgres psql
- ALTER USER dbuser CREATEDB;
- ALTER ROLE dbuser SUPERUSER;
- \q
- sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" sampledb

Now the system is ready to receive a GeoDjango application. Virtualenv, etc will be created and run here inside the virtual machine, but as we created the shared folder, we can edit/create files using our favorite text editor.


## Initialize the GeoDjango project

- virtualenv -p python3 env
- source env/bin/activate
- pip install django-toolbelt
- pip freeze > requirements.txt
- django-admin startproject myproj
- add 'django.contrib.gis' to the INSTALLED_APPS on settings.py
- edit the database config in the settings.py as follows:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'sampledb',
        'USER': 'dbuser',
        'PASSWORD': 'dbpwd',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

Now before going any further, lets check if our project is working.

- python manage.py migrate
- python manage.py runserver 0.0.0.0:8000
- Open your web brownser and go to http://localhost:8000 to access your django project that at this moment should be something like:
```
It worked!
Congratulations on your first Django-powered page.
```

## Create a model with geolocation field

- python manage.py startapp app
- Append 'app' to `INSTALLED_APPS` on settings.py
- Edit app/models.py
```
from django.contrib.gis.db import models

class Park(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    contry = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    address = models.TextField()
    location = models.PointField()

    def __str__(self):
        return "{}, {}, {} - {} - {}, Coords: {}".format(
            self.name,
            self.address,
            self.city,
            self.state,
            self.contry,
            self.location.coords
        )

```

- python manage.py makemigrations
- python manage.py migrate
- Edit app/admin.py

```
from django.contrib import admin
from .models import Park

admin.site.register(Park)
```

- python manage.py createsuperuser
- python manage.py runserver 0.0.0.0:8000
- Open your web brownser and go to http://localhost:8000/admin login and add few Parks.
- See that the widget to render the location field is not connected to the other fields allowing a user to type one address and select another in the map.

## Now lets see how to manipulate create and retrieve instances with PointField from python code

- python manage.py shell
- Import the Park model and need PostGIS classes/methods needed

```
from app.models import Park
from django.contrib.gis.geos import Point, fromstr
from django.contrib.gis.measure import Distance
```

- Lets create a Park that corresponds to the Tribeca Skate Park in NYC
```
tribeca_skatepark_location = fromstr("POINT({} {})".format(40.7195189,-74.014987))
tribeca_skatepark = Park(
    name = "Tribeca Skate Park",
    desc = "Street Skate Park",
    country = "US",
    state = "NY",
    city = "New York",
    address = "N Moore St",
    location = tribeca_skatepark_location
)

tribeca_skatepark.save()
```

- We can do a basic check with `Park.objects.all()`that must return the "Tribeca Skatepark" that we just created and the other added thru the admin website. ".get .filter .first .last", etc also available as any other django models but this is not why we are using GeoDjango. Lets do some queries by geolocation.

```
distance = {'mi': 4}
center = fromstr("POINT({} {})".format(40.7595287,-74.0007471))
Park.objects.filter(location__distance_lte=(center, Distance(**distance)))

```


Is there anything wrong or could anything be done better?

Fork/Fix it! Pull requests are welcome :)

If you prefer, open an issue or contact me at menezes.victor@gmail.com
