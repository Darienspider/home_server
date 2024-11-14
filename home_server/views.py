from django.shortcuts import render

def home(request):
    context = {
        "title":"Home Server Main Screen"
    }
    return render(request, "home.html",context=context)
