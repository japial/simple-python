from django.http import HttpRequest
from django.shortcuts import render

from data.atms import get_locations


def index(request: HttpRequest):
    search_query = request.GET.get('search')

    if search_query:
        atm_list = filter(lambda atm: search_query.title() in atm.location, get_locations())
    else:
        atm_list = get_locations

    context = {'atm_list': atm_list}
    return render(request, 'base.html', context)

