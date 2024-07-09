from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from pixi_db.views import (
    # SQLAlchemyComparePairsAPIView,
    SQLAlchemyConnectNEAPIView,
    SQLAlchemyDisconnectNEAPIView,
    TestExecutionAPIView,
    UsersAPIView,
    TestStepsResultsAPIView,
    TestExecutionMetricsAPIView,
    MetadataAPIView
    # SQLAlchemySendRCVAPIView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/connectdb/', SQLAlchemyConnectNEAPIView.as_view()),
    path('api/disconnectdb/', SQLAlchemyDisconnectNEAPIView.as_view()),
    path('test-execution/', TestExecutionAPIView.as_view(), name='test-execution-list'),
    path('test-execution/<str:pk>/', TestExecutionAPIView.as_view(), name='test-execution-detail'),
    path('users/', UsersAPIView.as_view(), name='users-list'),
    path('users/<str:pk>/', UsersAPIView.as_view(), name='users-detail'),
    path('teststeps-results/', TestStepsResultsAPIView.as_view()),
    path('teststeps-results/<str:log_id>/', TestStepsResultsAPIView.as_view()),
    path('test-execution-metrics/', TestExecutionMetricsAPIView.as_view(), name='test-execution-metrics-list'),
    path('test-execution-metrics/<str:pk>/', TestExecutionMetricsAPIView.as_view(), name='test-execution-metrics-detail'),
    path('metadata/', MetadataAPIView.as_view(), name='metadata-list'),
    path('metadata/<int:pk>/', MetadataAPIView.as_view(), name='metadata-detail'),

    # path('api/sendRcvdb/', SQLAlchemySendRCVAPIView.as_view()),
    # path('api/compairPairdb/', SQLAlchemyComparePairsAPIView.as_view()),

]
