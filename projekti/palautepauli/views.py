from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import BaseFormView, CreateView
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .models import TalkooPalaute, KokousPalaute, Hairioilmoitus
from .forms import TalkooPalauteForm, KokousPalauteForm, HairioilmoitusForm




#, 't_monivalinta'
class TalkooPalauteView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = TalkooPalauteForm
    model = TalkooPalaute
    template_name = 'palautepauli/TalkooPalaute.html'
    #fields = ['comment']
    success_url = reverse_lazy('palautepauli:index')
    def form_valid(self, form):
        # Set the form's author to the submitter if the form is valid
        form.instance.kayttaja = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


def index(request):
    talkoopalaute = TalkooPalaute.objects.all().order_by('-date')   
    context = {"talkoopalaute": talkoopalaute}
    return render(request, 'palautepauli/index.html', context)




class KokousPalauteView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = KokousPalauteForm
    model = KokousPalaute
    template_name = 'palautepauli/KokousPalaute.html'
    #fields = ['comment']
    success_url = reverse_lazy('palautepauli:index')
    def form_valid(self, form):
        # Set the form's author to the submitter if the form is valid
        form.instance.kayttaja = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


def index(request):
    kokouspalaute = KokousPalaute.objects.all().order_by('-date')  
    context = {"kokouspalaute": kokouspalaute}
    return render(request, 'palautepauli/index.html', context)






class HairioilmoitusView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = HairioilmoitusForm
    model = Hairioilmoitus
    template_name = 'palautepauli/hairioilmoitus.html'
    #fields = ['comment']
    success_url = reverse_lazy('palautepauli:index')
    def form_valid(self, form):
        # Set the form's author to the submitter if the form is valid
        form.instance.kayttaja = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


def index(request):
    ilmoitus = Hairioilmoitus.objects.all().order_by('-date')
    context = {"ilmoitus": ilmoitus}
    return render(request, 'palautepauli/index.html', context)