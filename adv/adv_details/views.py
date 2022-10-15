from http.client import HTTPResponse
from operator import truediv
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import Advactes_Serializer, Advactes_compnay_Serializer, Company_Serializer,Company_Serializer_details
from .models import Adevactes,Company

# Create your views here.
@api_view(['GET'])
def Index_view(request):
    sample = Adevactes.objects.all()
    
    url=sample[0].profile_pic.url
    print(url)
    twitter=Adevactes.objects.values_list('twitter',flat=True)
    github=Adevactes.objects.values_list('github',flat=True)
    print(sample.values_list('company'))
    serializer=Advactes_Serializer(sample,many=True)
    company=Company.objects.filter(id=serializer.data[0]['company'])
    print(company)
    for data in serializer.data:
        data['profile_pic']='https://developeradvocates-production.up.railway.app{}'.format(data['profile_pic'])
        company_id=data['company']
        youtube=Adevactes.objects.filter(id=data['id'])
        #print(data['profile_pic'].url)
        company_serializer=Company_Serializer(Company.objects.filter(id=data['company']),many=True)
        print(data['id'])
        data['company']=company_serializer.data[0]
        data['company']['logo']='https://developeradvocates-production.up.railway.app/{}'.format(data['company']['logo'])
        data['company']['herf']='https://developeradvocates-production.up.railway.app/companies/{}'.format(company_id)
        data['links']={'youtube':youtube.values_list('youtube',flat=True)[0],'twitter':youtube.values_list('twitter',flat=True)[0],'github':youtube.values_list('github',flat=True)[0]}

        

    return Response(serializer.data)

@api_view(['GET'])
def details_view(request,pk):
    adv=Adevactes.objects.filter(id=pk)
    serializer=Advactes_Serializer(adv,many=True)
    company=Company.objects.filter(id=serializer.data[0]['company'])
    for data in serializer.data:
        data['profile_pic']='https://developeradvocates-production.up.railway.app{}'.format(data['profile_pic'])
        youtube=Adevactes.objects.filter(id=data['id'])
        company_id=data['company']
        print(youtube.values('youtube'))
        company_serializer=Company_Serializer(Company.objects.filter(id=data['company']),many=True)
        #print(company_serializer.data[0]['herf'])
        data['company']=company_serializer.data[0]
        data['company']['logo']='https://developeradvocates-production.up.railway.app/{}'.format(data['company']['logo'])
        data['company']['herf']='https://developeradvocates-production.up.railway.app/companies/{}'.format(company_id)
        data['links']={'youtube':youtube.values_list('youtube',flat=True)[0],'twitter':youtube.values_list('twitter',flat=True)[0],'github':youtube.values_list('github',flat=True)[0]}

        

    return Response(serializer.data[0])
@api_view(['GET'])
def Companey_view(request):
    companey=Company.objects.all()
    
    print(companey.values())
    serializer=Company_Serializer_details(companey,many=True)
    for data in serializer.data:
        data['logo']='https://developeradvocates-production.up.railway.app/{}'.format(data['logo'])
        adv=Adevactes.objects.filter(company=data['id'])
        adv_serializer=Advactes_compnay_Serializer(adv,many=True)
        data['Advacates']=adv_serializer.data[0]
        data['Advacates']['profile_pic']='https://developeradvocates-production.up.railway.app{}'.format(data['Advacates']['profile_pic'])
    
    return Response(serializer.data)
@api_view(['GET'])
def Companey_detailview(request,pk):

    companey= Company.objects.filter(id=pk)
    serializer=Company_Serializer_details(companey,many=True)
    for data in serializer.data:
        data['logo']='https://developeradvocates-production.up.railway.app/{}'.format(data['logo'])
        adv=Adevactes.objects.filter(company=data['id'])
        adv_serializer=Advactes_compnay_Serializer(adv,many=True)
        data['Advacates']=adv_serializer.data[0]
        data['Advacates']['profile_pic']='https://developeradvocates-production.up.railway.app{}'.format(data['Advacates']['profile_pic'])
    
    return Response(serializer.data[0])


    