from django.urls import path
from . import views
from .views import IndexPageView,AboutPageView,ContactPageView,GalleryPageView,LoginPageView,SignupPageView,SuccessPageView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    # path('success/', SuccessPageView.as_view(), name='success'),
    path('dashboard/', LoginView.as_view(template_name='dashboard.html'), name='dashboard'),
    
]
