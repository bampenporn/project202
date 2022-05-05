from django.contrib import admin
from myapp.models import Car,Client,Rent

class CarAdmin(admin.ModelAdmin):
    list_display = ['maker','model','price','color','date']

admin.site.register(Car,CarAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','address','postcode','email','phone']

admin.site.register(Client,ClientAdmin)

class RentAdmin(admin.ModelAdmin):
    list_display = ['rent_date','return_date','cost','car','client']
    list_editable = ['return_date','cost']

admin.site.register(Rent,RentAdmin)