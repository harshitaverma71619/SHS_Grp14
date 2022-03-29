from asyncio.windows_events import NULL
from distutils.log import error
from email import message
from functools import reduce
from pickle import NONE
from tokenize import Number
from wsgiref.simple_server import demo_app
from xml.dom.minidom import Attr
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from Doctors.models import prescriptions, labTests

from Doctors import models
from .forms import *
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.db.models import Q
import operator
from Patients.models import PatientDetails
from HospitalStaff.models import AppointmentDetails
import datetime

flag = 'true'

class doctorHome(View):
    def get(self,request):
        appDetails = AppointmentDetails.objects.filter(requested_date = datetime.date.today())
        print(appDetails)
        print(datetime.date.today())
        date = datetime.date.today()
        return render(request,'doctorHome.html',{
            'user':'Doctor',
            'appDetails': appDetails,
            'date':date
        })

class addPrescription(View):
    def get(self,request, id):
        try:
            print("Entered Try")
            details = AppointmentDetails.objects.filter(appointment_id=id)
            prescriptionDetails = models.prescriptions.objects.filter(appointment_id = id)
            details1 = {}
            print(details)
        finally:
            return render(request, 'addPrescription.html', {"prescriptionDetails": prescriptionDetails,"patientdetails" : details, 'patientPrescriptionForm': patientPrescriptionForm(details1)})
    
    def post(self, request, id):
        msgS=''
        try:
            print("Enteredpost try")
            # try:
            #     id = signing.loads(id)
            # except:
            #     raise Http404
            detail1 = AppointmentDetails.objects.get(appointment_id = id)
            print(detail1.patient_id)
            print("user detail")
            print(detail1.patient_id)
            # client_persons=client_person.objects.filter(client_id=id)
            prescription = patientPrescriptionForm(request.POST)
            print(prescription.is_valid())
            if prescription.is_valid():
                print("entered prescription if")
                # detail.first_name = escapeXSS(str(request.POST.get('first_name')))
                # detail.first_name = escapeXSS(str(request.POST.get('address')))
                # detail.first_name = signing.loads(request.POST.get('sector'))
                # detail.first_name = signing.loads(request.POST.get('under_ministry'))
                #detail1.patient_diagnosis = request.POST.get('patient_diagnosis')
                drug1 = prescription.cleaned_data.get('drug')
                print(drug1)
                unit1 = prescription.cleaned_data.get('unit')
                print(unit1)
                dosage1 = prescription.cleaned_data.get('dosage')
                prescription_text1 = prescription.cleaned_data.get('prescription_text')
                print(prescription_text1)
                print(detail1.patient_id)
                pt = detail1.patient_id
                ap = detail1.appointment_id
                fs = detail1.first_name
                ls = detail1.last_name
                rq = detail1.requested_date
                di = detail1.doctor_id
                pd = detail1.patient_diagnosis
                prescriptionObj = prescriptions(patient_id = pt,appointment_id = ap,first_name = fs,
                last_name = ls, requested_date = rq,doctor_id = di,patient_diagnosis = pd,
                drug = drug1,unit = unit1,dosage = dosage1, prescription_text = prescription_text1)
                print(prescriptionObj)
                prescriptionObj.save()
                print(detail1)
                #PatientDetailsObj = PatientDetails(patient_id = detail.patient_id,patient_name=detail.patient_name,patient_age = detail.patient_age, patient_weight = detail.patient_weight,patient_height = detail.patient_height, patient_address = detail.patient_address, patient_phone_no = detail.patient_phone_no,patient_email =detail.patient_email,insurance_id = detail.insurance_id, patient_diagnosis = detail.patient_diagnosis,patient_reports=detail.patient_reports, patient_prescription=detail.patient_prescription)
                #PatientDetailsObj.save()
                #msgS="Updated Successfully"
                messages.success(request, 'Drug Added Successfully!')
            #return HttpResponseRedirect(reverse('doctors:updatePatientDetails', args=[detail1.patient_id]))
        except:
            #msgE="Something Went Wrong"
            messages.error(request, error)
        finally:
            # id = signing.dumps(id)
            #messages.add_message(request, messages.SUCCESS if msgS else messages.ERROR, (msgS if not msgS == '' else msgE),
             #                    extra_tags='callout callout-success calloutCustom lead' if msgS else 'callout callout-danger calloutCustom lead')
            #return redirect('/doctors/patientRecords/search/', args=[detail1.patient_id])
            details = AppointmentDetails.objects.filter(appointment_id=id)
            details1 = {}
            prescriptionDetails = models.prescriptions.objects.filter(appointment_id = detail1.appointment_id)
            return render(request, 'addPrescription.html',{"patientdetails" : details, 'patientPrescriptionForm': patientPrescriptionForm(details1),'prescriptionDetails': prescriptionDetails})

