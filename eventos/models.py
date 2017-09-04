from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome



class Endereco(models.Model):
	nomeend=models.CharField(max_length=128,blank=False, null=True)
	descricao = models.TextField()



class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    pai = models.CharField(max_length=10)

    def __str__(self):             
        return self.cpf
class Evento(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    sigla = models.TextField()
    realizador = models.ForeignKey(PessoaFisica, related_name='pessoas_fisica', null=True, blank=False)
    endereco = models.ForeignKey(Endereco, related_name='endereco', null=True, blank=False)
    logo = models.TextField()
    numero = models.CharField(max_length=13)
    ano = models.CharField(max_length=4)
    data_de_inicio = models.DateField(blank=True, null=True)
    data_de_fim = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Inscrito(models.Model):
    pessoa = models.ForeignKey(Evento, related_name='evento', null=True, blank=False)
    evento = models.ForeignKey(Pessoa, related_name='pessoa', null=True, blank=False)