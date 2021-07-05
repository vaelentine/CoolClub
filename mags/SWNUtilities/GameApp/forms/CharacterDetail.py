from django.forms import ModelForm
from ..models import Character


class CharacterDetail(ModelForm):
    class Meta:
        model = Character
        exclude = ['attributes']