class viewLabReports(View):
    def get(self,request):
        return render(request,'viewLabReports.html',{
            'user':'Doctor'
        })

class addDiagnosis(View):
    def get(self,request, id):
        flag = 'false'
        try:
            print("Entered Try")
            details = AppointmentDetails.objects.get(appointment_id=id)
            #lab_tests1 = AppointmentDetails.objects.get(appointment_id = id)
            print(details)
            details2 = AppointmentDetails.objects.filter(appointment_id=id)
            details = {'patient_diagnosis': details.patient_diagnosis, 'appointment_id': id}
            #lab_tests = {'lab_tests': lab_tests1.lab_tests, 'appointment_id': id}
           # print(lab_tests)
            labTestDetails = labTests.objects.filter(appointment_id = id)
            print(labTestDetails)
            #print(lab_tests)
        finally:
            return render(request, 'patientDiagnosis.html', {'details2': details2, 'flag': flag, 'labTestDetails': labTestDetails, 'diagnosisForm': diagnosisForm(details), 'labTestsForm': labTestsForm(), 'details': details})

    def post(self, request, id):
        msgS=''
        flag = 'true'
        if request.POST.get('lab_tests') == 'lab_test1' or request.POST.get('lab_tests') == 'lab_test2' or request.POST.get('lab_tests') == 'lab_test3' or request.POST.get('lab_tests') == 'lab_test4':
            print("-------")
            try:
                print("Enteredlab try")
                # try:
                #     id = signing.loads(id)
                # except:
                #     raise Http404
                detail1 = AppointmentDetails.objects.get(appointment_id = id)
                print(detail1.patient_id)
                print("user detail---------")
                print(detail1.patient_id)
                # client_persons=client_person.objects.filter(client_id=id)
                labTests1 = labTestsForm(request.POST)
                print(labTests1.is_valid())
                if labTests1.is_valid():
                    print("entered prescription if")
                    # detail.first_name = escapeXSS(str(request.POST.get('first_name')))
                    # detail.first_name = escapeXSS(str(request.POST.get('address')))
                    # detail.first_name = signing.loads(request.POST.get('sector'))
                    # detail.first_name = signing.loads(request.POST.get('under_ministry'))
                    #detail1.patient_diagnosis = request.POST.get('patient_diagnosis')
                    lab_tests1 = labTests1.cleaned_data.get('lab_tests')
                    print(lab_tests1)
                    pt = detail1.patient_id
                    ap = detail1.appointment_id
                    fs = detail1.first_name
                    ls = detail1.last_name
                    rq = detail1.requested_date
                    di = detail1.doctor_id
                    pd = detail1.patient_diagnosis

                    labTestObj = labTests(patient_id = pt,appointment_id = ap,first_name = fs,
                    last_name = ls, requested_date = rq,doctor_id = di, patient_diagnosis = pd,lab_Tests = lab_tests1)
                    print(labTestObj)
                    labTestObj.save()
                    print(detail1)
                    #PatientDetailsObj = PatientDetails(patient_id = detail.patient_id,patient_name=detail.patient_name,patient_age = detail.patient_age, patient_weight = detail.patient_weight,patient_height = detail.patient_height, patient_address = detail.patient_address, patient_phone_no = detail.patient_phone_no,patient_email =detail.patient_email,insurance_id = detail.insurance_id, patient_diagnosis = detail.patient_diagnosis,patient_reports=detail.patient_reports, patient_prescription=detail.patient_prescription)
                    #PatientDetailsObj.save()
                    #msgS="Updated Successfully"
                    messages.success(request, 'Lab Test Added Successfully!')
                #return HttpResponseRedirect(reverse('doctors:updatePatientDetails', args=[detail1.patient_id]))
            except:
                #msgE="Something Went Wrong"
                messages.error(request, error)
            finally:
                # id = signing.dumps(id)
                #messages.add_message(request, messages.SUCCESS if msgS else messages.ERROR, (msgS if not msgS == '' else msgE),
                    #                    extra_tags='callout callout-success calloutCustom lead' if msgS else 'callout callout-danger calloutCustom lead')
                #return redirect('/doctors/patientRecords/search/', args=[detail1.patient_id])
                details = AppointmentDetails.objects.get(appointment_id=id)
                #lab_tests1 = AppointmentDetails.objects.get(appointment_id = id)
                print(details)
                details = {'patient_diagnosis': details.patient_diagnosis, 'appointment_id': id}
                #lab_tests = {'lab_tests': lab_tests1.lab_tests, 'appointment_id': id}
                labTestDetails = labTests.objects.filter(appointment_id = id)
                details2 = AppointmentDetails.objects.filter(appointment_id=id)
                return render(request, 'patientDiagnosis.html', {'details2':details2,'flag': flag,'labTestDetails': labTestDetails, 'diagnosisForm': diagnosisForm(details), 'labTestsForm': labTestsForm(), 'details': details})

        else:
            try:
                print("Eneubhjd")
                print("Enteredpost try")
                # try:
                #     id = signing.loads(id)
                # except:
                #     raise Http404
                detail1 = AppointmentDetails.objects.get(appointment_id = id)
                print(detail1.patient_id)
                print("user detail")
                print(detail1.patient_id)
                # client_persons=client_person.objects.filter(client_id=id)
                diagnosis = diagnosisForm(request.POST)
                print(diagnosis.is_valid())
                if diagnosis.is_valid():
                    print("entered if")
                    # detail.first_name = escapeXSS(str(request.POST.get('first_name')))
                    # detail.first_name = escapeXSS(str(request.POST.get('address')))
                    # detail.first_name = signing.loads(request.POST.get('sector'))
                    # detail.first_name = signing.loads(request.POST.get('under_ministry'))
                    detail1.patient_diagnosis = request.POST.get('patient_diagnosis')
                    detail1.save()
                    print(detail1)
                    #PatientDetailsObj = PatientDetails(patient_id = detail.patient_id,patient_name=detail.patient_name,patient_age = detail.patient_age, patient_weight = detail.patient_weight,patient_height = detail.patient_height, patient_address = detail.patient_address, patient_phone_no = detail.patient_phone_no,patient_email =detail.patient_email,insurance_id = detail.insurance_id, patient_diagnosis = detail.patient_diagnosis,patient_reports=detail.patient_reports, patient_prescription=detail.patient_prescription)
                    #PatientDetailsObj.save()
                    #msgS="Updated Successfully"
                    messages.success(request, 'Patient Diagnosis Added Successfully!')
                #return HttpResponseRedirect(reverse('doctors:updatePatientDetails', args=[detail1.patient_id]))
            except:
                #msgE="Something Went Wrong"
                messages.error(request, 'Something Went Wrong!')
            finally:
                # id = signing.dumps(id)
                #messages.add_message(request, messages.SUCCESS if msgS else messages.ERROR, (msgS if not msgS == '' else msgE),
                #                    extra_tags='callout callout-success calloutCustom lead' if msgS else 'callout callout-danger calloutCustom lead')
                #return redirect('/doctors/patientRecords/search/', args=[detail1.patient_id])
                details = AppointmentDetails.objects.get(appointment_id=id)
                #lab_tests1 = AppointmentDetails.objects.get(appointment_id = id)
                details2 = AppointmentDetails.objects.filter(appointment_id=id)
                print(details)
                details = {'patient_diagnosis': details.patient_diagnosis, 'appointment_id': id}
                #lab_tests = {'lab_tests': lab_tests1.lab_tests, 'appointment_id': id}
                labTestDetails = labTests.objects.filter(appointment_id = id)
                return render(request, 'patientDiagnosis.html', {'details2':details2,'flag': flag,'labTestDetails': labTestDetails, 'diagnosisForm': diagnosisForm(details), 'labTestsForm': labTestsForm(), 'details': details})

