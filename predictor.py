import numpy as np
import pickle


#load models
try :
    with open('crop_encoding.pkl', 'rb' ) as f:
        crop_encoding = pickle.load(f)
except FileNotFoundError:
    raise FileNotFoundError('Critical file "crop_encoding.pkl" not found ')

try:
    with open('state_encoding.pkl', 'rb') as f:
        state_encoding = pickle.load(f)
except FileNotFoundError:
    raise FileNotFoundError('Critical file "state_encoding.pkl" not found ')

try:
    with open('yield_model.pkl', 'rb') as f:
        yield_model = pickle.load(f)
except FileNotFoundError:
    raise FileNotFoundError('Critical file "yield_model.pkl" not found ')


valid_crops = list(crop_encoding.index)
valid_states = list(state_encoding.index)



def encode_crop_state(crop, state):
    
    crop_encoded = crop_encoding[crop]
    state_encoded = state_encoding[state]

    return crop_encoded, state_encoded

def encode_season(season):

    season_rabi = 1 if season == "Rabi" else 0
    season_summer = 1 if season == "Summer" else 0
    season_whole_year = 1 if season == "Whole Year" else 0

    return season_rabi, season_summer, season_whole_year

def build_features(crop_encoded, year, state_encoded, area,
           rainfall, fertilizer, pesticide,
           season_rabi, season_summer, season_whole_year):
    input_array = np.array([[crop_encoded, year, state_encoded, area,
           rainfall, fertilizer, pesticide,
           season_rabi, season_summer, season_whole_year]])
    
    return input_array

def predict(crop, season, state, year, rainfall, area, fertilizer, pesticide):
    crop_encoded, state_encoded = encode_crop_state(crop, state)
    season_rabi, season_summer, season_whole_year = encode_season(season)
    features = build_features(crop_encoded, year, state_encoded, area,
                            rainfall, fertilizer, pesticide,
                            season_rabi, season_summer, season_whole_year)

    predicted_value = yield_model.predict(features)[0]
    total_production = predicted_value * area
    total_quintal = total_production * 10

    return predicted_value, total_production, total_quintal


