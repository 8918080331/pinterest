from django.contrib import admin
from app1.models import User,Pin
# Register your models here.





@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ['id', 'pin', 'heading',
                    'tag', 'details', 'pincategory','postedtime','owner']




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username','first_name','last_name', 'email','is_cdc', 'is_teacher', 'is_student','active','profilepic']