class patientRecords(View):
    def get(self,request):
        return render(request,'patientRecords.html',{
            'user':'Doctor'
        })

class patientDiagnosis(View):
    def get(self,request):
        return render(request,'searchDiagnosis.html',{
            'user':'Doctor'
        })

def searchBar(request):
    flag = "true"
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            patientdetails = PatientDetails.objects.filter(patient_id = query)
            print("search bar")
            print(patientdetails)
            details = {}
            return render(request, 'searchResultsView.html', {'patientdetails': patientdetails, "details": details, "flag":flag})
        else:
            print("No patient with this id number")
            return render(request, 'searchResultsView.html',{})

def searchLabReports(request):
    flag = "true"
    if request.method == 'GET':
        query = request.GET.get('query')
        #query1 = request.GET.get('query1')
        if query:
            labreportdetails = labTests.objects.filter(appointment_id = query)
            #labreportdetails = labreportdetails.filter(lab_Tests = query1)
            print("search bar")
            print("labreportdetails")
            print(labreportdetails)
            details = {}
            return render(request, 'viewLabReports.html', {'labreportdetails': labreportdetails, "details": details, "flag":flag})
        else:
            print("No patient with this id number")
            return render(request, 'viewLabReports.html',{})

def searchDiagnosis(request):
    flag = "true"
    if request.method == 'GET':
        print("Entered Serach Diagnosis")
        query = request.GET.get('query')
        if query:
            patientdetails = AppointmentDetails.objects.filter(patient_id = query)
            #patientdetails = patientdetails.filter(doctor_id = 2)
            print("search bar")
            print(patientdetails)
            details = {}
            return render(request, 'ViewDiagnosis.html', {'patientdetails': patientdetails, "details": details, "flag":flag})
        else:
            print("No patient with this id number")
            return render(request, 'ViewDiagnosis.html',{})

