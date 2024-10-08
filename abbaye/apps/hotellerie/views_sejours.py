""" apps/hotellerie/view_sejours.py """

import datetime

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from modules.mails import mail_pere_suiveur, mail_sacristie

from apps.main.decorators import group_required

from .forms import SejourForm
from .models import Chambre, Sejour


@group_required('Hôtellerie')
def list(request):
    """ List view of Sejours. """
    sejours = Sejour.objects.all().order_by('-sejour_du')
    return render(request, 'hotellerie/sejours/list.html', {'sejours': sejours})


@group_required('Hôtellerie')
def create(request):
    """ Create a Sejour. """
    if request.method == 'POST':
        form = SejourForm(request.POST)

        if form.is_valid():
            sejour = form.save()

            # Create rooms:
            for chambre in form.cleaned_data['chambre']:
                Chambre.objects.create(sejour=sejour, chambre=chambre)

            # Send mails:
            if sejour.dit_messe and sejour.mail_sacristie:
                mail_sacristie(sejour)
            if sejour.personne and sejour.mail_pere_suiveur:
                mail_pere_suiveur(sejour)

            date = form.cleaned_data['sejour_du']
            return HttpResponseRedirect(reverse('hotellerie:main_calendar', kwargs={
                'day': '{:%d}'.format(date),
                'month': '{:%m}'.format(date),
                'year': '{:%Y}'.format(date),
            }))

    form = SejourForm()

    return render(request, 'hotellerie/sejours/form.html', {'form': form})


@group_required('Hôtellerie')
def details(request, *args, **kwargs):
    """ Details of a Sejour. """
    sejour = get_object_or_404(Sejour, pk=kwargs['pk'])
    chambres = sejour.chambres_string()
    return render(
        request,
        'hotellerie/sejours/details.html',
        {
            'sejour': sejour,
            'chambres': chambres,
        }
    )


@group_required('Hôtellerie')
def update(request, **kwargs):
    """ Update a Sejour. """
    sejour = get_object_or_404(Sejour, pk=kwargs['pk'])

    if request.method == 'POST':
        form = SejourForm(request.POST, instance=sejour)

        if form.is_valid():
            form.save()

            # Remove old rooms and insert new ones:
            Chambre.objects.filter(sejour=sejour).delete()
            for chambre in form.cleaned_data['chambre']:
                Chambre.objects.create(sejour=sejour, chambre=chambre)

            # Send mails:
            if sejour.dit_messe and sejour.mail_sacristie:
                mail_sacristie(sejour)
            if sejour.personne and sejour.mail_pere_suiveur:
                mail_pere_suiveur(sejour)
            date = form.cleaned_data['sejour_du']
            return HttpResponseRedirect(reverse('hotellerie:main_calendar', kwargs={
                'day': '{:%d}'.format(date),
                'month': '{:%m}'.format(date),
                'year': '{:%Y}'.format(date),
            }))

    else:
        chambres = sejour.chambres_list()
        form = SejourForm(
            instance=sejour,
            initial={
                'chambre': chambres,
            }
        )

    return render(request, 'hotellerie/sejours/form.html', {
        'form': form,
        'sejour': sejour,
    })


@group_required('Hôtellerie')
def delete(request, *args, **kwargs):
    """ Delete a Sejour. """
    sejour = get_object_or_404(Sejour, pk=kwargs['pk'])

    if request.method == 'POST':
        form = SejourForm(request.POST, instance=sejour)
        sejour.delete()
        return HttpResponseRedirect(reverse('hotellerie:main_calendar'))

    form = SejourForm(instance=sejour)

    return render(request, 'hotellerie/sejours/delete.html', {
        'form': form,
        'sejour': sejour,
    })


def get_rooms_status(request):
    """ Returns the rooms' status between sejour_du and sejour_au. """
    # Get data from JS:
    id_sejour = int(request.GET['id_sejour'])
    start_raw = request.GET['start']
    start_split = start_raw.split('/')
    start = datetime.date(
        int(start_split[2]), int(start_split[1]), int(start_split[0])
    )
    end_raw = request.GET['end']
    end_split = end_raw.split('/')
    end = datetime.date(
        int(end_split[2]), int(end_split[1]), int(end_split[0])
    )

    # Create the rooms' dict:
    rooms = {}
    for i in range(27):
        rooms[str(i)] = {
            'occupied': '',
            'title': '',
        }
    rooms['Chambre de l\'évêque'] = {
        'occupied': '',
        'title': '',
    }

    # Get sejours having a day between start and end:
    sejours_du_inside = Sejour.objects.filter(
        sejour_du__gte=start
    ).filter(
        sejour_du__lte=end
    )
    sejours_au_inside = Sejour.objects.filter(
        sejour_au__gte=start
    ).filter(
        sejour_au__lte=end
    )
    sejours_before_and_after = Sejour.objects.filter(
        sejour_du__lte=start
    ).filter(
        sejour_au__gte=end
    )
    sejours = sejours_du_inside.union(
        sejours_au_inside,
        sejours_before_and_after
    )

    for i, sejour in enumerate(sejours):
        chambres = Chambre.objects.filter(sejour=sejour)
        if sejour.pk != id_sejour:
            for j, chambre in enumerate(chambres):
                rooms[chambre.chambre]['occupied'] = True
                rooms[chambre.chambre]['title'] += '{}\n'.format(sejour)

    return JsonResponse(rooms)
