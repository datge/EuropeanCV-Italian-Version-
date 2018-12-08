from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



from . import views


app_name='resumes'

urlpatterns = [
    path('',views.index,name='index'),
    path('temp/',views.temp,name='temp'),
    path('temp_formazione/',views.temp_formazione,name='temp_formazione'),
    path('temp_lingue/',views.temp_lingue,name='temp_lingue'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)