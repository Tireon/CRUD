from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = "lastname","firstname","post", "data", "email", "number", "status"

admin.site.register(Member, MemberAdmin)