def searchAppointments(request):
    if request.method == 'GET':
        print(request)
        start = request.GET.get('start')
        appDetails = AppointmentDetails.objects.filter(requested_date = start)
        date = start
        return render(request,'doctorHome.html',{
            'user':'Doctor',
            'appDetails': appDetails,
            'date': date
        })

class updatePatientDetails(View):
    def get(self, request, id):
        flag = 'false'
        try:
            print("Entered try")
            details = PatientDetails.objects.get(patient_id=id)
            print(details)
            details = {'patient_id': details.patient_id,'patient_name': details.patient_name,'patient_age': details.patient_age, 'patient_weight': details.patient_weight,
            'patient_height': details.patient_height, 'patient_address': details.patient_address, 'patient_phone_no': details.patient_phone_no,
            'patient_email': details.patient_email}
            print(details)
        finally:
            print("enteed finally")
            return render(request, 'searchResultsView.html', {'details': details, 'patientDetailsForm': patientDetailsForm(details), "flag":flag})
    
    def post(self, request, id):
        msgS=''
        try:
            print("Enteredpost try")
            # try:
            #     id = signing.loads(id)
            # except:
            #     raise Http404
            detail1 = PatientDetails.objects.get(patient_id = id)
            print(detail1.patient_id)
            print("user detail")
            print(detail1.patient_id)
            # client_persons=client_person.objects.filter(client_id=id)
            detailForm = patientDetailsForm(request.POST)
            print(detailForm.is_valid())
            if detailForm.is_valid():
                print("entered if")
                # detail.first_name = escapeXSS(str(request.POST.get('first_name')))
                # detail.first_name = escapeXSS(str(request.POST.get('address')))
                # detail.first_name = signing.loads(request.POST.get('sector'))
                # detail.first_name = signing.loads(request.POST.get('under_ministry'))
                detail1.patient_id = request.POST.get('patient_id')
                detail1.patient_name = request.POST.get('patient_name')
                detail1.patient_age = request.POST.get('patient_age')
                detail1.patient_weight = request.POST.get('patient_weight')
                detail1.patient_height = request.POST.get('patient_height')
                detail1.patient_address = request.POST.get('patient_address')
                detail1.patient_phone_no = request.POST.get('patient_phone_no')
                detail1.patient_email = request.POST.get('patient_email')
                detail1.save()
                print(detail1.patient_id)
                #PatientDetailsObj = PatientDetails(patient_id = detail.patient_id,patient_name=detail.patient_name,patient_age = detail.patient_age, patient_weight = detail.patient_weight,patient_height = detail.patient_height, patient_address = detail.patient_address, patient_phone_no = detail.patient_phone_no,patient_email =detail.patient_email,insurance_id = detail.insurance_id, patient_diagnosis = detail.patient_diagnosis,patient_reports=detail.patient_reports, patient_prescription=detail.patient_prescription)
                #PatientDetailsObj.save()
                #msgS="Updated Successfully"
                messages.success(request, 'Patient Details Updated Successfully!')
            #return HttpResponseRedirect(reverse('doctors:updatePatientDetails', args=[detail1.patient_id]))
        except:
            #msgE="Something Went Wrong"
            messages.error(request, 'Something Went Wrong!')
        finally:
            # id = signing.dumps(id)
            #messages.add_message(request, messages.SUCCESS if msgS else messages.ERROR, (msgS if not msgS == '' else msgE),
             #                    extra_tags='callout callout-success calloutCustom lead' if msgS else 'callout callout-danger calloutCustom lead')
            flag = 'true'
            #return redirect('/doctors/patientRecords/search/', args=[detail1.patient_id])
            print(detail1.patient_id)
            patientdetails = PatientDetails.objects.filter(patient_id = detail1.patient_id)
            print(patientdetails)
            return render(request, 'searchResultsView.html',{"patientdetails":patientdetails, "flag":flag})


