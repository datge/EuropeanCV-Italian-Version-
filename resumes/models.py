from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Informazioni_Personali(models.Model):
    nome = models.CharField(max_length=50)
    indirizzo = models.CharField(max_length=100,blank=True,null=True)
    foto_tessera = models.ImageField(blank=True, null=True,upload_to='profile_image')
    telefono = PhoneNumberField(blank=True,null=True)
    fax = PhoneNumberField(blank=True,null=True)
    email = models.EmailField(max_length=254,blank=True,null=True)
    sito_web = models.URLField(max_length=200,blank=True,null=True)
    nazionalita =models.CharField(max_length=50)
    data_di_nascita =models.DateField(auto_now_add=False)
    madre_lingua = models.CharField(max_length=100)
    patenti =  models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = ("Informazioni Personali")
class Esperienza_Lavorativa(models.Model):
    id_resume = models.ForeignKey(Informazioni_Personali,on_delete=models.CASCADE,blank=True)
    data_da_a = models.CharField(max_length=50,blank=True,null=True)
    nome_datore = models.CharField(max_length=100,blank=True,null=True)
    indirizzo_datore = models.CharField(max_length=100,blank=True,null=True)
    tipo_azienda = models.CharField(max_length=100,blank=True,null=True)
    tipo_impiego = models.CharField(max_length=100,blank=True,null=True)
    principali_mansioni = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return str(self.id_resume)
    
    class Meta:
        verbose_name_plural = ("Esperienze Lavorative")

class Informazione_Istruzione(models.Model):
    id_resume = models.ForeignKey(Informazioni_Personali,on_delete=models.CASCADE,blank=True)
    data_da_a = models.CharField(max_length=50, blank=True, null=True)
    nome_formazione = models.CharField(max_length=100,blank=True,null=True)
    materia_studio = models.CharField(max_length=100,blank=True,null=True)
    qualifica = models.CharField(max_length=100,blank=True,null=True)
    punteggio = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return str(self.id_resume)
    class Meta:
        verbose_name_plural = ("Qualifiche")

class Cap_Lingue(models.Model):
    LIVELLI = (
        ('Elementare','Elementare'),
        ('Buono','Buono'),
        ('Eccellente','Eccellente'),
    )
    id_resume = models.ForeignKey(Informazioni_Personali, on_delete=models.CASCADE,blank=True)
    nome_lingua =  models.CharField(max_length=100,blank=True,null=True)
    lettura = models.CharField(max_length=10, choices=LIVELLI,blank=True,null=True)
    scrittura = models.CharField(max_length=10, choices=LIVELLI,blank=True,null=True)
    orale = models.CharField(max_length=10, choices=LIVELLI,blank=True,null=True)

    def __str__(self):
        return str(self.id_resume)
    class Meta:
        verbose_name_plural  = ("Capacità Linguistiche")


class Comp_Relazionali(models.Model):
    id_resume = models.ForeignKey(Informazioni_Personali, on_delete=models.CASCADE,blank=True)
    descrizione_rela = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return str(self.id_resume)
    class Meta:
        verbose_name_plural = ("Competenze Relazionali")


class Comp_Organizzative(models.Model):
    id_resume = models.ForeignKey(Informazioni_Personali, on_delete=models.CASCADE,blank=True)
    descrizione_orga = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return str(self.id_resume)

    
    class Meta:
        verbose_name_plural = ("Competenze Organizzative")

class Comp_Tecniche(models.Model):
    id_resume = models.ForeignKey(Informazioni_Personali, on_delete=models.CASCADE,blank=True)
    descrizione_tecniche = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return str(self.id_resume)

    
    class Meta:
        verbose_name_plural = ("Competenze Tecniche")

class Comp_Artistiche(models.Model):
    id_resume = models.ForeignKey(Informazioni_Personali, on_delete=models.CASCADE,blank=True)
    descrizione_artistiche = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return str(self.id_resume)

    
    class Meta:
        verbose_name_plural = ("Competenze Artistiche")

class Altre_Comp(models.Model):
    id_resume = models.ForeignKey(Informazioni_Personali, on_delete=models.CASCADE,blank=True)
    descrizione_altre =  models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return str(self.id_resume)
    
    class Meta:
        verbose_name_plural = ("Altre Competenze")

class Altre_Informa(models.Model):
    id_resume = models.ForeignKey(Informazioni_Personali, on_delete=models.CASCADE,blank=True)
    altre_informazioni =  models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return str(self.id_resume)
    
    class Meta:
        verbose_name_plural = ("Altre Informazioni")
