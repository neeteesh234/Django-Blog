from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    Categories_name = models.CharField(max_length = 100, unique=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
 
 
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.Categories_name   

STATUS_CHOICES = (
    (0, 'Draft'),
    (1, 'Published'),
)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, null=True)
    short_description = models.TextField(max_length=300)
    blog_Body = models.TextField(max_length=5000)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.title