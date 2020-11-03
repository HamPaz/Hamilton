import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
#from django.template import loader
from .models import Pergs, Escol

def get_queryset(self):
    return Pergs.objects.filter(dat_publ__lte=timezone.now()).order_by('-dat_publ')[:5]

def index(request):
    ult_list_pergs = Pergs.objects.order_by('-dat_publ')[:5]
    context = {'ult_list_pergs': ult_list_pergs}
    return render(request, 'enque/index.html', context)

def detail(request, pergs_id):
    try:
        pergunta = Pergs.objects.get(pk=pergs_id)
    except Pergs.DoesNotExist:
        raise Http404("Pergunta não existe.")
    return render(request, 'enque/detail.html', {'pergs': pergunta})

def results(request, pergs_id):
    pergunta = get_object_or_404(Pergs, pk=pergs_id)
    return render(request, 'enque/results.html', {'pergs': pergunta})

def vote(request, pergs_id):
    pergunta = get_object_or_404(Pergs, pk=pergs_id)
    try:
        selected_escol = pergunta.escol_set.get(pk=request.POST['escolha'])
    except (KeyError, Escol.DoesNotExist):
        return render(request, 'enque/detail.html', {
            'pergs': pergunta,
            'error_message': "Por favor, escolha uma opção.",
        })
    else:
        selected_escol.int_votos += 1
        selected_escol.save()
        return HttpResponseRedirect(reverse('enque:results', args=(pergunta.id,)))











