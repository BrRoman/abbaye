""" apps/imprimerie/views_memo.py """

import markdown as md

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.main.decorators import group_required
from .models import Memo
from .forms import MemoForm


@group_required('Imprimerie')
def memo(request):
    """ Memo imprimerie. """
    markdown = Memo.objects.first().content
    html = md.markdown(
        markdown,
        extensions=['markdown.extensions.fenced_code']
    )
    return render(
        request,
        'imprimerie/memo/memo.html',
        {
            'html': html,
        },
    )


@group_required('Imprimerie')
def memo_update(request):
    """ Update Memo imprimerie. """
    content = Memo.objects.first()
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=content)
        if form.is_valid():
            content.save()
            return HttpResponseRedirect(
                reverse(
                    'imprimerie:memo',
                )
            )

    else:
        form = MemoForm(instance=content)

    return render(
        request,
        'imprimerie/memo/form.html',
        {
            'form': form,
            'content': content,
        }
    )