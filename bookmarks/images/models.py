from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    shooting = models.DateField(db_index=True, verbose_name='Shooting date')
    private = models.BooleanField(default=False, verbose_name='Видна всем')
    created = models.DateField(auto_now_add=True, db_index=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='images_liked',
                                       blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.encode("UTF-8"))
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:image', args=[self.id, self.slug])
