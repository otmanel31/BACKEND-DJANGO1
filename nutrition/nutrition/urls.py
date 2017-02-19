"""nutrition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from aliments.views import *
from users.views import *

#admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'aliments', AlimentViewSet)
router.register(r'nutriment', NutrimentViewSet)
router.register(r'portionaliments', PortionalimentViewSet)
router.register(r'nutdata', NutdataViewSet)
router.register(r'users', NutriuserViewset)
router.register(r'repas', RepasViewset)
router.register(r'elementrepas', ElementrepasViewset)
#router.register(r'search')


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^api/', routers.urls)
# ]
urlpatterns = (
    # Examples:
    # url(r'^$', 'eboutique.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^aliments/mean/(?P<nutr_no>\d+)$',ListAliments.as_view(),name='mean'),
  #   url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
)
