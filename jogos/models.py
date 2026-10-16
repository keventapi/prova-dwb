from django.db import models
from django.contrib import admin

# Create your models here.
class Modalidade(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    modalidade_tipo = {
        "COLETIVA": "Coletiva",
        "INDIVIDUAL": "Individual"
    }

    tipo = models.CharField(
        max_length=30,
        choices=modalidade_tipo,
        default=modalidade_tipo["COLETIVA"]
    )

    max_atletas = models.PositiveIntegerField()
    class Meta:
         verbose_name = "modalidade"
         verbose_name_plural = "modalidades"
         ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} do tipo {self.tipo} com a quantidade maxima de atletas {self.max_atletas}"
    


class Equipe(models.Model):
    nome = models.CharField(max_length=50, unique=True) 
    curso = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    criado_em = models.DateTimeField(auto_created=True)
    
    @admin.display
    def quantidade_atletas(self):
        return self.atletas.count()

    class Meta:
        verbose_name = "equipe"
        verbose_name_plural = "equipes"
        ordering = ["nome"]

    def __str__(self):
        return f"equipe {self.nome} do curso {self.curso} da cor {self.cor} foi cadastrado em: {self.criado_em}"

class Tecnico(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=50)
    equipe = models.OneToOneField(Equipe, on_delete=models.CASCADE, related_name="tecnico")
    class Meta:
        verbose_name = "técnico"
        verbose_name_plural = "técnicos"
        ordering = ["nome"]
    def __str__(self):
            return f"tecnico do nome: {self.nome} com o email {self.email} e numero de telefone {self.telefone}"
    

class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50, unique=True)
    data_nascimento = models.DateField()
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name="atletas")
    modalidade = models.ManyToManyField(Modalidade, related_name="atletas")
    class Meta:
        verbose_name = "atleta"
        verbose_name_plural = "atletas"
        ordering = ["nome"]
    def __str__(self):
            return f"atleta do nome: {self.nome} com a matricula {self.matricula} nascido em {self.data_nascimento}"
    

