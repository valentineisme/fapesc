from django.contrib import admin
from fapesc.models import relacao,restricao,objeto,usuario,casos

admin.site.register(relacao)
admin.site.register(restricao)
admin.site.register(objeto)
admin.site.register(usuario)
#admin.site.register(historico)
#admin.site.register(comunidade)
#admin.site.register(imagem)
admin.site.register(casos)

# Register your models here.
