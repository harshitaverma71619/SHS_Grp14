from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from LabStaff.models import LabReports
from HospitalStaff.models import AppointmentDetails
import json

# Create your views here.
class labStaffHome(View):
    def get(self, request):
        return render(request, 'labStaffHome.html', {
            'user': 'Harshil'
        })

class viewRequests(View):
    def get(self, request):
        request_details = AppointmentDetails.objects.all()
        # jsonDecoder = json.decoder.JSONDecodeError()
        # for entry in request_details:
        #     if entry.lab_tests != None:
        #         lab_tests = json.loads(entry.lab_tests)
        #         entry.lab_tests = lab_tests
        #     else:
        #         entry.lab_tests = []
        return render(request, 'viewRequests.html', {
            'requests': request_details,
        })

    def post(self,request):
        msgS = ''
        try:
            request_details = AppointmentDetails.objects.all()
            id = int(request.POST.get('approve'))
            for entry in request_details:
                if entry.id == id:
                    lab_report = LabReports(report_id = 1, doctor_id = entry.doctor_id, patient_id = entry.patient_id, lab_staff_id = 1, report_status = "Approved", test_name = entry.lab_tests)
                    lab_report.save()
                    appointment = AppointmentDetails.objects.get(id=entry.id)
                    appointment.report_status = "Approved"
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
