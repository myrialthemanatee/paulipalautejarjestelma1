from django import forms
from django.forms.widgets import RadioSelect
from .models import TalkooPalaute, KokousPalaute, Hairioilmoitus


class TalkooPalauteForm(forms.ModelForm):
    class Meta:
        model = TalkooPalaute
        fields = ['t_hyvaa', 't_huonoa','t_kehitettavaa', 'arvosana']
        widgets = {
            't_hyvaa': forms.Textarea, 't_huonoa': forms.Textarea, 't_kehitettavaa': forms.Textarea, 'arvosana': forms.RadioSelect
        } 

class KokousPalauteForm(forms.ModelForm):
    class Meta:
        model = KokousPalaute
        fields = ['k_hyvaa', 'k_huonoa','k_kehitettavaa', 'arvosana']
        widgets = {
            'k_hyvaa': forms.Textarea, 'k_huonoa': forms.Textarea, 'k_kehitettavaa': forms.Textarea, 'arvosana': forms.RadioSelect
        }

class HairioilmoitusForm(forms.ModelForm):
    class Meta:
        model = Hairioilmoitus
        fields = ['h_huoneisto', 'h_hairionkuvaus','h_hairiontarkennus', 'arvosana']
        widgets = {
            'h_huoneisto': forms.Textarea(attrs={'rows':1, 'cols':15}), 'h_hairionkuvaus': forms.Textarea, 'h_hairiontarkennus': forms.Textarea, 'arvosana': forms.RadioSelect
        }