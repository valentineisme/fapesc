from django.db import models
from django.contrib.auth.models import User


class relacao(models.Model):
    nome = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Relacao'
        verbose_name_plural = 'Relacoes'

    def __str__(self):
        return self.nome


class restricao(models.Model):
    descricao = models.CharField(max_length=128)
    distancia = models.IntegerField()

    class Meta:
        verbose_name = 'Restricao'
        verbose_name_plural = 'Restricoes'

    def __str__(self):
        return self.descricao


class objeto(models.Model):
    nome = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Objeto'
        verbose_name_plural = 'Objetos'

    def __str__(self):
        return self.nome


class usuario(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, editable=False)
    nome = models.CharField(max_length=128)
    sobrenome = models.CharField(max_length=128)
    dataNasc = models.DateField(blank=True, null=True)
    rua = models.CharField(max_length=128)
    numero = models.IntegerField(default=0)
    bairro = models.CharField(max_length=128)
    cidade = models.CharField(max_length=128)
    estado = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    senha = models.CharField(max_length=128, null=True)
    formacao = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def save(self):
        if not self.id:
            c = usuario.objects.filter(email=self.email).count()
            if c:
                raise Exception("Email Existente")

            usr = User.objects.filter(username=self.email)
            if usr:
                u = usr[0]
            else:
                u = User.objects.create_user(self.email, self.email, self.senha)
            u.save()
            self.user = u
        else:
            self.user.username = self.email
            self.user.email = self.email
            self.user.set_password(self.senha)
            self.user.save()

        super(usuario, self).save()

    def __str__(self):
        return self.nome


# class comunidade(models.Model):
#     nome = models.CharField(max_length=128)
#     bairro = models.CharField(max_length=128)
#     cidade = models.CharField(max_length=128)
#     estado = models.CharField(max_length=128)
#     teste = models.CharField(max_length=128)
#
#
#     class Meta:
#         verbose_name = 'Comunidade'
#         verbose_name_plural = 'Comunidades'
#
#     def __str__(self):
#         return (self.nome)
#
#
# class imagem(models.Model):
#     comunidade = models.ForeignKey(comunidade)
#     imagem = models.FileField(upload_to='static/', blank=True)
#     dataImagem = models.DateField(blank=True)
#     latitude = models.CharField(max_length=128)
#     longitude = models.CharField(max_length=128)
#
#     class Meta:
#         verbose_name = 'Imagem'
#         verbose_name_plural = 'Imagens'
#
#     def __str__(self):
#         return str(self.comunidade)


# class historico(models.Model):
#     usuario = models.ForeignKey(usuario)
#     imagem = models.ForeignKey(imagem)
#     data = models.DateField(blank=True)
#     objeto1 = models.CharField(max_length=128)
#     relacao = models.CharField(max_length=128)
#     objeto2 = models.CharField(max_length=128)
#     distancia = models.IntegerField(default=0)
#     resultado = models.CharField(max_length=128)
#     plano_acao = models.CharField(max_length=128)
#
#
#     class Meta:
#         verbose_name = 'Historico'
#         verbose_name_plural = 'Historico'
#
#     def __str__(self):
#         return self.plano_acao


class casos(models.Model):
    objeto1 = models.CharField(max_length=128)
    relacao = models.ForeignKey(relacao)
    objeto2 = models.CharField(max_length=128)
    distancia = models.IntegerField(default=0)
    restricao = models.ForeignKey(restricao)
    resultado = models.CharField(max_length=128)
    plano_acao = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Caso'
        verbose_name_plural = 'Casos'

    def __str__(self):
        return (self.resultado)

# Create your models here.
