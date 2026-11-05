from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfume, ImagemPerfume
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def formulario(request):

    if request.method == "POST":

        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        imagem = request.FILES.get("imagem")
        tipo = request.POST.get("tipo")

        # Criar o perfume principal
        perfume = Perfume.objects.create(
            titulo=titulo,
            descricao=descricao,
            imagem=imagem,
            tipo=tipo
        )

        # Receber várias imagens adicionais
        imagens = request.FILES.getlist("imagens")

        # Guardar cada imagem associada ao perfume
        for img in imagens:
            ImagemPerfume.objects.create(
                perfume=perfume,
                imagem=img
            )

        return redirect("catalogo")

    return render(request, "Formulario/Formulario.html")

def catalogo(request):

    perfumes = Perfume.objects.all().order_by("id")

    busca = request.GET.get("q", "")

    if busca:
        perfumes = perfumes.filter(
            Q(titulo__icontains=busca) |
            Q(descricao__icontains=busca)
        )

    paginator = Paginator(perfumes, 12)

    numero = request.GET.get("page")

    pagina = paginator.get_page(numero)

    return render(request, "Catalogo/Catalogo.html", {
        "perfumes": pagina.object_list,
        "pagina": pagina,
        "busca": busca,
    })


def detalhes_perfume(request, id):
    perfume = get_object_or_404(Perfume, id=id)
    imagens = perfume.imagens.all()

    if perfume.tipo == "masculino":
        genero = "Masculino"
    elif perfume.tipo == "feminino":
        genero = "Feminino"
    else:
        genero = "Unissex"

    return render(request, "Detalhes/Detalhes.html", {
        "perfume": perfume,
        "genero": genero,
        "imagens": imagens,
    })



    
    
    
        
