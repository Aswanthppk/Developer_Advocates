from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Adevactes,Company

class Advactes_Serializer(ModelSerializer):
    class Meta:
        model=Adevactes
        
        fields=['id','name','profile_pic','short_bio','long_bio','advocate_years_exp','company']
class Company_Serializer(ModelSerializer):
    class Meta:
        model=Company
        fields=['id','name','logo','herf']

class Company_Serializer_details(ModelSerializer):
    class Meta:
        model=Company
        fields=['id','name','logo','summery']
class Advactes_compnay_Serializer(ModelSerializer):
    class Meta:
        model=Adevactes
        fields=['id','name','profile_pic','short_bio','long_bio','advocate_years_exp']
class Advacates_image_url_serializer(ModelSerializer):
    class Meta:
        model=Adevactes
        fields=['company','profile_pic']
class Company_logo_serializer(ModelSerializer):
    class Meta:
        model=Company
        fields=['logo']