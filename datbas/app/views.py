from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseNotFound

def index(request):
    products = Product.objects.all()
    return render(request, 'app/index.html', context={'products': products})





def create(request):
    if(request.method == "POST"):
        product = Product()
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.company_id = request.POST.get('company') 
        product.save()
        return redirect('homepage')

    companies = Company.objects.all()
    return render (request, 'app/create.html', context={'companies': companies})




def edit(request, id):
    try:
        product = Product.objects.get(id=id)
        if request.method == 'POST':
            product.name = request.POST.get("name")
            product.price = request.POST.get("price")
            product.company_id = request.POST.get('company')
            product.save()
            return redirect('homepage')
        else:
            companies = Company.objects.all()
            return render(request, 'app/edit.html', {'product': product, 'companies': companies})
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h2>Product not found</h2>')




def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('homepage')
    
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h2>Product not found</h2>')



