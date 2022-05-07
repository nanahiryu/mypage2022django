
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Weapon, Main, SubWeapon, Special, Range
import random
from .forms import RangeQuizForm, SubSpQuizForm

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'spla/index.html'


class WeaponListView(generic.ListView):
    template_name = 'spla/weapon_list.html'
    model = Weapon
    ordering = 'id'


class WeaponDetailView(generic.DetailView):
    template_name = 'spla/weapon_detail.html'
    model = Weapon


class MainListView(generic.ListView):
    template_name = 'spla/main_list.html'
    model = Main
    ordering = 'id'


class MainDetailView(generic.DetailView):
    template_name = 'spla/main_detail.html'
    model = Main
    context_object_name = 'main'


class SubListView(generic.ListView):
    template_name = 'spla/sub_list.html'
    model = SubWeapon
    ordering = 'id'


class SubDetailView(generic.DetailView):
    template_name = 'spla/sub_detail.html'
    model = SubWeapon
    context_object_name = 'sub'


class SpecialListView(generic.ListView):
    template_name = 'spla/special_list.html'
    model = Special
    ordering = 'id'


class SpecialDetailView(generic.DetailView):
    template_name = 'spla/special_detail.html'
    model = Special
    context_object_name = 'special'


class RangeQuizEnterView(generic.TemplateView):
    template_name = 'spla/range_quiz_enter.html'


class RangeQuizView(generic.FormView):
    template_name = 'spla/range_quiz.html'
    model = Range
    form_class = RangeQuizForm
    success_url = reverse_lazy('spla:range_quiz_result')

    # DBからランダムに一つrangeオブジェクトを取得し,それとはメインが違うrangeオブジェクトを取得し,contextに格納
    # それぞれのrange(first, second)のid, 射程がどちらが長いかの文字列(judge)をsessionに保存
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["first"] = random.choice(Range.objects.all())
        self.request.session["first"] = context["first"].id
        context["second"] = random.choice(
            Range.objects.exclude(main=context["first"].main))
        self.request.session["second"] = context["second"].id
        if context["first"].range > context["second"].range:
            self.request.session["judge"] = "左！"
        elif context["first"].range == context["second"].range:
            self.request.session["judge"] = "あいこ！"
        else:
            self.request.session["judge"] = "右！"
        return context

    # 解答内容(player_answer), 比較していたrange(first, second), 判定結果(judge)をcontextに入れてrender
    def form_valid(self, form):
        first = Range.objects.get(id=self.request.session["first"])
        second = Range.objects.get(id=self.request.session["second"])
        if form.data["answer"] == "first":
            player_answer = "左！"
        elif form.data["answer"] == "even":
            player_answer = "あいこ！"
        else:
            player_answer = "右！"
        context = {
            "first": first,
            "second": second,
            "judge": self.request.session["judge"],
            "player_answer": player_answer,
        }
        # print(context)
        return render(self.request, 'spla/range_quiz_result.html', context)


class SubSpQuizEnterView(generic.TemplateView):
    template_name = 'spla/subsp_quiz_enter.html'


class SubSpQuizView(generic.FormView):
    template_name = 'spla/subsp_quiz.html'
    model = Weapon
    form_class = SubSpQuizForm
    success_url = reverse_lazy('spla:subsp_quiz_result')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["weapon"] = random.choice(Weapon.objects.all())
        # 答えとなるサブ、スペシャルのidをsessionに渡す
        self.request.session["weapon"] = context["weapon"].id
        self.request.session["sub"] = context["weapon"].sub.id
        self.request.session["sp"] = context["weapon"].special.id
        return context

    def form_valid(self, form):
        # 正解と解答をcontextに格納
        context = {
            'weapon': Weapon.objects.get(id=self.request.session["weapon"]),
            'sub_correct': SubWeapon.objects.get(id=self.request.session["sub"]),
            'sp_correct': Special.objects.get(id=self.request.session["sp"]),
            'sub_ans': SubWeapon.objects.get(id=form.data["sub_choices"]),
            'sp_ans': Special.objects.get(id=form.data["sp_choices"]),
        }
        if context['sub_correct'] == context['sub_ans'] and context['sp_correct'] == context['sp_ans']:
            context['judge'] = True
        else:
            context['judge'] = False
        return render(self.request, 'spla/subsp_quiz_result.html', context)
