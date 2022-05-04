from django import forms
from django.db import models

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
