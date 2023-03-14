from django.shortcuts import render

# Create your views here.
def second_jin(request):
    d={'name':'Subbareddy','age':50}
    return render(request,'second_jin.html',context=d)


