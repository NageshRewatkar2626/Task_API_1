from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View
from t1.models import EmployeeModel
from django.contrib import messages
# from django.db.utils import IntegrityError
from rest_framework import viewsets
from .serializers import EmployeeSerializer

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all().order_by('name')
    serializer_class = EmployeeSerializer
class EmpDetails(View):
	def post(self,request):
		e_name	= request.POST.get('e1')
		e_cno	= request.POST.get('e2')
		e_email	= request.POST.get('e3')
		e_pwd	= request.POST.get('e4')

		print(e_name,e_cno,e_email,e_pwd)
		EmployeeModel(name=e_name,contact_no=e_cno,email=e_email,password=e_pwd).save()
		messages.success(request,"Registered Successfully")
		return redirect('main')

# calling this below fn through js
@method_decorator(csrf_exempt,name='dispatch')
def check(request):
	n=request.POST.get('cname')
	try:
		EmployeeModel.objects.get(name=n)
		res = {"error":"Name is present already"}
	except EmployeeModel.DoesNotExist:
		res = {"msg":"Name is Available"}
	return JsonResponse(res)


# calling this below fn through js
@method_decorator(csrf_exempt,name='dispatch')
def checkcontact(request):
	cno=request.POST.get('contact')
	try:
		EmployeeModel.objects.get(contact_no=cno)
		res = {"error":"Contact is present already"}
	except EmployeeModel.DoesNotExist:
		res = {"msg":"Contact is Available"}
	return JsonResponse(res)


# calling this below fn through js
@method_decorator(csrf_exempt,name='dispatch')
def checkemail(request):
	cno=request.POST.get('email')
	try:
		EmployeeModel.objects.get(email=cno)
		res = {"error":"Email is present already"}
	except EmployeeModel.DoesNotExist:
		res = {"msg":"Email is Available"}
	return JsonResponse(res)

def login_page(request):
	us	=request.POST.get('u1')
	ps	=request.POST.get('p1')
	try:                                      
		result = EmployeeModel.objects.get(email=us,password=ps)
		return render(request,'login_page.html',{'data':result,'d':EmployeeModel.objects.all()})

	except EmployeeModel.DoesNotExist:
		messages.error(request,'Invalid Employee')
		return redirect('main')
	