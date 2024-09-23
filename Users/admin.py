from django.contrib.auth.models import Group
from django.contrib import admin

# Desregistrar el modelo Group
admin.site.unregister(Group)
