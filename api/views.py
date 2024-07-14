from django.shortcuts import render
from .forms import Tree_Model
from .predictor import ValuePredictor

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = Tree_Model(request.POST)
        if form.is_valid():

            MatchHeadshots = form.cleaned_data['MatchHeadshots'] 
            MatchKills = form.cleaned_data['MatchKills']
            MatchFlankKills = form.cleaned_data['MatchFlankKills']
            MatchAssists = form.cleaned_data['MatchAssists']
            Survived = form.cleaned_data  ['Survived']

            to_predict_list = [MatchHeadshots, MatchKills, MatchFlankKills, MatchAssists, Survived]

            resultado = ValuePredictor(to_predict_list)

            return render(request, 'modeloML/index.html', {'form': form, 'resultado': resultado})

    else:
        form = Tree_Model()
    return render(request, 'modeloML/index.html', {'form':form})
