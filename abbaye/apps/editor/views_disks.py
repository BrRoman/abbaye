""" apps/editor/views_disks.py """

import os

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required

from .forms import DiskForm
from .models import Charge, Product


def disks_list(request):
    """ List of disks. """
    disks = Product.objects.filter(
        category='disk').order_by('ref_tm', 'ean', 'title')
    return render(
        request,
        'editor/disks/list.html',
        {
            'disks': disks
        }
    )


@group_required('Editor')
def disk_create(request):
    """ Create a disk. """
    if request.method == 'POST':
        form = DiskForm(request.POST)
        if form.is_valid():
            disk = form.save()
            return HttpResponseRedirect(
                reverse(
                    'editor:disk_details',
                    kwargs={
                        'pk': disk.pk,
                    }
                )
            )

    else:
        form = DiskForm()

    return render(
        request,
        'editor/disks/form.html',
        {
            'form': form,
        }
    )


def disk_details(request, **kwargs):
    """ Details of a disk. """
    disk = get_object_or_404(Product, pk=kwargs['pk'])

    # Charges:
    charges = Charge.objects.filter(product=disk)
    total_charges = 0
    for index, charge in enumerate(charges):
        total_charges += charge.amount
    cost = (total_charges / disk.circulation) if disk.circulation else 0
    theorical_price = (cost * disk.coefficient) if disk.coefficient else 0

    # Barcode:
    if disk.ean:
        if not os.path.exists('{}.png'.format(disk.ean)):
            # Create the png:
            os.system(
                "barcode -b {0} -e 'ean13' -u mm -g 100x50 -S -o /home/frromain/Sites/abbaye/abbaye/apps/editor/static/editor/img/barcodes/barcode.svg; \
                convert /home/frromain/Sites/abbaye/abbaye/apps/editor/static/editor/img/barcodes/barcode.svg -transparent '#FFFFFF' -trim /home/frromain/Sites/abbaye/abbaye/apps/editor/static/editor/img/barcodes/{0}.png; \
                rm /home/frromain/Sites/abbaye/abbaye/apps/editor/static/editor/img/barcodes/*.svg; \
                cp /home/frromain/Sites/abbaye/abbaye/apps/editor/static/editor/img/barcodes/{0}.png /home/frromain/Sites/abbaye/abbaye/apps/editor/static/editor_files/img/barcodes/{0}.png"
                .format(disk.ean)
            )

    return render(
        request,
        'editor/disks/details.html',
        {
            'disk': disk,
            'charges': charges,
            'total_charges': total_charges,
            'cost': '{:.2f}'.format(cost),
            'theorical_price': '{:.2f}'.format(theorical_price),
            'visual_path': '/editor/img/visuals/{}.jpg'.format(disk.ref_tm),
            'barcode_path': '/editor/img/barcodes/{}.png'.format(disk.ean),
        },
    )


@group_required('Editor')
def disk_update(request, **kwargs):
    """ Update a disk. """
    disk = Product.objects.get(pk=kwargs['pk'])

    if request.method == 'POST':
        form = DiskForm(request.POST, instance=disk)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'editor:disk_details',
                    kwargs={
                        'pk': disk.pk,
                    }
                )
            )

    else:
        form = DiskForm(instance=disk)

    return render(
        request,
        'editor/disks/form.html',
        {
            'form': form,
            'disk': disk,
        }
    )


@group_required('Editor')
def disk_delete(request, **kwargs):
    """ Delete a disk. """
    disk = Product.objects.get(pk=kwargs['pk'])

    if request.method == 'POST':
        form = DiskForm(request.POST, instance=disk)
        disk.delete()
        return HttpResponseRedirect(reverse('editor:disks_list'))

    form = DiskForm(instance=disk)

    return render(request, 'editor/disks/delete.html', {
        'form': form,
        'disk': disk,
    })
