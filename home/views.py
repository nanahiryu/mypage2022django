from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'home/index.html'

class AboutView(generic.TemplateView):
    template_name = 'home/about.html'