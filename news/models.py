from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.SlugField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=255)
    amount_of_upvotes = models.IntegerField(default=0)
    

    class Meta:
        ordering = ('-creation_date',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255)
    content = models.TextField()