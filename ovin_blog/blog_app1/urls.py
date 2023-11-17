from django.urls import path
from . import views
from .views import IndexPageView,AboutPageView,ContactPageView,GalleryPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
]
