""" apps/absences/models.py """

import datetime

from django.db import models

from apps.moines.models import Monk


class Ticket(models.Model):
    """ Ticket class. """
    type = models.CharField(
        max_length=25,
    )
    monks = models.ManyToManyField(
        Monk,
        related_name='monks',
    )
    destination = models.TextField(
        null=True,
    )
    go_date = models.DateField(
        null=True,
    )
    go_moment = models.CharField(
        max_length=25,
        null=True,
    )
    servants = models.BooleanField(
        null=True,
    )
    picnic = models.BooleanField(
        null=True,
    )
    go_by = models.CharField(
        max_length=25,
        null=True,
    )
    go_station = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )
    go_hour = models.TimeField(
        null=True,
        blank=True,
    )
    back_date = models.DateField()
    back_moment = models.CharField(
        max_length=25,
        null=True,
    )
    keep_hot = models.BooleanField()
    back_by = models.CharField(
        max_length=25,
        null=True,
    )
    back_station = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )
    back_hour = models.TimeField(
        null=True,
        blank=True,
    )
    ordinary_form = models.BooleanField(
        null=True,
    )
    commentary = models.TextField(
        null=True,
        blank=True,
    )
    additional_recipients = models.ManyToManyField(
        Monk,
        related_name='additional_recipients',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

    def monks_as_string(self):
        """ String containing all the monks of this ticket. """
        return ', '.join(
            monk.__str__() for monk in self.monks.all()
            .order_by('absolute_rank', 'entry', 'rank_entry')
        )

    def additional_recipients_as_string(self):
        """ String containing all the additional recipients of this ticket. """
        return '</br>'.join(
            (monk.__str__() + ' (' + monk.email + ')')
            for monk in self.additional_recipients.all()
            .order_by('entry', 'rank_entry')
        )

    def is_past(self):
        """ Boolean: Is the ticket in the past? """
        return self.back_date < datetime.date.today()

    def __str__(self):
        dates = '{:02}/{:02}/{}-{:02}/{:02}/{}'.format(
            self.go_date.day,
            self.go_date.month,
            self.go_date.year,
            self.back_date.day,
            self.back_date.month,
            self.back_date.year
        )
        dates = dates.split('-')[0] \
            if self.back_date == self.go_date \
            else dates
        monks = self.monks_as_string() \
            if len(self.monks.all()) == 1 \
            else '{} et alii'.format(self.monks_as_string().split(',')[0])
        return '{} ({})'.format(
            monks,
            dates,
        )
