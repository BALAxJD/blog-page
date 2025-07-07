from django.db import models

class BlogPost(models.Model):
    STATUS_CHOICES=[
        ('draft','Draft'),
        ('published','Published')
    ]

    title=models.CharField(max_length=200)
    content=models.TextField()
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
