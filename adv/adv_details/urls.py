from django.urls import path
from . import views



urlpatterns = [
    path('advocates/',views.Index_view,name='index'),
    path('advocates/<int:pk>/',views.details_view,name='details'),
    path('companies/',views.Companey_view,name='companey'),
    path('companies/<int:pk>/',views.Companey_detailview,name='compeny_details')
    
]