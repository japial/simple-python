import re

from django.http import HttpRequest
from django.shortcuts import render

from ticket.data import Ticket
from ticket.forms import TicketForm


def index(request: HttpRequest):
    errors = {}
    ticket = None
    is_valid = False
    if request.method == 'POST':
        form = TicketForm(data=request.POST)
        is_valid = form.is_valid();

        phone = request.POST.get('phone')
        name = request.POST.get('name')
        email = request.POST.get('email')

        if is_valid:
            ticket = Ticket(name, email, phone)
            ticket.save()

    else:
        form = TicketForm()

    return render(
        request,
        'index.html',
        context={
            'errors': errors,
            'ticket': ticket,
            'form': form
        }
    )

