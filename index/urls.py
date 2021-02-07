from django.urls import path
from index import views

urlpatterns = [
    path("", views.home, name="home"),
    path("more/<int:art_type>/", views.more_images, name="more"),
]
