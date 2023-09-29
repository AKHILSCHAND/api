"""
URL configuration for restframework_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from restFramework_App import views
from restFramework_App.views import taskViewset
router= routers.SimpleRouter()
router.register('task',taskViewset)
router.register('completed_task',views.Completed)
router.register('not_completed_task',views.notCompleted)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
