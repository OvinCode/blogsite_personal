from django.views.generic import TemplateView
from django.conf import settings

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
