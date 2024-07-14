import pandas as pd
import pickle
import os
from django.conf import settings
from sklearn.ensemble import RandomForestClassifier

def ValuePredictor(to_predict_list):
    model_path = os.path.join(settings.BASE_DIR, 'tree_model_final')
    f2 = open(model_path, 'rb')
    model = pickle.load(f2)
    params = to_predict_list
    df_params = pd.DataFrame([params])
    df_params = df_params.rename(columns={
        0: 'MatchHeadshots', 
        1: 'MatchKills', 
        2: 'MatchFlankKills', 
        3: 'MatchAssists',
        4: 'Survived'
    })
    resultado = ''
    if(model.predict(df_params)[0] == 1):
        resultado = 'EQUIPO GANADOR 😁'
    else:
        resultado = 'EQUIPO PERDEDOR 😥'
    return resultado