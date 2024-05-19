from django.shortcuts import render

# Create your views here.
def all_agun(request):
    return render(request, 'agun/all_agun.html')