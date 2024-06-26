from django.db import models
from accounts.models import CustomUser

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name="owned_groups"
    )
    users = models.ManyToManyField(CustomUser, related_name="joined_groups")


class Blog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="blogs")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="blogs")
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    image = models.ImageField(upload_to='uploads/')


class Reaction(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="reactions"
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="reactions")
    reaction_code = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True, null=True)


class Comment(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="comments"
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
