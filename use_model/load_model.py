import pickle
import xgboost as xgb



# def pred_loc():
#     with open('model_best_xgb(無做特徵縮減).pkl','rb') as f:
#         data = pickle.load(f)
#         model = xgb.XGBClassifier()
#         model.predict()
        
#         return 

def pred_loc():
    model = xgb.Booster()
    model.load_model('model_best_xgb(無做特徵縮減).pkl')
    y_pred = model.predict()