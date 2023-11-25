from django.shortcuts import render, get_object_or_404
from .models import Usuario

def inicio(request):
   
    return render(request,'usuario.html',{'usuario':Usuario})

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    usuarios = { 
        'usuarios': Usuario.objects.all() 
    }
        

    return render(request,'usuarios.html',usuarios)

    