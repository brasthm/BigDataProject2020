import pandas as pd
import pymongo
import json
import os
 
def import_csvfile(filepath):
 mng_client = pymongo.MongoClient('localhost', 27017)
 mng_db = mng_client['Big_Data'] # Replace mongo db name
 collection_name = 'Insurance' # Replace mongo db collection name
 db_cm = mng_db[collection_name]

 data = pd.read_csv(filepath, error_bad_lines=False)
 data_json = json.loads(data.to_json(orient='records'))
 db_cm.remove()
 db_cm.insert(data_json)
     
import_csvfile("C://Users//Etienne//Documents//FISE3//Projet BigData//BigDataProject2020//README.md")
