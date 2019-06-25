 #sampleproject URL Configuration

# #The `urlpatterns` list routes URLs to views. For more information please see:
#  #   https://docs.djangoproject.com/en/2.2/topics/http/urls/
# #Examples:
# #Function views
#  ##   1. Add an import:  from my_app import views
#    # 2. Add a URL to urlpatterns:  path('', views.home, name='home')
# #Class-based views
#  #   1. Add an import:  from other_app.views import Home
#   #  2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# #Including another URLconf
#  #   1. Import the include() function: from django.urls import include, path
#   #  2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path
from home1.views import form_view, booksearch, deletebook, editbook
from home1.views import home_view, design, register, form, carousel,html_form


urlpatterns = [
    path('',booksearch),
    path('deletebook/<id>',deletebook),
    path('editbook/<id>',editbook),
    path('home/',home_view),
    path('myproject/',design),

    path('form/',form),
    path('carousel/',carousel),
    path('forms/',form_view,name='forms'),
    path('contact/',form_view,name='contact'),
    path('html/',html_form),
    path('admin/',admin.site.urls),

]
# *************************************************** ]
# from django.conf.urls import include, url
# from django.contrib import admin
# from sampleproject import views
# from . import views
# #from home.views import home_view, base, registered
 
#'app_name' = 'registration'

# urlpatterns = [
#     path('', views.reg_redirect, name='reg_redirect'),
#     path('admin/', admin.site.urls),
#     path('base/registered', views.registered, name='registered')
# ]

#  from django.contrib import admin
#  from django.urls import path
#  from home.views import form_view, registered,index
# urlpatterns = [
#      path('', views.re_redirect,name='reg_redirect'),
#      path('admin/', admin.site.urls),
#      path('registered/',form_view,name='registered'),
#  ]
