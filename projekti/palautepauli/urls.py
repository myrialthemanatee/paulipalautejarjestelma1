from django.urls import path

from . import views

app_name = 'palautepauli'
urlpatterns = [
    path('', views.index, name='index'),
    path('talkoopalaute', views.TalkooPalauteView.as_view(), name='talkoopalaute'),
    path('kokouspalaute', views.KokousPalauteView.as_view(), name='kokouspalaute'),
    path('hairioilmoitus', views.HairioilmoitusView.as_view(), name='hairioilmoitus'),
]