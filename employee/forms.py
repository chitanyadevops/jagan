from django import forms
from .models import Employee

class DateInput(forms.DateInput):
	input_type='date'
class EmployeeForm(forms.ModelForm):
	class Meta:
		model= Employee
		fields = ('firstname','lastname','departmentid','designation','salary','phone_number','join_date')
		widgets = {'join_date':DateInput()}
		labels={
		    'firstname':'First Name',
		    'lastname':'Last Name',
		    'departmentid':'Department name',
		    'designation':'Designation',
		    'salary':'salary',
		    'phone_number':'Phone Number',
		    'join_date':'Join Date'

		}

	def __init__(self, *args, **kwargs):
		super(EmployeeForm,self).__init__(*args, **kwargs)
		self.fields['departmentid'].empty_label="select"
		self.fields['designation'].required=False
		self.fields['join_date'].required=False





