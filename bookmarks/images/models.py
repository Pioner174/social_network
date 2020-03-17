from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.urls import reverse


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    shooting = models.DateField(db_index=True, verbose_name='Shooting date')
    created = models.DateField(auto_now_add=True, db_index=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='images_liked',
                                       blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def clean(self):
        if not self.url and not self.image:
            errors = {NON_FIELD_ERRORS: ValidationError(
                'Должно быть заполнено хотябы одно поле url или image')}
            raise ValidationError(errors)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
