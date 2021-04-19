from django.shortcuts import render
from .models import Car

# Create your views here.

def home(request):
    cars = Car.objects.all()
    year_search = Car.objects.values_list('year', flat=True).distinct()

    model_search = Car.objects.values_list('model', flat=True).distinct()

    transmission__search = Car.objects.values_list('transmission' , flat=True).distinct()

    brand_search = Car.objects.values_list('brand', flat=True).distinct()

    mileage_search = Car.objects.values_list('mileage', flat=True).distinct()

    discounted_price_search = Car.objects.values_list('discounted_price', flat=True).distinct()



    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)


    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)



    if 'mileage' in request.GET:
        mileage = request.GET['mileage']
        if mileage:
            cars = cars.filter(mileage__iexact=mileage)
            


    


    if 'brand' in request.GET:
        brand = request.GET['brand']
        if brand:
            cars = cars.filter(brand__iexact=brand)




    if 'discounted_price' in request.GET:
        discounted_price = request.GET['discounted_price']
        if discounted_price:
            cars = cars.filter(discounted_price__iexact=discounted_price)



    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)        








    data = {

        'cars': cars,
        'year_search': year_search,
        'brand_search': brand_search,
        'transmission_search': transmission__search,
        'mileage_search': mileage_search,
        'model_search': model_search,
        'discounted_price_search': discounted_price_search,

    }      

    
    




    return render(request, 'pages/index.html', {'cars': cars})


def about(request):
    return render(request, 'pages/about.html',)


def search(request):
    cars = Car.objects.all()
    return render(request, 'pages/search.html', {'cars': cars})


def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars/cars.html',{'cars': cars})  


def car_detail(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'cars/car_detail.html', {'cars': cars})      

    



    


