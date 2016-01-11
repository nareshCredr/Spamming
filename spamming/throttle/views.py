from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import userform
from .models import user
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class UserView(CreateView):
    form_class = userform
    context_object_name = 'form'
    template_name = 'login.html'
    model = user
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        super(UserView,self).form_invalid(form)
        return HttpResponse("Failed")