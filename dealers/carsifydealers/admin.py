from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
admin.site.register(Gumasta)

@admin.register(India_States)
class ViewAdmin(ImportExportModelAdmin):
    pass

#index
@admin.register(Contact, Newsletter)
class ViewAdmin(ImportExportModelAdmin):
    pass


#user details
@admin.register(UserProfile, Address, Address_Type)
class ViewAdmin(ImportExportModelAdmin):
    pass

#car
@admin.register(Car_Company, Car_Model, Car_Fuel, Transmission_Type, Number_of_Owners, Car_Body_Type)
class ViewAdmin(ImportExportModelAdmin):
    pass

#individual car
@admin.register(Individual_Car_Details, UserFavouriteCars, Individual_Car_Images)
class ViewAdmin(ImportExportModelAdmin):
    pass


@admin.register(DealerApplication, Dealer)
class ViewAdmin(ImportExportModelAdmin):
   pass
