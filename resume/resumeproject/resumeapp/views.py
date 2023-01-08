from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request,'courses.html')

def education(request):

    edu = {
        "one":{'sr.no':1,'study':'SSC','passing-year':2015,'board':'Maharashtra Board','Percentages':80 },
        "two":{'sr.no':2,'study':'HSC','passing-year':2016,'board':'Maharashtra Board','Percentages':70 },
        "three":{'sr.no':3,'study':'BE','passing-year':2019,'board':'Mumbai university','Percentages':60 },
    }
    data = { 'education': edu }

    return render(request,'education.html',data)

def skills(request):

    s1={
        "PYTHON": 65,
        'HTML' : 60,
        'CSS' : 55,
        'JAVASCRIPT' : 60
    }
    s2={'skills':s1}
    return render(request,'skills.html',s2)

def projects(request):
    return render(request,'projects.html')

def exp(request):
    return render(request,'exp.html')

def contact(request):
    return render(request,'contact.html')

def thanks(request):
    return render(request,'thanks.html')
