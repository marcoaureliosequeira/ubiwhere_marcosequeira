"""ubiwhereExercise URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from ubiwhere_app.views import DataFromSensorViewSet

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('sensorData/list/author/(?P<author>[\w{}.-]{1,255})/$', DataFromSensorViewSet.as_view({'get': 'listByAuthor'}), name='listByAuthor'),
    url('sensorData/list/category/(?P<category>[\w{}.-]{1,255})/$', DataFromSensorViewSet.as_view({'get': 'listByCategory'}), name='listByCategory'),
    url('sensorData/list/location/(?P<location>[\w{}.-]{1,255})/$', DataFromSensorViewSet.as_view({'get': 'listByLocation'}), name='listByLocation'),
    url('sensorData/create/', DataFromSensorViewSet.as_view({'post': 'create'}), name='create'),
    url('sensorData/validate/(?P<dataId>[\d{1,}])/$', DataFromSensorViewSet.as_view({'put': 'validate'}), name='validate'),
]
urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]