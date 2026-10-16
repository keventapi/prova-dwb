from django.shortcuts import render, get_object_or_404
from .models import Equipe, Modalidade
# Create your views here.
def home(req):
    equipes = Equipe.objects.all()
    modalidades = Modalidade.objects.all()
    return render(req, "jogos/index.html", {"equipes": equipes, "modalidades": modalidades})

def equipe(req, id):
    equipe_obj = get_object_or_404(Equipe, id=id)
    return render(req, "jogos/equipe.html", {"equipe": equipe_obj})

def modalidade(req, id):
    modalidade_obj = get_object_or_404(Modalidade, id=id)
    return render(req, "jogos/modalidade.html", {"modalidade": modalidade_obj})