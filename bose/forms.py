
from django import forms

class BECParametersForm(forms.Form):
    alpha = forms.FloatField(
        label="Tilt Strength (α)",
        initial=0.05,
        min_value=0.0,
        max_value=1.0,
        help_text="Strength of linear potential (like gravity)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.01'
        })
    )
    g = forms.FloatField(
        label="Interaction Strength (g)",
        initial=0.5,
        min_value=0.01,
        max_value=2.0,
        help_text="How strongly atoms interact (repulsion)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.1'
        })
    )
    mu = forms.FloatField(
        label="Chemical Potential (μ)",
        initial=1.0,
        min_value=0.1,
        max_value=3.0,
        help_text="Energy cost to add atoms to condensate",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.1'
        })
    )