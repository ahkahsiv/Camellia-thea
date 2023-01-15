from . models import contact
from django.forms import ModelForm

class contactForm(ModelForm):
    class Meta:
        model=contact
        fields="__all__"