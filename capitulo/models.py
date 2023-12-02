from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from slugify import slugify


class Capitulo(models.Model):
    class Meta:
        verbose_name = "Capítulo"
        verbose_name_plural = "Capitulos"

    cidade = models.CharField(verbose_name="Cidade", max_length=40)
    uf = models.CharField(verbose_name="UF", max_length=2, choices=STATE_CHOICES)
    pais = models.CharField(verbose_name="País", max_length=30)
    fundacao = models.DateField(verbose_name="Data de Fundação")
    slug = models.SlugField(verbose_name="Idenitifador")

    def __str__(self):
        return f"PyLadies {self.cidade}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.cidade)
        super().save(*args, **kwargs)

    @property
    def numero_de_integrantes(self):
        return len(self.integrantes.all())
    
    @property
    def lista_integrantes(self):
        return self.integrates.all()


class PyLady(models.Model):
    class Meta:
        verbose_name = "PyLady"
        verbose_name_plural = "PyLadies"

    capitulo = models.ForeignKey(
        Capitulo, on_delete=models.SET_NULL, related_name="integrantes", null=True, blank=True
    )
    nome = models.CharField(verbose_name="Nome", max_length=40)
    ingresso = models.DateField(verbose_name="Data de Ingresso", auto_now=True)

    def __str__(self):
        return f"{self.nome} - {str(self.capitulo)}"
