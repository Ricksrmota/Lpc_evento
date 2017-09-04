from django.contrib import admin
from eventos.models import Pessoa
from eventos.models import PessoaFisica
from eventos.models import Evento
from eventos.models import Inscrito
from eventos.models import Endereco



admin.site.register(Pessoa)
admin.site.register(PessoaFisica)
admin.site.register(Evento)
admin.site.register(Inscrito)
admin.site.register(Endereco)

# Register your models here.
