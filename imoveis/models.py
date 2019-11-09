from django.db import models

class Imovel(models.Model):


BAIRROS = [
    ('NV','Nova Vista'),
    ('NG','Nova Gameleira'),
    ('OU','Outro: '),
]


class Casa(models.Model):
    quartos = models.IntegerField(default=2, verbose_name='Número de Quartos')
    suites = models.IntegerField(default=1, verbose_name='Número de Suítes')
    salas_estar = models.IntegerField(default=1, verbose_name='Número de Salas de Estar')
    vagas = models.IntegerField(default=1, verbose_name='Número de Vagas na Garagem')
    area = models.FloatField(verbose_name='Área (m2)')
    armario = models.BooleanField(default=False, verbose_name='Possui Armário Embutido?')
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    bairro = models.CharField(max_length=2, choices=BAIRROS, verbose_name='Bairro')
    aluguel = models.FloatField(verbose_name='Valor Total do Aluguel')
    endereco = models.TextField(verbose_name='Rua, Número e Complemento')

class Apartamento(models.Model):
    quartos = models.IntegerField(default=2, verbose_name='Número de Quartos')
    suites = models.IntegerField(default=1, verbose_name='Número de Suítes')
    salas_estar = models.IntegerField(default=1, verbose_name='Número de Salas de Estar')
    vagas = models.IntegerField(default=1, verbose_name='Número de Vagas na Garagem')
    area = models.FloatField(verbose_name='Área (m2)')
    armario = models.BooleanField(default=False, verbose_name='Possui Armário Embutido?')
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    andar = models.IntegerField(default=1, verbose_name='Andar')
    valor = models.FloatField(verbose_name='Valor do Condomínio')
    porteiro = models.BooleanField(default=False, verbose_name='Possui Porteiro 24h?')
    bairro = models.CharField(max_length=2, choices=BAIRROS, verbose_name='Bairro')
    aluguel = models.FloatField(verbose_name='Valor Total do Aluguel')
    endereco = models.TextField(verbose_name='Rua, Número e Complemento')
