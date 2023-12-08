from django.contrib import admin
from .models import *

class SchoolModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)
    

class SchoolAdsInline(admin.TabularInline):
    model = SchoolAds
    readonly_fields = ('id',)
    extra = 1


class SchoolGalleryInline(admin.TabularInline):
    model = SchoolGallery
    readonly_fields = ('id',)
    extra = 1

class SchoolAcademicInline(admin.TabularInline):
    model = SchoolAcademic
    readonly_fields = ('id',)
    extra = 1
    

class SchoolOpenCloseInline(admin.TabularInline):
    model = OpeningHours
    readonly_fields = ('id',)
    extra = 1

class SchoolFormsInline(admin.TabularInline):
    model = SchoolJoining
    readonly_fields = ('id',)
    extra = 1

class SchoolImageInline(admin.TabularInline):
    model = SchoolImage
    readonly_fields = ('id',)
    extra = 1

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name','region','phone_number1','whatsapp_number','email','location']
    list_filter = ['name', 'region', 'location']
    inlines = [SchoolFormsInline, SchoolImageInline,SchoolAdsInline ,SchoolOpenCloseInline, SchoolGalleryInline]

admin.site.register(Region)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(UserFeedback)
# admin.site.register(School)
# admin.site.register(SchoolImage)

admin.site.site_header = "ShuleZetu Admin"
admin.site.site_title = "ShuleZetu Admin Portal"
admin.site.index_title = "Welcome to ShuleZetu Online Marketplace"