from django.contrib import admin
from .models import Grocery,Kitchen,Snack,History

admin.site.register(History)
admin.site.register(Grocery)
admin.site.register(Kitchen)
admin.site.register(Snack)