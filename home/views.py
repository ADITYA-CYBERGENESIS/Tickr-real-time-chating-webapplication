from django.shortcuts import render,redirect


# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect('chathome')
    return render(request,'home\homepage.html')

def pricing(request):
    return render(request,'home/pricing.html') 