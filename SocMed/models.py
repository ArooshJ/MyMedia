from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    # posts = models.ManyToManyField(Post)
    Followers = models.ManyToManyField('self',symmetrical=False, blank=True,null=True,related_name='Following')
    # Following= models.ManyToManyField('self',blank=True,null=True)

    dp = models.CharField(max_length=1000, blank=True,null=True)
    Bio = models.CharField(max_length=1000, blank=True,null=True)
    Name = models.CharField(max_length=100, blank=True,null=True)
    
    def __str__(self):
        return self.user.username

    
class Post(models.Model):
    content = models.TextField(null =True, blank=True)
    link = models.CharField(max_length=1000, null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    by = models.ForeignKey(Account, on_delete=models.CASCADE,null=True,blank=True)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)
    AccountsLiked = models.ManyToManyField(Account, null=True,blank=True,related_name='likedPosts')

  


    def __str__(self) :
        return f"{self.by}: \n {self.content[0:50]}"
    
class Comment(models.Model):
    for_Post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    by = models.ForeignKey(Account, on_delete=models.CASCADE,null=True,blank=True)
    likes = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)
    AccountsLiked = models.ManyToManyField(Account, null=True,blank=True,related_name= 'likedComments')

    def __str__(self) :
        return f"{self.by}\n {self.content[0:30]}"
    
class Reply(models.Model):

    for_Comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    content = models.TextField(null=True,blank=True)
    by = models.ForeignKey(Account, on_delete=models.CASCADE,null=True,blank=True,related_name= 'likedReplies')
    likes = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)
    AccountsLiked = models.ManyToManyField(Account, null=True,blank=True)


    def __str__(self) :
        return f"{self.by}\n {self.content[0:30]}"
    
    
    


