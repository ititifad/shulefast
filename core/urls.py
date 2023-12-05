from django.urls import path
from .import views


urlpatterns = [
    path('', views.home,name='home'),
    path('feedback/', views.feedback, name='feedback'),
    path('about-us/', views.about_page, name='about'),
    path('thank-you/', views.thank_you_page, name='thank_you_page'),
    path('region/<int:region_id>/', views.region_cat, name='region-cat'),
    path('category/<int:category_id>/', views.subcat_cat, name='subcat-cat'),
    path('schools/<int:subcategory_id>/', views.school_sub, name='school-sub'),
    path('ad/<int:id>/', views.school_ad, name='school_ad'),
    path('<slug:slug>/', views.school, name='school_detail'),
]
