
from django.db import models

class Perfume(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='perfumes/')

    TIPOS_PERFUME = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('unissex', 'Unissex'),
    ]

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS_PERFUME,
        default='unissex'
    )

    def __str__(self):
        return self.titulo

    
class ImagemPerfume(models.Model):
    perfume = models.ForeignKey(
        Perfume,
        on_delete=models.CASCADE,
        related_name="imagens"
    )

    imagem = models.ImageField(upload_to="perfumes/")

    def __str__(self):
        return f"Imagem de {self.perfume.titulo}"


    

