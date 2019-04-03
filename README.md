# TFBSinG
Prediction of the binding sites of multiple transcription factors in a whole genome

>  >100,000bp
## Requirements
* Windows
* msvcp120d.dll, msvcr120d.dll, vcomp120d.dll
* For python3 (python 3.6.4)
* Django
* train_model_hg19.model : http://165.246.44.27:8080/share.cgi?ssid=0E5Pj1q
* train_model_mm10.model : http://165.246.44.27:8080/share.cgi?ssid=0nbSCBQ

##  Setup progress (video)
* https://m.youtube.com/watch?v=gdxYlS55toU

* http://165.246.44.27:8080/share.cgi?ssid=082bw63

## Site Instructions
How to set up TFBSinG's Python (django)

1. You can configure the settings on your local PC using the following method.
 
```django-admin startproject lee_test```

2. Move folder to lee_test location

```python manage.py startapp home_site```

3. Move the file to root (lee_test)
* train_model_hg19.model
* train_model_mm10.model

4. Change the settings.py in the folder of lee_test as below.

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
Change the urls.py in the folder of lee_test as below.
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('home_site/', include('home_site.urls')),
    # new url definition
    path('admin/', admin.site.urls),
]
```

Run the Django project
```
python manage.py runserver
```

Enter the following address on the web
```
http://127.0.0.1:8000/home_site/
```

## Bug report
- DLL(MSVCP120D,MSVCR120D,VCOMP120D).zip is decomposed.
- 3 dll files move to C:\Windows\System32.
```
MSVCP120D.dll
MSVCR120D.dll
VCOMP120D.dll
```


Copyright 2018 Chungkeun Lee, All Rights Reserved.
