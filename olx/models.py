from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length = 30)
    user_phone = models.BigIntegerField()

    def __unicode__(self):
        return self.user_name

class Post(models.Model):
    post_created = models.DateField()
    post_description = models.CharField(max_length = 100)
    is_sold = models.BooleanField(default = True)
    post_user = models.ForeignKey(User)

    # def __unicode__(self):
    #     return self.post_description

