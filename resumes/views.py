from django.shortcuts import render
from .forms import FormInfoPers,FormLavoro,FormIstruzione,FormLingue,FormRelazionali,FormOrganizzative,FormTecniche,FormArtistiche,FormAltre,FormAltreInfo
from django.http import HttpResponse

from django.http import FileResponse,JsonResponse

from django.template.loader import get_template


import pdfkit
from .models import Informazioni_Personali,Esperienza_Lavorativa,Informazione_Istruzione,Cap_Lingue,Comp_Relazionali,Comp_Organizzative,Comp_Tecniche,Comp_Artistiche,Altre_Comp,Altre_Informa
from django.template import Context
from django_ajax.decorators import ajax
formlavoro=[]
lavo=[]
valido=False

'''
variabili temporali per acchiappare dati lavoro dal java script 
ed aggiungerli a liste per poi quando viene premuto il tasto invia aggiunto 
in database
'''

data = []
nome = []
tipo_azienda = []
tipo_impiego = []
principali_mansioni = []
raggio=0

data_formazione = []
nome_formazione = []
materia_studio = []
qualifica = []
punteggio = []
raggio_formazione=0

'''
fine variabili temporali per lavoro e formazione
'''
raggio_lingue=0
nome_lingue = []
lettura_lingue = []
scrittura_lingue = []
orale_lingue =[]

 
inizializzazione_json={
        'lavoro':0,
        'formazione':0,
    }

    
def index(request):
    if request.method != 'POST':

        form = FormInfoPers()
        form1 = FormLavoro(prefix="form0")
        form2 = FormIstruzione()
        form3 = FormLingue()
        form4 = FormRelazionali()
        form5 = FormOrganizzative()
        form6 = FormTecniche()
        form7 = FormArtistiche()
        form8 = FormAltre()
        form9 = FormAltreInfo()


    else:
        form = FormInfoPers(request.POST,request.FILES)

        form1 = FormLavoro(request.POST,prefix="form0")
        


        form2 = FormIstruzione(request.POST)
        form3 = FormLingue(request.POST)
        form4 = FormRelazionali(request.POST)
        form5 = FormOrganizzative(request.POST)
        form6 = FormTecniche(request.POST)
        form7 = FormArtistiche(request.POST)
        form8 = FormAltre(request.POST)
        form9 = FormAltreInfo(request.POST)

        form.id_resume = 0
        form1.id_resume = 0
        form2.id_resume = 0
        form3.id_resume = 0
        form4.id_resume = 0
        form5.id_resume = 0
        form6.id_resume = 0
        form7.id_resume = 0
        form8.id_resume = 0
        form9.id_resume = 0
                
        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid() and form8.is_valid() and form9.is_valid(): 
            
            id_utente=form.save()
            esperienza_lavorativa=form1.save(commit=False)
            istruzione = form2.save(commit=False)
            lingua = form3.save(commit=False)
            relazionali = form4.save(commit=False)
            organizzative = form5.save(commit=False)
            tecniche = form6.save(commit=False)
            artistiche = form7.save(commit=False)
            altre = form8.save(commit=False)
            altre_info = form9.save(commit=False)

            esperienza_lavorativa.id_resume_id = id_utente.id
            global raggio

            for x in range(raggio-1):
                caricare_lavoro_in_database = Esperienza_Lavorativa(id_resume_id=id_utente.id , data_da_a=data[x] , nome_datore=nome[x] , tipo_azienda=tipo_azienda[x] , tipo_impiego=tipo_impiego[x] , principali_mansioni=principali_mansioni[x])
                caricare_lavoro_in_database.save()

            for x in range(raggio_formazione-1):
                caricare_formazione_in_database = Informazione_Istruzione(id_resume_id=id_utente.id , data_da_a=data_formazione[x] , nome_formazione=nome_formazione[x] , materia_studio=materia_studio[x] , qualifica=qualifica[x] , punteggio=punteggio[x] )
                caricare_formazione_in_database.save()

            for x in range(raggio_lingue-1):
                caricare_lingua_in_database = Cap_Lingue(id_resume_id=id_utente.id , nome_lingua=nome_lingue[x] , lettura=lettura_lingue[x] , scrittura=scrittura_lingue[x] ,orale=orale_lingue[x])
                caricare_lingua_in_database.save()

            istruzione.id_resume_id = id_utente.id
            lingua.id_resume_id =id_utente.id
            relazionali.id_resume_id = id_utente.id
            organizzative.id_resume_id = id_utente.id
            tecniche.id_resume_id = id_utente.id
            artistiche.id_resume_id = id_utente.id
            altre.id_resume_id = id_utente.id
            altre_info.id_resume_id = id_utente.id

            relazionali.save()
            organizzative.save()
            tecniche.save()
            artistiche.save()
            lingua.save()
            esperienza_lavorativa.save()
            altre.save()
            altre_info.save()

            istruzione.save()
            return pdf(id_utente.id)
    context = {'form': form,'form1':form1,'form2':form2,'form3':form3,'form4':form4,'form5':form5,'form6':form6,'form7':form7,'form8':form8,'form9':form9}
    return render(request, 'resumes/index.html', context)

