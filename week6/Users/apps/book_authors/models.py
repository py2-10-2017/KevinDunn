from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return "<Book object: {}>".format(self.name)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    notes = models.TextField(default='')
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return "<Author object: {} {}>".format(self.first_name, self.last_name)

    #________________________________________________________________________
# Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby
# Create 5 different authors: Mike, Speros, John, Jadee, Jay
# Add a new field in the authors table called 'notes'.  Make this a TextField.  Successfully create and run the migration files.
# Change the name of the 5th book to C#
# Change the first_name of the 5th author to Ketul
# Assign the first author to the first 2 books
# Assign the second author to the first 3 books
# Assign the third author to the first 4 books
# Assign the fourth author to the first 5 books (or in other words, all the books)
# For the 3rd book, retrieve all the authors
# For the 3rd book, remove the first author
# For the 2nd book, add the 5th author as one of the authors
# Find all the books that the 3rd author is part of
# Find all the books that the 2nd author is part of