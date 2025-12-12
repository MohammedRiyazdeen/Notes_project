from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.\
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=125)
    slug = models.SlugField(blank=True,null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='unique_category_per_user')
        ]
        #(Older style)
        #unique_together = ('user', 'name')


    def __str__(self):
        return self.name 
    
    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super(Category,self).save(*args, **kwargs)


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='notes', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title




