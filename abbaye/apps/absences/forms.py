""" apps/absences/forms.py """

from django import forms
from django.core.exceptions import ValidationError

from apps.moines.models import Monk
from .models import Ticket

MOMENTS = [
    ('', ''),
    ('Matin', 'Matin'),
    ('Déjeuner', 'Déjeuner'),
    ('Après-midi', 'Après-midi'),
    ('Dîner', 'Dîner'),
    ('Soirée', 'Soirée'),
]
BY = [
    ('', ''),
    ('Voiture', 'Voiture'),
    ('Train', 'Train'),
]
STATIONS = [
    ('', ''),
    ('Les Laumes', 'Les Laumes'),
    ('Montbard', 'Montbard'),
]


class AdditionalRecipients(forms.ModelMultipleChoiceField):
    """ Override label. """

    def label_from_instance(self, obj):
        """
        Convert objects into strings and generate the labels for the choices
        presented by this object. Subclasses can override this method to
        customize the display of the choices.
        """
        return '<b>{}</b> ({})'.format(obj.name, obj.email)


class TicketForm(forms.ModelForm):
    """ Ticket form Ticket. """
    type = forms.ChoiceField(
        choices=[
            ('out', 'Billet d\'absence = Je pars de Flavigny puis je reviens à Flavigny.'),
            ('in', 'Billet de présence = Je passe à Flavigny puis je repars.'),
        ],
        widget=forms.RadioSelect(
            attrs={
                'id': 'id_type',
                'class': 'list-unstyled d-flex flex-column align-items-start mx-auto',
            }
        ),
    )
    monks = forms.ModelMultipleChoiceField(
        queryset=Monk.objects.filter(
            is_active=True
        )
        .order_by('absolute_rank', 'entry', 'rank_entry'),
        widget=forms.CheckboxSelectMultiple(),
        error_messages={
            'required': 'Veuillez sélectionner au moins 1 moine.',
        },
    )
    destination = forms.CharField(
        required=False,
        widget=forms.TextInput(),
    )
    go_date = forms.DateField(
        error_messages={
            'required': 'Ce champ est obligatoire.',
        },
    )
    go_moment = forms.ChoiceField(
        required=False,
        choices=MOMENTS,
    )
    servants = forms.BooleanField(
        required=False,
    )
    picnic = forms.BooleanField(
        required=False,
        label='Casse-croûte',
        label_suffix=''
    )
    go_by = forms.ChoiceField(
        required=False,
        choices=BY,
    )
    go_station = forms.ChoiceField(
        required=False,
        choices=STATIONS,
    )
    go_hour = forms.TimeField(
        required=False,
        input_formats=[
            '%H:%M',
        ],
        help_text='Format : HH:MM, merci.',
    )
    ordinary_form = forms.BooleanField(
        required=False,
    )
    back_date = forms.DateField(
        error_messages={
            'required': 'Ce champ est obligatoire. Si vous ne connaissez pas la date de votre retour, entrez une date approximative et indiquez-le en commentaire.',
        },
    )
    back_moment = forms.ChoiceField(
        required=False,
        choices=MOMENTS,
    )
    keep_hot = forms.BooleanField(
        required=False,
        label='Garder du chaud',
        label_suffix=''
    )
    back_by = forms.ChoiceField(
        required=False,
        choices=BY,
    )
    back_station = forms.ChoiceField(
        required=False,
        choices=STATIONS,
    )
    back_hour = forms.TimeField(
        required=False,
        input_formats=[
            '%H:%M',
        ],
        help_text='Format : HH:MM, merci.',
    )
    commentary = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Tapez ici toutes vos remarques, et n\'oubliez pas de signer si votre identité n\'est pas évidente.',
            }
        ),
    )
    additional_recipients = AdditionalRecipients(
        required=False,
        queryset=Monk.objects
        .filter(absences_recipient=False)
        .filter(is_active=True)
        .exclude(email='')
        .exclude(email=None)
        .order_by('absolute_rank', 'entry', 'rank_entry'),
        widget=forms.CheckboxSelectMultiple(),
        help_text='Cochez les moines supplémentaires à qui vous souhaitez faire parvenir ce message.',
    )

    class Meta:
        model = Ticket
        fields = '__all__'

    def clean_back_date(self):
        """ Function to check that back date isn't before go date. """
        if 'go_date' in self.cleaned_data.keys() \
                and self.cleaned_data['go_date'] > self.cleaned_data['back_date']:
            raise ValidationError(
                'La date de retour est antérieure à la date de départ !'
            )
        return self.cleaned_data['back_date']
