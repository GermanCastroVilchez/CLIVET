#encoding: utf-8
from django import forms

from django.utils.translation import ugettext_lazy as _, ugettext
from django.utils.text import capfirst, get_text_list
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div, Row, HTML
from crispy_forms.bootstrap import FormActions, TabHolder, Tab, \
    PrependedAppendedText, PrependedText, InlineRadios

from django.utils.timezone import get_current_timezone
from datetime import datetime

from apps.utils.forms import smtSave, btnCancel, btnReset

from ..models.mascota import Mascota, BOOL_GENERO, TIPO_MASCOTA, CONDICION

class MascotaForm(forms.ModelForm):
    """Tipo Documeto Form."""
    class Meta:
        """Meta."""
        model = Mascota
        exclude = ()
        fields = ['nombre','dueño','fecha_nacimiento','genero','especie','raza','color','esterelizado','descripcion',]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)

        super(MascotaForm, self).__init__(*args, **kwargs)

        self.fields['nombre'] = forms.CharField(
            label=capfirst(_(u'nombre')),
            required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
            u' '),
        )
        self.fields['fecha_nacimiento'] = forms.DateTimeField(
            label=_(u'Fecha Nacimiento'), required=False,
            initial=datetime.now().replace(tzinfo=get_current_timezone()),
            widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S',),
            input_formats=(
                '%d/%m/%Y', '%d/%m/%y', '%d-%m-%Y', '%d-%m-%y', '%Y-%m-%d',
                '%Y-%m-%d %H:%M:%S'),
            help_text=u'<small class="help-error"></small> %s' % _(
                u''),
        )
        self.fields['genero'] = forms.ChoiceField(
            label=capfirst(_(u'genero*:')), required=False,
            choices=BOOL_GENERO,
            widget=forms.RadioSelect(attrs={'default':'macho',}),
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['especie'] = forms.ChoiceField(
            label=capfirst(_(u'tipo Mascota')), required=False,
            choices=TIPO_MASCOTA,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['raza'] = forms.CharField(
            label=capfirst(_(u'raza')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['color'] = forms.CharField(
            label=capfirst(_(u'color')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['cond_corporal'] = forms.ChoiceField(
            label=capfirst(_(u'C. Corporal')), required=False,
            choices=CONDICION,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['esterelizado'] = forms.BooleanField(
            label=capfirst(_(u'¿Esterelizado?')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )

        self.fields['descripcion'] = forms.CharField(
            label=capfirst(_(u'Descripcion')), required=False,
            widget=forms.Textarea(attrs = {'rows': 4, }),

            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )

        self.helper = FormHelper()

        self.helper.form_method = 'post'
        self.helper.form_class = 'js-validate form-vertical form-mascota'
        self.helper.layout = Layout(
            Row(
                Div(
                    Field('nombre', placeholder="Introdusca el nombre de la mascota", css_class='input-required'),
                css_class="col-md-4"),
                Div(
                    Field('dueño', css_class="chosen-select select-medica", tabindex="6"),
                css_class='col-md-4'),
                Div(
                    Field('fecha_nacimiento', css_class='input-datex'),
                css_class="col-md-4"),
                ),
            Row(
                Div(
                    Field('especie',),
                css_class="col-md-3"),
                Div(
                    Field('raza',placeholder="Introdusca la raza",  css_class='input-required' ),
                css_class="col-md-3"),
                Div(
                    Field('color', placeholder="Introdusca el color", css_class='input-required'),
                css_class="col-md-3"),
                Div(
                    Field('cond_corporal', ),
                css_class="col-md-3"),
            ),
            Row(
                Div(
                    Div(
                        InlineRadios('genero', default="macho"),
                        Field('esterelizado',),
                    css_class='mascota-opcion'),
                css_class='col-md-3'),
                Div(
                    Field('descripcion', placeholder="Introdusca una cualidad de la mascota"),
                css_class='col-md-9'),
            ),
            Row(
                Div(
                    FormActions(
                        smtSave(),
                        btnCancel(),
                        btnReset(),
                    ),
                css_class="col-md-12 btn-controls"),
            ),
        )
