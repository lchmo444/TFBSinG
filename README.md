# TFBSinG
Prediction of the binding sites of multiple transcription factors in a whole genome


## Requirements
* Windows
* For python3 (python 3.6.4)
* Django
* train_model_hg19.model : http://165.246.44.27:8080/share.cgi?ssid=0E5Pj1q
* train_model_mm10.model : http://165.246.44.27:8080/share.cgi?ssid=0nbSCBQ

## Site Instructions
How to set up TFBSinG's Python (django)

You can configure the settings on your local PC using the following method.

```django-admin startproject lee_test2```

Move folder to lee_test2 location

```python manage.py startapp home_site```

Change the settings.py in the folder of lee_test2 as below.

```ALLOWED_HOSTS = ['*']```
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
'home_site.apps.HomeSiteConfig',]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static"),
]
```
Change the urls.py in the folder of lee_test2 as below.
```
url patterns = [
path('home_site/',include('home_site.urls)),
path('admin/', admin.site.urls),
]
```



Copyright 2018 Chungkeun Lee, All Rights Reserved.
