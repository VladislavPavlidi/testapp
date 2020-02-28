from django.forms import ModelForm

from .models import Realtor


class RealtorForm(ModelForm):
    class Meta:
        model = Realtor
        fields = ('surname', 'name', 'subdivision')
