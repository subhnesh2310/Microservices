"""apimanager URL Configuration

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
from apimanager.connectNE import ConnectView
from apimanager.disconnectNE import DisconnectView
from apimanager.sendrcv import SendRCVViewSet
from apimanager.comaprePairs import ComparePairsView
from apimanager.generate_logs import LogFileView
from apimanager.retDataToTables import RetDataTOTables
from apimanager.gcs_api import GCSFileListView
from apimanager.gcp_content import FileContentView
from apimanager.gcs_upload_file import GCSFileUploadWithStructureView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/connectNE/', ConnectView.as_view()),
    path('api/disconnectNE/', DisconnectView.as_view()),
    path('api/sendrcv/', SendRCVViewSet.as_view()),
    path('api/logs/', LogFileView.as_view(), name='log-file'),
    path('api/retDataToTab/', RetDataTOTables.as_view()),
    path('api/compare_pair/', ComparePairsView.as_view()),
    path('api/files/', GCSFileListView.as_view(), name='gcs-file-list'),
    path('api/bucket_files/', FileContentView.as_view(), name='file-content'),
    path('api/upload_with_structure/', GCSFileUploadWithStructureView.as_view(), name='upload_with_structure'),
]
