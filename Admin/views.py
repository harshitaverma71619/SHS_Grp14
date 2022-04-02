from django import conf
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from Admin.forms import createEmployeeForm
from Admin.models import EmployeeDetails

# Create your views here.
class adminHome(View):
    def get(self, request):
        return render(request, 'adminHome.html', {
            'user': 'Admin'
        })

class viewEmployeeRecords(View):
    def get(self, request):
        employeeDetails = EmployeeDetails.objects.all()
        return render(request, 'viewEmployeeRecords.html', {
            'user': 'Admin',
            'createEmployeeForm': createEmployeeForm,
            'employeeDetails': employeeDetails
        })

class createEmployeeRecords(View):
    def get(self, request):
        employeeDetails = EmployeeDetails.objects.all()
        return render(request, 'createEmployeeRecords.html', {
            'user': 'Admin',
            'createEmployeeForm': createEmployeeForm,
            'employeeDetails': employeeDetails
        })
    def post(self, request):
        msgS = ''
        try:
            form = createEmployeeForm(request.POST)
            if form.is_valid():
                employee_first_name = form.cleaned_data.get('employee_first_name')
                employee_last_name = form.cleaned_data.get('employee_last_name')
                employee_dept = form.cleaned_data.get('employee_dept')
                print("going to save")
                EmployeeObj = EmployeeDetails(employee_first_name = employee_first_name, employee_last_name = employee_last_name, employee_dept = employee_dept)
                EmployeeObj.save()
                print("Saved")
                msgS = "Added Successfully"
            else:
                msgE = "Mention Name of the Application Type"
        except:
            print("in except block")
            msgE = "Something went Wrong"
        finally:
            print("in finally block")
            messages.add_message(request, messages.SUCCESS if msgS else messages.ERROR,
                                    (msgS if not msgS == '' else msgE),
                                    extra_tags='callout callout-success calloutCustom lead' if msgS else 'callout callout-danger calloutCustom lead')
            return redirect('/admin/createEmployeeRecords.html')

class editEmployeeRecords(View):
    def get(self, request):
        employeeDetails = EmployeeDetails.objects.all()
        return render(request, 'editEmployeeRecords.html', {
            'user': 'Admin',
            'createEmployeeForm': createEmployeeForm,
            'employeeDetails': employeeDetails
        })
    def post(self, request):
        msgS = ''
        try:
            form = createEmployeeForm(request.POST)
            if form.is_valid():
                employee_first_name = form.cleaned_data.get('employee_first_name')
                employee_last_name = form.cleaned_data.get('employee_last_name')
                employee_dept = form.cleaned_data.get('employee_dept')
                print("going to save")
                EmployeeObj = EmployeeDetails(employee_first_name = employee_first_name, employee_last_name = employee_last_name, employee_dept = employee_dept)
                EmployeeObj.save()
                print("Saved")
                msgS = "Added Successfully"
            else:
                msgE = "Mention Name of the Application Type"
        except:
            print("in except block")
            msgE = "Something went Wrong"
        finally:
            print("in finally block")
            messages.add_message(request, messages.SUCCESS if msgS else messages.ERROR,
                                    (msgS if not msgS == '' else msgE),
                                    extra_tags='callout callout-success calloutCustom lead' if msgS else 'callout callout-danger calloutCustom lead')
            return redirect('/admin/editEmployeeRecords.html')

class updateEmployeeDetails(View):
    def get(self, request, id):
        flag = 'false'
        print('hello')
        try:
            print("Entered try")
            details = EmployeeDetails.objects.get(employee_id=id)
            print(details)
            details = {'employee_id': details.employee_id,'employee_first_name': details.employee_first_name,'employee_last_name': details.employee_last_name, 'employee_dept': details.employee_dept}
            print(details)
        except:
            print('Error')
        finally:
            return render(request, 'updateEmployeeRecords.html', {'details': details, 'employeeDetailsForm': createEmployeeForm(details), "flag": flag})

    def post(self, request, id):
        msgS=''
        try:
            detail1 = EmployeeDetails.objects.get(employee_id = id)
            detailForm = createEmployeeForm(request.POST)
            print(detailForm.is_valid())
            if detailForm.is_valid():
                print("entered if")
                detail1.employee_first_name = request.POST.get('employee_first_name')
                detail1.employee_last_name = request.POST.get('employee_last_name')
                detail1.employee_dept = request.POST.get('employee_dept')
                detail1.save()
                messages.success(request, 'Employee Details Updated Successfully!')
        except:
            messages.error(request, 'Something Went Wrong!')
        finally:
            flag = 'true'
            print(detail1.employee_id)
            employeeDetails = EmployeeDetails.objects.all()
            print(employeeDetails)
            return redirect('/admin/editEmployeeRecords.html')

class deleteEmployeeRecord(View):
    def get(self, request, id):
        try:
            details = EmployeeDetails.objects.get(employee_id=id)
            details.delete()
        except:
            print('Error')
        finally:
            return redirect('/admin/editEmployeeRecords.html')
    
    def post(self, request):
        pass