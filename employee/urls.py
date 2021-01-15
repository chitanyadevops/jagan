
from django.urls import path, include
from . import views
urlpatterns = [
	path('',views.index,name='index'),
	path('search/<str:firstname>/',views.search,name='search'),
	path('employee/',views.employee_form,name='employee_insert'),
	path('<int:id>/',views.employee_form,name='employee_update'),
	path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
	path('employee/list/',views.employee_list, name='employee_list'),

	
]
