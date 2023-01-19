import pandas as pd

from elasticsearch import Elasticsearch


df = pd.read_csv('final_corpus.csv')


from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200", verify_certs=False, http_auth=['elastic', 'DwIbcCE_g==ZZt939WlG'])

# convert pandas dataframe to json then bulk upload


import json

def upload_to_elastic(df):
    for i in range(len(df)):
        es.index(index='songs', id=i, body=df.iloc[i].to_json())
    
upload_to_elastic(df)