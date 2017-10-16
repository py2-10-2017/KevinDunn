from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.Charfield(max_lengh=255)
    state = models.Charfield(max_lengh=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return "<Blog object: {} {} {}>".format(self.name, self.city, self.state)

