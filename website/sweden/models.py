
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Token(models.Model):
    slug = models.SlugField()
    token_name = models.CharField(max_length=100, unique=True)
    meta_title = models.CharField(max_length=500, blank=True)
    meta_description = models.TextField(max_length=500, blank=True)
    article_title = models.CharField(max_length=100, blank=True)
    content = RichTextUploadingField(blank=True, null=True)
    logo = models.ImageField(upload_to='token', blank=True)
    ticket_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited = models.CharField(max_length=100, blank=True)
    cover_image = models.ImageField(upload_to='token', blank=True)

    def __str__(self):
        return '{}'.format(
            self.token_name
        )

    def get_absolute_url(self):
        return '/{}'.format(
            self.token_name
        )