from django import forms
from django.forms import ModelForm

from .models import Informazioni_Personali,Esperienza_Lavorativa,Informazione_Istruzione,Cap_Lingue,Comp_Relazionali,Comp_Organizzative,Comp_Artistiche,Comp_Tecniche,Altre_Comp,Altre_Informa

class DateInput(forms.DateInput):
    input_type = 'date'

class FormInfoPers(forms.ModelForm):
    class Meta:
        model = Informazioni_Personali
        fields = '__all__'
        widgets = {'indirizzo': forms.Textarea(attrs={'cols': 35,'rows':1})}
        widgets = {'patenti': forms.Textarea(attrs={'cols': 35,'rows':1})}
        widgets = {'data_di_nascita': DateInput()}
        
class FormLavoro(forms.ModelForm):
    class Meta:
        model =  Esperienza_Lavorativa
        fields = '__all__'
class FormIstruzione(forms.ModelForm):
    class Meta:
        model =  Informazione_Istruzione
        fields = '__all__'
class FormLingue(forms.ModelForm):
    class Meta:
        model =  Cap_Lingue
        fields = '__all__'
class FormRelazionali(forms.ModelForm):
    class Meta:
        model = Comp_Relazionali
        fields = '__all__'
        widgets = {'descrizione_rela': forms.Textarea(attrs={'cols': 80,'rows':5})}

class FormOrganizzative(forms.ModelForm):
    class Meta:
        model = Comp_Organizzative
        fields = '__all__'
        widgets = {'descrizione_orga': forms.Textarea(attrs={'cols':80,'rows':5})}
class FormTecniche(forms.ModelForm):
    class Meta:
        model = Comp_Tecniche
        fields = '__all__'
        widgets = {'descrizione_tecniche': forms.Textarea(attrs={'cols':80,'rows':5})}

class FormArtistiche(forms.ModelForm):
    class Meta:
        model = Comp_Artistiche
        fields = '__all__'
        widgets = {'descrizione_artistiche': forms.Textarea(attrs={'cols':80,'rows':5})}

class FormAltre(forms.ModelForm):
    class Meta:
        model = Altre_Comp
        fields = '__all__'
        widgets = {'descrizione_altre': forms.Textarea(attrs={'cols':80,'rows':5})}

class FormAltreInfo(forms.ModelForm):
    class Meta:
        model = Altre_Informa
        fields = '__all__'
        widgets = {'altre_informazioni': forms.Textarea(attrs={'cols':80,'rows':5})}

