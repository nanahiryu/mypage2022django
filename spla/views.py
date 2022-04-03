
from django.views import generic
from .models import Weapon, Main, SubWeapon, Special

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'spla/index.html'


class WeaponListView(generic.ListView):
    template_name = 'spla/weapon_list.html'
    model = Weapon


class WeaponDetailView(generic.DetailView):
    template_name = 'spla/weapon_detail.html'
    model = Weapon


class MainListView(generic.ListView):
    template_name = 'spla/main_list.html'
    model = Main


class MainDetailView(generic.DetailView):
    template_name = 'spla/main_detail.html'
    model = Main
    context_object_name = 'main'


class SubListView(generic.ListView):
    template_name = 'spla/sub_list.html'
    model = SubWeapon


class SubDetailView(generic.DetailView):
    template_name = 'spla/sub_detail.html'
    model = SubWeapon
    context_object_name = 'sub'


class SpecialListView(generic.ListView):
    template_name = 'spla/special_list.html'
    model = Special


class SpecialDetailView(generic.DetailView):
    template_name = 'spla/special_detail.html'
    model = Special
    context_object_name = 'special'
