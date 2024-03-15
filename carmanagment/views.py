from django.shortcuts import render, redirect
from .models import Car, UserProfile


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'carmanagment/car_list.html', {'cars': cars})


def add_car(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        manufacturer = request.POST.get('manufacturer')
        year = request.POST.get('year')
        image = request.FILES.get('image')
        file = request.FILES.get('file')

        car = Car(
            name=name,
            number=number,
            manufacturer=manufacturer,
            year=year,
            image=image,
            file=file,
        )
        car.save()

        return redirect('car_list')

    return render(request, 'carmanagment/add_car.html')


def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)  # получение профиля пользователя по залогиненым данным, ничего передавать не надо!

