from django.db import models
from unidecode import unidecode
from django.template.defaultfilters import slugify
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Store(models.Model):
    title = models.CharField(max_length=100, verbose_name='магазин', unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='store_image/%Y/%m/', blank=True)
    image_store = ImageSpecField(source='image',
                                processors=[ResizeToFill(82.5, 82.5)],
                                format='JPEG',
                                options={'quality': 50})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Store, self).save()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:posts_by_category', args=[self.slug])

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

