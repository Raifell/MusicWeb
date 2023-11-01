from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class MusicGenre(models.Model):
    genre_name = models.CharField('Genre', max_length=50)

    def __str__(self):
        return '{} - {}'.format(self.pk, self.genre_name)

    def get_absolute_url(self):
        return reverse('bands_page', kwargs={'genre': self.genre_name})


class MusicBand(models.Model):
    name = models.CharField('Artist', max_length=100)
    genre = models.ForeignKey(MusicGenre, on_delete=models.DO_NOTHING, verbose_name='Genre')
    year = models.PositiveIntegerField('Year', validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    description = models.TextField('Description')
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify('{}'.format(self.name))
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.genre.genre_name, self.year)

    def get_absolute_url(self):
        return reverse('info_page', kwargs={'genre': self.genre.genre_name, 'slug': self.slug})
