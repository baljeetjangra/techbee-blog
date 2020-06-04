from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,auto_now_add=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    