import sys
import os
import joblib
import pandas as pd
from sklearn.metrics import f1_score, accuracy_score, recall_score,precision_score,roc_auc_score
import tqdm
import argparse
import pickle
from DataPreaparators import PreProcess, create_patients_df
import random
import warnings
warnings.filterwarnings('ignore')


if __name__ == "__main__":

    test_files= sys.argv[1] #getting directory path
    patients_list = os.listdir(test_files) # Files names list in the given directory
    test_df = create_patients_df(patients_list,test_files) # create dataframe
    test_df.to_csv('test.csv',index=False)
    del test_df
    del patients_list
    test_df = pd.read_csv('test.csv') # create dataframe
    preprocessor= PreProcess(df=test_df, imputer_path='Trained Models/knn_imputer') #Preprocess the dataframe - aggregations and imputing
    model = joblib.load('Trained Models/best_XGB_run3_43') #load model
    with open(f'Trained Models/Best_features_dict_XGB_run_4.pickle', 'rb') as handle:
        features_dict = pickle.load(handle)
    features = features_dict[43]
    random.seed(0)
    y_pred = model.predict(preprocessor.X[features]) #predict
    ##calculate measures
    print('F1 Score: ',f1_score(preprocessor.y,y_pred))
    print('Accuracy Score: ',accuracy_score(preprocessor.y,y_pred))
    print('Recall Score: ',recall_score(preprocessor.y,y_pred))
    print('Precision Score: ',precision_score(preprocessor.y,y_pred))
    print('roc_auc Score: ',roc_auc_score(preprocessor.y,y_pred))

    #create df and write to csv
    final_results =preprocessor.IDS
    final_results['SepsisLabel'] = y_pred
    final_results[['ID','SepsisLabel']].to_csv('prediction.csv',header=False, index=False)