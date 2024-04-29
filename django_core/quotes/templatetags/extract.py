from django import template
from bson.objectid import ObjectId
from django.shortcuts import get_object_or_404

from ..models import Author


register = template.Library()


def get_author(id_):
    author = id_
    return author.fullname


register.filter('author', get_author)
