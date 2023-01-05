from django.contrib import admin
from .models import Destination,Bus,BookBus

# Register your models here.


admin.site.register(Destination)
admin.site.register(Bus)
admin.site.register(BookBus)