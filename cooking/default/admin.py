from django.contrib import admin
from .models import *

# Register your models here.
#Jon 123

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(cooking_recipe, BookAdmin)
admin.site.register(Ingredient, BookAdmin)
admin.site.register(Direction, BookAdmin)