""" apps/polyglotte/admin.py """

from django.contrib import admin
from .models import Verse

admin.site.register(Verse)
