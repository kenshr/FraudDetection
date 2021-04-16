# Testing ML model on test sample data
import numpy as np
import pandas as pd
import pickle
import pipeline as p

def predict(new_data):
  # Load in pickled model
  with open('model_2.pkl', 'rb') as f:
    model = pickle.load(f)

  # read in sample data and store as dataframe
  df = pd.json_normalize(new_data)

  # preprocess sample
  sample_clean = p.preprocess(df).prep()

  # REMOVE WHEN LIVE WITH API (data will never have label information)
  if  'acct_type' in sample_clean.columns.to_list():
    sample_clean.drop('acct_type', axis=1, inplace=True)

  # REMOVE IF/WHEN WE DEBUG PIPELINE (Removes if there's an extra column (bug??))
  if sample_clean.shape[0] > 1:
    sample_clean.drop(0, axis=0,inplace=True)

  # schema that model was trained on
  schema = ['delivery_method','fb_published','has_analytics',
            'has_header','has_logo','name_length','num_order','num_payouts',
            'org_facebook','org_twitter','show_map','user_type','approx_payout_date',
            'body_length','channels','event_created','event_end','event_published',
            'event_start','gts','sale_duration','sale_duration2','user_age',
            'venue_latitude','venue_longitude','currency_CAD','currency_EUR',
            'currency_GBP','currency_MXN','currency_NZD','currency_USD','listed_y',
            'payout_type_ACH','payout_type_CHECK']

  # create df with sample data with appropriate schema
  final = pd.DataFrame(data=sample_clean, columns=schema)
  # fill NaNs
  final.fillna(0, inplace=True)
  # separate features and label
  X = final.copy()
  return model.predict_proba(X)


if __name__ == '__main__':
  pass
