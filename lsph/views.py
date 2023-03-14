from django.shortcuts import render

# Create your views here.
def first_jin(request):
    d={'name':'Harikumar','age':20}
    return render(request,'first_jin.html',context=d)

