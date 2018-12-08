from django.contrib import admin
from resumes.models import Informazioni_Personali,Esperienza_Lavorativa,Informazione_Istruzione,Cap_Lingue
from resumes.models import Comp_Relazionali,Comp_Organizzative,Comp_Tecniche,Comp_Artistiche,Altre_Comp,Altre_Informa
# Register your models here.
admin.site.register(Informazioni_Personali)
admin.site.register(Esperienza_Lavorativa)
admin.site.register(Informazione_Istruzione)
admin.site.register(Cap_Lingue)
admin.site.register(Comp_Relazionali)
admin.site.register(Comp_Organizzative)
admin.site.register(Comp_Tecniche)
admin.site.register(Comp_Artistiche)
admin.site.register(Altre_Comp)
admin.site.register(Altre_Informa)

