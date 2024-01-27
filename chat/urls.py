from django.urls import path

from chat import views

urlpatterns = [
    path("chat/<int:pk>/", views.ChatPrivateRetrieveAPIView.as_view()),
]
