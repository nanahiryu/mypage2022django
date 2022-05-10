from django import forms
from django.db import models
from .models import SubWeapon, Special

RangeQuizChoice = [
    ('first', '左！'),
    ('even', 'あいこ！'),
    ('second', '右！')
]


class RangeQuizForm(forms.Form):
    answer = forms.fields.ChoiceField(
        label='Answer',
        choices=RangeQuizChoice,
        required=True,
        widget=forms.RadioSelect()
    )


class SubSpQuizForm(forms.Form):
    sub_choices = forms.ModelChoiceField(
        label='サブ',
        queryset=SubWeapon.objects,
        required=True,
    )
    sp_choices = forms.ModelChoiceField(
        label='スペシャル',
        queryset=Special.objects,
        required=True,
    )
