from __future__ import unicode_literals

from django.db import models

import re
import bcrypt

NAME_REGEX = re.compile(r'^[a-zA-Z]{2,30}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^[0-9a-zA-Z!@#$%]{8,40}$')

# Create your models here.
class UserManager(models.Manager):
    def validate_reg(self, postData):
        errors = []

        if not re.match(NAME_REGEX, postData['alias']):
            errors.append("Alias name must be more than 2 (letters only)")
        if not re.match(NAME_REGEX, postData['first_name']):
            errors.append("First name must be more than 2 (letters only)")
        if not re.match(NAME_REGEX, postData['last_name']):
            errors.append("Last name must be more than 2 (letters only)")
        if not re.match(EMAIL_REGEX, postData['email']):
            errors.append("Invalid Email")
        if not re.match(PASSWORD_REGEX, postData['password']):
            errors.append("Password needs 8 or more (letters and numbers, and or symbol)")
        if postData["password"] != postData["confirm"]:
            errors.append("Password Confirmation doesn't match")

        if not errors:
            hashed = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(14))
            new_user = self.create(
                alias = postData['alias'],
                first_name = postData['first_name'],
                last_name = postData['last_name'],
                email = postData['email'],
                password = hashed
            )
            return new_user
                    
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
    alias = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    def __str__(self):
         return "<User object: {} {}>".format(self.first_name, self.last_name)





class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return "<Author object: {}>".format(self.name)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return "<Book object: {}>".format(self.title)


class ReviewManager(models.Manager):
    def validate_review(self, postData):
        errors = []

        if len(postData['title']) < 1:
            errors.append("Can't leave Title empty")
        if not "author" in postData and len(postData['new_author']) < 3:
            errors.append('new author names must 3 or more characters')
        if "author" in postData and len(postData['new_author']) > 0 and len(postData['new_author']) < 3:
            errors.append('new author names must 3 or more characters')
        if len(postData['review']) < 1:
            errors.append('Review should not be left empty')
        if not int(postData['rating']) > 0 or not int(postData['rating']) <= 5:
            errors.append('invalid rating')
        return errors

        
        
    def create_review(self, clean_data, user_id):
        # retrieve or create author
        the_author = None
        if len(clean_data['new_author']) < 1:
            the_author = Author.objects.get(id=int(clean_data['author']))
        else:
            the_author = Author.objects.create(name=clean_data['new_author'])
        # retrieve or create book
        the_book = None
        if not Book.objects.filter(title=clean_data['title']):
            the_book = Book.objects.create(
                title=clean_data['title'], author=the_author
            )
        else:
            the_book = Book.objects.get(title=clean_data['title'])
            # returns  Review object
            return self.create(
                comment = clean_data['review'],
                rating = clean_data['rating'],
                book = the_book,
                user = User.objects.get(id=user_id)
            )



    def recent_and_not(self):
        '''
        returns a tuple with the zeroeth index containing query for 3 most recent reviews, and the first index
        containing the rest
        '''
        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])
    
    

class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

    def __str__(self):
         return "<Book: {}, Review: {}>".format(self.book.title, self.comment)
