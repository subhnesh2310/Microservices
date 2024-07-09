"""cliCodec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from cliCodec.connectNE_cli import connectNE_subscription
from cliCodec.disconnectNe_cli import disconnectNE_subscription
from cliCodec.sendRCV_cli import sendrcv_subscription
from cliCodec.ComparePair_cli import compare_subscription
from cliCodec.retDataToTable_cli import retDataToTable

urlpatterns = [
    path('api/connectNE_subscription/', connectNE_subscription),
    path('api/disconnectNE_subscription/', disconnectNE_subscription),
    path('api/sendrcv_subscription/', sendrcv_subscription),
    path('api/compare_subscription/', compare_subscription),
    path('api/retDataToTable/', retDataToTable)
]