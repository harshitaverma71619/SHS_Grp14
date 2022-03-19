from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from HospitalStaff.models import AppointmentDetails
from .forms import *
from django.contrib import messages
from django.utils.decorators import method_decorator


class patientHome(View):
    def get(self,request):
        return render(request,'patientHome.html',{
            'user':'aish'
        })

   
        

class bookAppointment(View):
    def get(self,request):
        appDetails = AppointmentDetails.objects.all()
        return render(request,'bookAppointment.html',{
            'user':'aish',
            'appointmentForm': appointmentForm,
            'appDetails': appDetails,
        })
    def post(self,request):
        msgS = ''
        try:
            form = appointmentForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                requested_date = form.cleaned_data.get('requested_date')
                appointment_with = form.cleaned_data.get('appointment_with')
                print("going to save")
                AppointmentObj = AppointmentDetails( appointment_id=1,patient_id=2,first_name=first_name,last_name=last_name,
                                            appointment_with=appointment_with,requested_date=requested_date)
                AppointmentObj.save()
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
            return redirect('/patient/bookAppointment')


class updateAppointment(View):
    def get(self, request, id):
        try:
            detail = AppointmentDetails.objects.get(id=id)
            detail = {'appointment_id': detail.appointment_id,'patient_id': detail.patient_id,'first_name': detail.first_name,'last_name': detail.last_name,
                        'appointment_with': detail.appointment_with,'requested_date': detail.requested_date}
        finally:
            return render(request, 'updateAppointment.html', {               
                'appointmentForm': appointmentForm(detail),             
            })
    def post(self, request, id):
        msgS=''
        try:
            # try:
            #     id = signing.loads(id)
            # except:
            #     raise Http404
            detail = AppointmentDetails.objects.get(id=id)
            # client_persons=client_person.objects.filter(client_id=id)
            detailForm = appointmentForm(request.POST)
            if detailForm.is_valid():
                # detail.first_name = escapeXSS(str(request.POST.get('first_name')))
                # detail.first_name = escapeXSS(str(request.POST.get('address')))
                # detail.first_name = signing.loads(request.POST.get('sector'))
                # detail.first_name = signing.loads(request.POST.get('under_ministry'))
                detail.first_name = request.POST.get('first_name')
                detail.last_name = request.POST.get('last_name')
                detail.appointment_with = request.POST.get('appointment_with')
                detail.requested_date = request.POST.get('requested_date')
                detail.save()
            msgS="Updated Successfully"
        except:
            msgE="Something Went Wrong"
        finally:
            # id = signing.dumps(id)
            messages.add_message(request, messages.SUCCESS if msgS else messages.ERROR, (msgS if not msgS == '' else msgE),
                                 extra_tags='callout callout-success calloutCustom lead' if msgS else 'callout callout-danger calloutCustom lead')
            return HttpResponseRedirect(reverse('patient:updateAppointment', args=[id]))
