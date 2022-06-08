from django.shortcuts import render

# Create your views here.

def companies(request):
    
    context ={}

    return render(request, 'companies/companies.html', context)