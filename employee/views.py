from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from tablib import Dataset

#pagination
def index(request):
	employee_list = Employee.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(employee_list, 2)
	try:
		employees = paginator.page(page)
	except PageNotAnInteger:
		employees = paginator.page(1)
	except EmptyPage:
		employees = paginator.page(paginator.num_pages)

	return render(request, 'index.html/', { 'employees': employees })

#search


def search(request):

	q = request.GET.get('q')
	employee_list= Employee.objects.values_list('firstname', flat=True)

	if q:
		employees = employee_list.search().query("match", title=q)
	else:
		employees = ''

	return render(request, 'search.html', {'employees': employees})

# Create your views here.
def employee_list(request):
	context={'employee_list':Employee.objects.all()}
	return render(request,'employee_list.html', context)


def employee_form(request, id=0):
	if request.method == "GET":
		if id == 0:
			form = EmployeeForm()
		else:
			employee = Employee.objects.get(pk=id)
			form = EmployeeForm(instance=employee)
		return render(request, "employee_form.html", {'form':form})
	else:
		if id == 0:
			form = EmployeeForm(request.POST)
		else:
			employee = Employee.objects.get(pk=id)
			form = EmployeeForm(request.POST,instance= employee)
		if form.is_valid():
			form.save()
		return redirect('list/')


def employee_delete(request,id):
	employee = Employee.objects.get(pk=id)
	employee.delete()
	return redirect('/employee/list/')


#export to excel
def export(request):
	employee_resource= EmployeeResource()
	dataset= employee_resource.export()
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition']= 'attachment; filename="employee.xls"'
	return response


#export to csv
def export(request):
	employee_resource= EmployeeResource()
	dataset= employee_resource.export()
	response = HttpResponse(dataset.csv, content_type='application/csv')
	response['Content-Disposition']= 'attachment; filename="employee.csv"'
	return response
#import dataset
def simple_upload(request):
	if request.method == 'POST':
		file_format = request.POST['file_format']
		employee_resource=EmployeeResource()
		dataset = Dataset()
		new_employees = request.FILES['myfile']
		if file_format == 'CSV':
			imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
			result = employee_resource.import_data(dataset, dry_run=True)
			
		if file_format == 'xlsx':
			imported_data = dataset.load(new_employees.read().decode('utf-8'),format='xlsx')
			result = employee_resource.import_data(dataset, dry_run=True)

		if not result.has_errors():
			employee_resource.import_data(dataset, dry_run=False)  # Actually import now

	return render(request, 'import.html')


