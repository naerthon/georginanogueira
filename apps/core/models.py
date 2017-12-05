from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from django.core.validators   import MaxValueValidator,MinValueValidator,MinLengthValidator
from django.template.defaultfilters import slugify


class Images(models.Model):
    def image_path(self, filename):
        return 'images/{}/'.format(filename)

    def image_thumb_path(self, filename):
        return 'thumbnail/{}/'.format(filename)

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    desc = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to=image_path)
    image_thumbnail = ProcessedImageField(
        upload_to=image_thumb_path,
        processors=[ResizeToFill(319, 200)],
        format='JPEG',
        options={'quality': 80},
    )
    created_by = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        self.image_thumbnail = self.image
        super(Images, self).save(*args, **kwargs)

    def save_slug(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Images, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerias"

    def __str__(self):
        return self.title

class Colecoes(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    desc = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    galery = models.ManyToManyField(Images)
    created_by = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Colecoes, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Coleção"
        verbose_name_plural = "Coleções"

    def __str__(self):
        return self.title

class ElasUsam(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    galery = models.ManyToManyField(Images)
    created_by = models.ForeignKey(User)
    slug = models.SlugField()
        
    class Meta:
        verbose_name = "Elas Usam"
        verbose_name_plural = "Elas Usam"

    def __str__(self):
        return self.title

class Eventos(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    date = models.DateTimeField(blank=True, null=True)
    galery = models.ManyToManyField(Images)
    created_by = models.ForeignKey(User)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Eventos, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.title

class Email(models.Model):
    full_name = models.CharField(max_length=100)
    ddd = models.IntegerField(validators=[MinValueValidator(10, message="Certifique-se que este valor possui 2 digitos."),MaxValueValidator(99)],verbose_name="DDD")
    phone = models.IntegerField(validators=[MaxValueValidator(999999999)],verbose_name='Telefone')
    message = models.TextField()
    send_date = models.DateTimeField(default=timezone.now)
    email = models.EmailField()

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Email"

    def __str__(self):
        return self.full_name