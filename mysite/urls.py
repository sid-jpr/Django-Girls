# Docstrings – you can write them at the top of a file, class or method to describe what it does
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, inc lude
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

# Writing regular expressions in Python is always done with r in front of the string. This is a helpful hint for
# Python that the string may contain special characters that are not meant for Python itself, but for the regular
# expression instead.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
# Django will now redirect everything that comes into 'http://127.0.0.1:8000/' to blog.urls and looks for further
# instructions there.
