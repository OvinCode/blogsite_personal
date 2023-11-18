from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

class BasePageView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STATIC_URL'] = settings.STATIC_URL
        # Add any other common context variables you need
        return context


class IndexPageView(BasePageView):
    template_name = "index.html"

class AboutPageView(BasePageView):
    template_name = "about.html"

class ContactPageView(BasePageView):
    template_name = "contact.html"

class GalleryPageView(BasePageView):
    template_name = "gallery.html"

class SuccessPageView(BasePageView):
    template_name = "success.html"

class LoginPageView(BasePageView):
    template_name = "login.html"

class SignupPageView(TemplateView):
    template_name = "signup.html"
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:
            user = User.objects.create_user(username, email, password)
        # Redirect to a success page or login page after successful signup
            return HttpResponseRedirect('/success/')  # Change the URL as needed
        
        return render(request, self.template_name, {'error_message': 'Invalid data. Please fill in all fields.'})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
