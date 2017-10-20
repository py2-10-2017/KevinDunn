from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

NAME_REGEX = re.compile(r'^[a-zA-Z]{2,30}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^[0-9a-zA-Z!@#$%]{8,40}$')

# Create your models here.
class CourseManager(models.Manager):
    def validate_reg(self, postData):
        errors = {}
        for field, value in postData.iteritems():
            if len(value) < 1:
                errors[field] = "{} field is reqired".format(field.replace('_', ' '))

            if not re.match(NAME_REGEX, postData['first_name']):
                errors["first_name"] = "First name must be more than 2 (letters only)"
            if not re.match(NAME_REGEX, postData['last_name']):
                errors["last_name"] = "Last name must be more than 2 (letters only)"
            if not re.match(EMAIL_REGEX, postData['email']):
                errors["email"] = "Invalid Email"
            if not re.match(PASSWORD_REGEX, postData['password']):
                errors["password"] = "Password needs 8 or more (letters, number and or symbol)"
            if postData["password"] != postData["confirm"]:
                errors["confirm"] = "Password Confirmation doesn't match"

            if not errors:
                hashed = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(5))
                # hashed = bcrypt.hashpw(postData['password'], bcrypt.gensalt())
            user = self.create(
                first_name = postData['first_name'],
                last_name = postData['last_name'],
                email = postData['email'],
                password = hashed
            )
                        
            return errors
            


    def login_val(self, postData):
        errors = []
        
        if len(self.filter(email=postData['email'])) > 0:
            user = self.filter(email=postData['email'])[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors.append('email/password incorrect')
        else:
            errors.append('email/password incorrect')

        if errors:
            return errors
        return user



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    conf = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
    
    def __str__(self):
         return "<Blog object: {} {}>".format(self.first_name, self.last_name)