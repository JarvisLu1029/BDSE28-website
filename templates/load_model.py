import pickle
import xgboost



def pred_loc():
    with open('model_best_xgb(無做特徵縮減).pkl','rb') as f:
        data = pickle.load(f)
    
        
        
        return 