def genera(contex,temp_id):
    template= get_template('resumes/compilato.html')
    html =  template.render(contex)
    path_wkthmltopdf = 'wkhtmltopdf/bin/wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    options = {
        'page-size': 'A4',
        'encoding': 'utf-8',
        'margin-top': '0cm',
        'margin-bottom': '0cm',
        'margin-left': '0cm',
        'margin-right': '0cm',
    }
    pdf = pdfkit.from_string(html,False,configuration=config,options=options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename = CV.pdf'
    return response    


def pdf(temp_id):
    informazioni = Informazioni_Personali.objects.get(id=temp_id)
    lavori = informazioni.esperienza_lavorativa_set.all()
    istruzioni= informazioni.informazione_istruzione_set.all()
    lingue = informazioni.cap_lingue_set.all()
    relazionali = Comp_Relazionali.objects.get(id_resume=temp_id)
    organizzative = Comp_Organizzative.objects.get(id_resume=temp_id)
    tecniche = Comp_Tecniche.objects.get(id_resume=temp_id)
    artistiche = Comp_Artistiche.objects.get(id_resume=temp_id)
    altre = Altre_Comp.objects.get(id_resume=temp_id)
    altre_info = Altre_Informa.objects.get(id_resume=temp_id)

    contex = {'info': informazioni,'lavori':lavori,'istruzioni':istruzioni,'lingue':lingue,'relazionali':relazionali,
        'organizzative':organizzative,'tecniche':tecniche,'artistiche':artistiche,'altre':altre,'altre_info':altre_info}
        
    return genera(contex,temp_id)

@ajax
def temp(request):
    richiesta=request.POST
    
    global raggio
    
    raggio = int(richiesta['lavori'])+1

    for x in range(1,raggio):
        
        data.append(richiesta['lista['+ str(x) +'][data]'])
        nome.append(richiesta['lista['+ str(x) +'][nome]'])
        tipo_azienda.append(richiesta['lista['+ str(x) +'][tipo_azienda]'])
        tipo_impiego.append(richiesta['lista['+ str(x) +'][tipo_impiego]'])
        principali_mansioni.append(richiesta['lista['+ str(x) +'][principali_mansioni]'])

    return(nome)

@ajax
def temp_formazione(request):
    richiesta=request.POST

    global raggio_formazione

    raggio_formazione= int(richiesta['formazioni'])+1
    for x in range(1,raggio_formazione):
        data_formazione.append(richiesta['lista['+ str(x) +'][data]'])
        nome_formazione.append(richiesta['lista['+ str(x) +'][nome]'])
        materia_studio.append(richiesta['lista['+ str(x) +'][materia_studio]'])
        qualifica.append(richiesta['lista['+ str(x) +'][qualifica]'])
        punteggio.append(richiesta['lista['+ str(x) +'][punteggio]'])

    return(nome_formazione)

@ajax
def temp_lingue(request):
    richiesta=request.POST

    global raggio_lingue

    raggio_lingue = int(richiesta['lingue'])+1
    for x in range(1,raggio_lingue):
        nome_lingue.append(richiesta['lista['+str(x) +'][nome]'])
        lettura_lingue.append(richiesta['lista['+str(x) +'][lettura]'])
        scrittura_lingue.append(richiesta['lista['+str(x) +'][scrittura]'])
        orale_lingue.append(richiesta['lista['+str(x) +'][orale]'])
    return(nome_lingue)







    