class updatePatientDiagnosis(View):
    def get(self, request, id):
        flag = 'false'
        try:
            print("Entered try")
            print(id)
            details = AppointmentDetails.objects.get(appointment_id=id)
            print(details)
            details = {'appointment_id': details.appointment_id,'patient_id': details.patient_id,'first_name': details.first_name, 'last_name': details.last_name,
            'doctor_id': details.doctor_id, 'requested_date': details.requested_date, 'status': details.status,
            'patient_diagnosis': details.patient_diagnosis}
            print(details)
        finally:
            print("enteed finally")
            return render(request, 'ViewDiagnosis.html', {'details': details, 'patientDiagnosisForm': patientDiagnosisForm(details), "flag":flag})
    
    def post(self, request, id):
        msgS=''
        try:
            print("Enteredpost try")
            # try:
            #     id = signing.loads(id)
            # except:
            #     raise Http404
            detail1 = AppointmentDetails.objects.get(appointment_id = id)
            print(detail1.patient_id)
            print("user detail")
            print(detail1.patient_id)
            # client_persons=client_person.objects.filter(client_id=id)
            detailForm = patientDiagnosisForm(request.POST)
            print(detailForm.is_valid())
            if detailForm.is_valid():
                print("entered if")
                # detail.first_name = escapeXSS(str(request.POST.get('first_name')))
                # detail.first_name = escapeXSS(str(request.POST.get('address')))
                # detail.first_name = signing.loads(request.POST.get('sector'))
                # detail.first_name = signing.loads(request.POST.get('under_ministry'))
                detail1.patient_diagnosis = request.POST.get('patient_diagnosis')
                detail1.save()
                print(detail1.patient_id)
                #PatientDetailsObj = PatientDetails(patient_id = detail.patient_id,patient_name=detail.patient_name,patient_age = detail.patient_age, patient_weight = detail.patient_weight,patient_height = detail.patient_height, patient_address = detail.patient_address, patient_phone_no = detail.patient_phone_no,patient_email =detail.patient_email,insurance_id = detail.insurance_id, patient_diagnosis = detail.patient_diagnosis,patient_reports=detail.patient_reports, patient_prescription=detail.patient_prescription)
                #PatientDetailsObj.save()
                #msgS="Updated Successfully"
                messages.success(request, 'Patient Diagnosis Updated Successfully!')
            #return HttpResponseRedirect(reverse('doctors:updatePatientDetails', args=[detail1.patient_id]))
        except:
            #msgE="Something Went Wrong"
            messages.error(request, 'Something Went Wrong!')
        finally:
            # id = signing.dumps(id)
            #messages.add_message(request, messages.SUCCESS if msgS else messages.ERROR, (msgS if not msgS == '' else msgE),
             #                    extra_tags='callout callout-success calloutCustom lead' if msgS else 'callout callout-danger calloutCustom lead')
            flag = 'true'
            #return redirect('/doctors/patientRecords/search/', args=[detail1.patient_id])
            print(detail1.patient_id)
            patientdetails = AppointmentDetails.objects.filter(patient_id = request.POST.get('patient_id'))
            print(patientdetails)
            return render(request, 'ViewDiagnosis.html',{"patientdetails":patientdetails, "flag":flag})


class deletePatientDiagnosis(View):
    def post(self, request, id):
            flag = 'false'
            try:
                print("Entered try")
                print(id)
                details = AppointmentDetails.objects.get(appointment_id=id)
                print(details)
                details = {'appointment_id': details.appointment_id,'patient_id': details.patient_id,'first_name': details.first_name, 'last_name': details.last_name,
                'doctor_id': details.doctor_id, 'requested_date': details.requested_date, 'status': details.status,
                'patient_diagnosis': details.patient_diagnosis}
                print(details)
            finally:
                print("enteed finally")
                return render(request, 'ViewDiagnosis.html', {'details': details, 'patientDiagnosisForm': patientDiagnosisForm(details), "flag":flag})
