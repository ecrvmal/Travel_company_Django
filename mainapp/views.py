# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404
# from .models import ListOfCountries
from mainapp.models import Accommodation


def main(request):
    return render(request, 'mainapp/index.html')


def accommodations(request):
    title = "Размещение"

    # list_of_accommodations = Accommodation.objects.filter(is_active=True)
    list_of_accommodations = Accommodation.objects.all()

    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations
    }
    print(f'content: {content}')
    return render(request, 'mainapp/accommodations.html', content)


def accommodation(request, pk):
    """
    the function returns list of accommodations from DB
    :param request:
    :param pk:
    :return:
    """
    title = 'products'

    content = {
        'title': title,
        'accommodation': get_object_or_404(Accommodation, pk=pk),
    }
    print(f'content: {content}')
    return render(request, 'mainapp/accommodation_details.html', content)
