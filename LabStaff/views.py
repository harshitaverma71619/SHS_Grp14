from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from Doctors.models import labTests
from LabStaff.models import LabReports
from HospitalStaff.models import AppointmentDetails
import json
from django.db.models import Q

# Create your views here.
class labStaffHome(View):
    def get(self, request):
        return render(request, 'labStaffHome.html', {
            'user': 'Harshil'
        })

class viewRequests(View):
    def get(self, request):
        request_details = labTests.objects.all()
        return render(request, 'viewRequests.html', {
            'requests': request_details
        })

    def post(self,request):
        msgS = ''
        try:
            request_details = labTests.objects.all()
            appoitment_id = int(request.POST.get('approve'))
            for entry in request_details:
                if entry.appointment_id == appoitment_id:
                    lab_report = LabReports(doctor_id = entry.doctor_id, patient_id = entry.patient_id, patient_diagnosis = entry.patient_diagnosis, lab_staff_id = 1, report_status = "Approved", test_name = entry.lab_test)
                    lab_report.save()
                    appointment = labTests.objects.get(appointment_id=entry.appointment_id)
                    appointment.lab_test_status = "Approved"
                    appointment.save()
                    msgS = "Added Successfully"
                    break
                else:
                    msgE = "Mention Name of the Application Type"
        except:
            print("in except block")
            msgE = "Something went Wrong"
        finally:
            print("in finally block")
            # messages.add_message(request, messages.SUCCESS if msgS else messages.ERROR,
            #                      (msgS if not msgS == '' else msgE),
            #                      extra_tags='callout callout-success calloutCustom lead' if msgS else 'callout callout-danger calloutCustom lead')
            return redirect('/labStaff/viewRequests')
class addLabRecord(View):
    def get(self, request):
        request_details = LabReports.objects.filter(report_status="Approved")
        return render(request, 'labReportPage.html', {
            'requests': request_details
        })
    def post(self,request):
        
        details = str(request.POST.get('details'))
        record_id=request.POST.get('addData')
        
        message=""
        try:
            report_data= LabReports.objects.get(id=record_id)
            report_data.report_info=details
            report_data.report_status="Added"
            report_data.save()    
            message="Added Scuccessfully"
                
        except:
            print("exception while fetching reports")
            message="Exception in fetching Lab Reports"
        finally:
            return redirect('/labStaff/addLabRecord')

class updateLabRecord(View):
    def get(self, request):
        crit=Q(report_status="Added")
        crit1=Q(report_status="Updated")
        request_details = LabReports.objects.filter(crit | crit1 )
       
        return render(request, 'updateReportPage.html', {
            'requests': request_details
        })
    def post(self,request):
        details = str(request.POST.get('details'))
        record_id=request.POST.get('update')
        message=""
        try:
            report_data= LabReports.objects.get(id=record_id)
            report_data.report_info=details
            report_data.report_status="Updated"
            report_data.save()      
            message="Updated Scuccessfully"
        except:
            print("exception while updating  reports")
            message="Exception in fetching Lab Reports"
        finally:
            return redirect('/labStaff/updateLabRecord')


    
class viewLabRecord(View):
    def get(self, request):
        request_details = LabReports.objects.all()
        return render(request, 'viewReportPage.html', {
            'requests': request_details,
        })