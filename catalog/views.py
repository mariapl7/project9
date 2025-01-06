from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Здесь вы можете добавить код для обработки данных, например, отправка email

        success = True  # Успешная отправка данных

    return render(request, 'catalog/contacts.html', {'success': success})