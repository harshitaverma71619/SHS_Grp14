from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from HospitalStaff.models import AppointmentDetails
from InsuranceStaff.models import InsuranceClaimDetails
from .forms import *
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import logout

def logout_view(request):
     logout(request)
     return redirect('/Login')

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
                doctor_id = form.cleaned_data.get('doctor_id')
                print("going to save")
                AppointmentObj = AppointmentDetails(patient_id=2,first_name=first_name,last_name=last_name,
                                            doctor_id=doctor_id,requested_date=requested_date)
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
            detail = AppointmentDetails.objects.get(appointment_id=id)
            detail = {'appointment_id': detail.appointment_id,'patient_id': detail.patient_id,'first_name': detail.first_name,'last_name': detail.last_name,
                        'doctor_id': detail.doctor_id,'requested_date': detail.requested_date}
        finally:
            return render(request, 'updateAppointment.html', {               
                'appointmentForm': appointmentForm(detail),             
            })
    def post(self, request, id):
        msgS='Entered'
        try:
            # try:
            #     id = signing.loads(id)
            # except:
            #     raise Http404
            detail = AppointmentDetails.objects.get(appointment_id=id)
            # client_persons=client_person.objects.filter(client_id=id)
            detailForm = appointmentForm(request.POST)
            if detailForm.is_valid():
                # detail.first_name = escapeXSS(str(request.POST.get('first_name')))
                # detail.first_name = escapeXSS(str(request.POST.get('address')))
                # detail.first_name = signing.loads(request.POST.get('sector'))
                # detail.first_name = signing.loads(request.POST.get('under_ministry'))
                detail.first_name = request.POST.get('first_name')
                detail.last_name = request.POST.get('last_name')
                detail.doctor_id = request.POST.get('doctor_id')
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

class insuranceClaimRequest(View):
    def get(self,request):
        appDetails = InsuranceClaimDetails.objects.all()
        return render(request,'insuranceClaimRequest.html',{
            'user':'aish',
            'insuranceClaimRequestForm': insuranceClaimRequestForm,
            'appDetails': appDetails,
        })
    def post(self,request):
        msgS = ''
        try:
            form = insuranceClaimRequestForm(request.POST)
            if form.is_valid():
                patient_firstname = form.cleaned_data.get('patient_firstname')
                patient_lastname = form.cleaned_data.get('patient_lastname')
                insurance_name = form.cleaned_data.get('insurance_name')
                claim_amt = form.cleaned_data.get('claim_amt')
                print("going to save")
                InsuranceClaimObj = InsuranceClaimDetails(patient_id=2,patient_firstname=patient_firstname,patient_lastname=patient_lastname,
                                            insurance_name=insurance_name,claim_amt=claim_amt)
                InsuranceClaimObj.save()
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
            return redirect('/patient/insuranceClaimRequest')    

class updateInsuranceClaimRequest(View):
    def get(self, request, id):
        try:
            detail = InsuranceClaimDetails.objects.get(id=id)
            detail = {'patient_id': detail.patient_id,'patient_firstname': detail.patient_firstname,'patient_lastname': detail.patient_lastname,
                        'insurance_name': detail.insurance_name,'claim_amt': detail.claim_amt}
        finally:
            return render(request, 'updateInsuranceClaimRequest.html', {               
                'insuranceClaimRequestForm': insuranceClaimRequestForm(detail),             
            })
    def post(self, request, id):
        msgS=''
        try:
            # try:
            #     id = signing.loads(id)
            # except:
            #     raise Http404
            detail = InsuranceClaimDetails.objects.get(id=id)
            # client_persons=client_person.objects.filter(client_id=id)
            detailForm = insuranceClaimRequestForm(request.POST)
            if detailForm.is_valid():
                # detail.first_name = escapeXSS(str(request.POST.get('first_name')))
                # detail.first_name = escapeXSS(str(request.POST.get('address')))
                # detail.first_name = signing.loads(request.POST.get('sector'))
                # detail.first_name = signing.loads(request.POST.get('under_ministry'))
                detail.patient_firstname = request.POST.get('patient_firstname')
                detail.patient_lastname = request.POST.get('patient_lastname')
                detail.insurance_name = request.POST.get('insurance_name')
                detail.claim_amt = request.POST.get('claim_amt')
                detail.save()
            msgS="Updated Successfully"
        except:
            msgE="Something Went Wrong"
        finally:
            # id = signing.dumps(id)
            messages.add_message(request, messages.SUCCESS if msgS else messages.ERROR, (msgS if not msgS == '' else msgE),
                                 extra_tags='callout callout-success calloutCustom lead' if msgS else 'callout callout-danger calloutCustom lead')
            return HttpResponseRedirect(reverse('patient:updateInsuranceClaimRequest', args=[id]))
  
class nextAppointment(View):
     def get(self, request, id):
         try:
             detail = AppointmentDetails.objects.get(appointment_id=id)
             detail = {'appointment_id': detail.appointment_id,'patient_id': detail.patient_id,'first_name': detail.first_name,'last_name': detail.last_name,
                         'doctor_id': detail.doctor_id}
         finally:
             return render(request, 'bookAppointment.html', {               
                 'appointmentForm': appointmentForm(detail),             
             })
     def post(self,request, id):
         msgS = ''
         try:
             form = appointmentForm(request.POST)
             if form.is_valid():
                 first_name = form.cleaned_data.get('first_name')
                 last_name = form.cleaned_data.get('last_name')
                 requested_date = form.cleaned_data.get('requested_date')
                 doctor_id = form.cleaned_data.get('doctor_id')
                 print("going to save")
                 AppointmentObj = AppointmentDetails(patient_id=2,first_name=first_name,last_name=last_name,
                                             doctor_id=doctor_id,requested_date=requested_date)
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
