""" apps/moines/forms.py """

from django import forms

from .models import Monk


class MonkForm(forms.ModelForm):
    """ Monk form.
    Required fields: name and entry. """
    name = forms.CharField(
        max_length=255,
        label='Nom',
        label_suffix=' :',
    )
    # civil_first_name = forms.CharField(
    #     max_length=255,
    #     label='Prénom civil',
    #     label_suffix=' :',
    # )
    # civil_last_name = forms.CharField(
    #     max_length=255,
    #     label='Nom civil',
    #     label_suffix=' :',
    # )
    # Dates:
    birthday = forms.DateField(
        required=False,
        label='Date de naissance',
        label_suffix=' :',
    )
    entry = forms.DateField(
        label='Date d\'entrée',
        label_suffix=' :',
    )
    rank_entry = forms.IntegerField(
        required=False,
        label='Rang',
        label_suffix=' :',
        help_text='Si plusieurs moines sont entrés le même jour, indiquez ici leur rang (1 pour le premier, 2 pour le deuxième etc.).',
        initial=1,
    )
    habit = forms.DateField(
        required=False,
        label='Date de prise d\'habit',
        label_suffix=' :',
    )
    profession_temp = forms.DateField(
        required=False,
        label='Date de profession temporaire',
        label_suffix=' :',
    )
    profession_perp = forms.DateField(
        required=False,
        label='Date de profession perpétuelle',
        label_suffix=' :',
    )
    priest = forms.DateField(
        required=False,
        label='Date d\'ordination sacerdotale',
        label_suffix=' :',
    )
    death = forms.DateField(
        required=False,
        label='Date de décès',
        label_suffix=' :',
    )
    feast_day = forms.ChoiceField(
        choices=[(i+1, i+1) for i in range(31)],
    )
    feast_month = forms.ChoiceField(
        choices=[
            (1, 'janvier'),
            (2, 'février'),
            (3, 'mars'),
            (4, 'avril'),
            (5, 'mai'),
            (6, 'juin'),
            (7, 'juillet'),
            (8, 'août'),
            (9, 'septembre'),
            (10, 'octobre'),
            (11, 'novembre'),
            (12, 'décembre'),
        ],
    )
    # Informations:
    laundry_number = forms.IntegerField(
        label='Numéro de linge',
        label_suffix=' :',
    )
    phone_number = forms.IntegerField(
        label='Numéro de téléphone',
        label_suffix=' :',
    )
    email = forms.EmailField(
        required=False,
        label='Email',
        label_suffix=' :',
    )
    additional_email = forms.EmailField(
        required=False,
        label='Email supplémentaire',
        label_suffix=' :',
    )
    # Admin fields:
    absolute_rank = forms.IntegerField(
        label='Rang absolu',
        label_suffix=' :',
    )
    is_abbot = forms.BooleanField(
        required=False,
        label='Est le TRP Abbé.',
        label_suffix='',
    )
    is_prior = forms.BooleanField(
        required=False,
        label='Est le RP Prieur.',
        label_suffix='',
    )
    is_abbot_emerite = forms.BooleanField(
        required=False,
        label='Est le TRP Abbé émérite.',
        label_suffix='',
    )
    is_active = forms.BooleanField(
        required=False,
        label='Est actif.',
        label_suffix='',
    )
    absences_recipient = forms.BooleanField(
        required=False,
        label='Est un destinataire <i>ex officio</i> des avis d\'absence.',
        label_suffix='',
    )

    class Meta:
        model = Monk
        fields = '__all__'
