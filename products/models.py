from django.db import models


class Product(models.Model):
    DISPONIVEL_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    nome = models.CharField('Nome' ,max_length=255)
    descricao = models.TextField('Descrição')
    valor = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    disponivel = models.CharField('Disponível', max_length=3, choices=DISPONIVEL_CHOICES)

    def __str__(self):
        return self.nome
      
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['valor']