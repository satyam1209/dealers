import email
from django.db.models.base import Model
from django.db.models.query import RawQuerySet
from django.shortcuts import render, redirect,HttpResponseRedirect,HttpResponse
from django.views.decorators import csrf
from .models import *
from django.contrib.auth.models import User
# from django.contrib.auth import 
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.db.models import Min,Max,Q
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.core.mail import EmailMultiAlternatives
import cv2
import numpy as np
from zipfile import ZipFile
import os
from os.path import basename
from wsgiref.util import FileWrapper
import random
from django.core.paginator import Paginator
from django.contrib.auth.hashers import check_password
from django.forms import forms
from .forms import SignUpForm, LoginForm
from django.contrib import messages
def home(request):
	return render(request, 'carsifydealers/home.html')


def user_login(request):
	if not request.user.is_authenticated:
		if request.method=="POST":
			form= LoginForm(request=request,data=request.POST)
			if form.is_valid():
				uname=form.cleaned_data['username']
				upass=form.cleaned_data['password']
				user=authenticate(username=uname,password=upass)
				if user is not None and user.is_active:
					login(request,user)
					messages.success(request,"Login Successfull !!!")
					return HttpResponseRedirect('/')
		else:
			form=LoginForm()
		return render(request,'carsifydealers/login2.html',{'form':form})
	else:
		return HttpResponseRedirect('/')

	
	

# Signup
def signup(request):
	if request.method=='POST':
		print("posst")
		form=SignUpForm(request.POST)
		print(form)
		# print(request.post.get['gumasta'])
		if form.is_valid():
			print(form)
			user=form.save()
			user.is_active=False
			messages.success(request,"you will get your account registered soon")
			form.save()
	else:
		form=SignUpForm()
	return render(request,'carsifydealers/signup.html',{'form':form})

# Logout
def user_logout(request):
	logout(request)
	messages.success(request,'Logout Successfull')
	return HttpResponseRedirect('/')

def about(request):
	return render(request, 'carsifydealers/about.html')

def contact(request):
	return render(request, 'carsifydealers/contact.html')


def Addcar(request):
    car_company = Car_Company.objects.all()
    car_model = Car_Model.objects.all()
    registeredstate = India_States.objects.all()
    numberofowners = Number_of_Owners.objects.all()
    vehicletype = Car_Body_Type.objects.all()
    tansmission = Transmission_Type.objects.all()
    fueltype = Car_Fuel.objects.all()
    print(car_company)


    if request.method == "POST":
        x = request.POST
        companyname = x['companyname']
        companyobj = Car_Company.objects.get(id=companyname)
        modelidd = x['modelname']
        modelname = Car_Model.objects.get(id=modelidd)
        VehicleNumber = x['VehicleNumber']
        Varient = x['Varient']
        RegisteredStateidd = x['RegisteredState']
        RegisteredState = India_States.objects.get(id=RegisteredStateidd)
        Registeredcity = x['Registeredcity']
        NumberofOwnersidd = x['NumberofOwners']
        NumberofOwners = Number_of_Owners.objects.get(id=NumberofOwnersidd)
        Manufacturing = x['Manufacturing']
        DManufacturing = datetime.date(int(Manufacturing), 1, 1)
        VehicalTypeidd = x['VehicalType']
        VehicalType = Car_Body_Type.objects.get(id=VehicalTypeidd)
        Transmissionidd = x['Transmission']
        Transmission = Transmission_Type.objects.get(id=Transmissionidd)
        Km = x['Km']
        color = x['color']
        FuelTypeidd = x['FuelType']
        FuelType = Car_Fuel.objects.get(id=FuelTypeidd)
        Price = x['Price']
        Insurance = x['Insurance']
        InsuranceType = x['InsuranceType']
        Comment = x['Comment']

        Images = request.FILES.getlist('Images')
        showimage = Images[0]

        #create a vehicle object here
        cid = Individual_Car_Details.objects.create(user=request.user, Company=companyobj, Model=modelname,\
            Registration_State=RegisteredState, Fuel_Type =FuelType, Transmission=Transmission, Owners=NumberofOwners,\
            Body_Type=VehicalType, Date_of_Manufacturing = DManufacturing, Card_Registration_Number=VehicleNumber,\
            Car_Varient=Varient, KM=Km, Color=color, Price=Price, Insurance=Insurance, Insurance_Type=InsuranceType, \
            City=Registeredcity, Discription=Comment, Showimage=showimage)

        #show image handeled
        '''
        imm = cid.Showimage
        img_path = imm.path
        img_name = str(imm)
        new_img = resize_img_show(img_path, img_name)
        cid.Showimage = new_img
        cid.save()
        os.remove(img_path)
        '''

        #creating image objects
        for image in Images:
            photo = Individual_Car_Images.objects.create(carid=cid, Image=image)
            '''
            imm = photo.Image

            img_path = imm.path
            img_name = str(imm)

            new_img = resize_img(img_path, img_name)
            photo.Image = new_img
            photo.save()
            os.remove(img_path)
            '''


        #return success page
        return HttpResponseRedirect('/')



    dic = {'car_company':car_company, 'car_model':car_model, 'registeredstate':registeredstate,\
            'numberofowners': numberofowners, 'vehicletype': vehicletype, 'tansmission':tansmission,\
           'fueltype':fueltype}

    return render(request, 'carsifydealers/addcar.html', dic)

def json_Car_add(request):
    car_company = list(Car_Company.objects.values())

    return JsonResponse({'data':car_company})

def json_Car_model(request, *args, **kwarg):
    selecedted_car = kwarg.get('car')
    obj_models = list(Car_Model.objects.filter(Company_Name=selecedted_car).values())

    return JsonResponse({'data':obj_models})
