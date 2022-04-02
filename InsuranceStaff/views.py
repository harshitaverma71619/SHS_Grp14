from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from InsuranceStaff.models import InsurancePolicies
from InsuranceStaff.models import InsuranceClaimDetails
from InsuranceStaff.models import InsuranceClaimRegister
from .forms import *
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import logout

# Create your views here.
class insuranceHome(View):
    def get(self,request):
        appDetails = InsuranceClaimDetails.objects.filter(claim_status = 'Pending')
        return render(request,'insuranceHome.html',{
            'user':'InsuranceStaff',
            'appDetails': appDetails,
        })

class newPolicies(View):
    def get(self,request):
        appDetails = InsurancePolicies.objects.all()
        return render(request,'newPolicies.html',{
            'user':'InsuranceStaff',
            'newInsurancePolicyForm': newInsurancePolicyForm,
            'appDetails': appDetails,
        })
    def post(self,request):
        msgS = ''
        try:
            form = newInsurancePolicyForm(request.POST)
            if form.is_valid():
                policy_name = form.cleaned_data.get('policy_name')
                coverage_plans = form.cleaned_data.get('coverage_plans')
                insurance_amt = form.cleaned_data.get('insurance_amt')
                print("going to save")
                InsurancePoliciesObj = InsurancePolicies(policy_name=policy_name,
                                            coverage_plans=coverage_plans,insurance_amt=insurance_amt)
                InsurancePoliciesObj.save()
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
            return redirect('/insurance/newPolicies')

class viewPolicies(View):
     def get(self, request):
        appDetails = InsurancePolicies.objects.all()
        return render(request,'viewPolicies.html',{
            'user':'InsuranceStaff',
            'newInsurancePolicyForm':newInsurancePolicyForm,
            'appDetails': appDetails,
        })
        
class checkClaims(View):
    def get(self, request, id):
        claimDetails = InsuranceClaimDetails.objects.get(claim_id=id)   
        print(claimDetails.claim_id)
        registerDetails = InsuranceClaimRegister.objects.all()
        policyDetails = InsurancePolicies.objects.all()
        policy_number =0
        amt =0
        print("hello")
        for a in policyDetails:
            if a.policy_name == claimDetails.policy_name:
                policy_number = a .policy_id
                amt = a.insurance_amt
                print("hi")
                print(policy_number)
        print(policy_number)
        found =0
        for a in registerDetails:
            if(a.patient_id == claimDetails.patient_id and 
                a.patient_firstname == claimDetails.patient_firstname and
                a.patient_lastname == claimDetails.patient_lastname and
                a.policy_id == policy_number and amt > claimDetails.claim_amt):
                print("Approved")
                print(claimDetails.patient_firstname)
                claimDetails.claim_status = 'Approved'
                claimDetails.claim_transaction_status = 'Approved'
                claimDetails.save()
                found = 1
                print("Saved")

        if(found):
           # messages.success(request, 'Approved on Verification')
            messages.success(request, 'Approved on Verification')
            #msgS = "Approved on Verification"
            print("true")
        else:
            claimDetails.claim_status = 'Rejected'
            claimDetails.save()
            #msgE = "Rejected on Verification"
            messages.error(request, 'Rejected on Verification')
            print("false")
        
        print("in finally block")
        '''
        messages.add_message(request, messages.SUCCESS if msgS else messages.ERROR,
                                (msgS if not msgS == '' else msgE),
                                extra_tags='callout callout-success calloutCustom lead' if msgS else 'callout callout-danger calloutCustom lead')
        '''
        appDetails = InsuranceClaimDetails.objects.filter(claim_status = 'Pending')

        return render(request,'insuranceHome.html',{
            'user':'InsuranceStaff',
             'appDetails': appDetails,
        })

class viewClaimRequests(View):
    def get(self,request):
        appDetails = InsuranceClaimDetails.objects.all()
        return render(request,'viewClaimRequests.html',{
            'user':'InsuranceStaff',
            'appDetails': appDetails,
        })






            
