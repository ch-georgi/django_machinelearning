from django import forms

CHOICES = [(1,'True'),(0,'False')]

class Tree_Model(forms.Form):
    MatchHeadshots = forms.IntegerField(required=True,) 
    MatchKills = forms.IntegerField(required=True,)
    MatchFlankKills = forms.IntegerField(required=True,)
    MatchAssists=forms.IntegerField(required=True,)
    Survived=forms.IntegerField(required=True, widget=forms.RadioSelect(choices=CHOICES))