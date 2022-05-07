from django.views import generic
from .models import AboutSkills

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'home/index.html'


class AboutView(generic.TemplateView):
    template_name = 'home/about.html'
    model = AboutSkills

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["skills"] = AboutSkills.objects.order_by('id')
        context["maxloop"] = [0 for i in range(5)]
        return context


class PortfolioView(generic.TemplateView):
    template_name = 'home/portfolio.html'
