import pandas as pd
import pymongo
import json
import os
 
def import_csvfile(filepath):
 mng_client = pymongo.MongoClient('localhost', 27017)
 mng_db = mng_client['Big_Data'] # Replace mongo db name
 collection_name = 'Insurance' # Replace mongo db collection name
 db_cm = mng_db[collection_name]
 cdir = os.path.dirname(_file_)
 file_res = os.path.join(cdir, filepath)
 data = pd.read_csv(file_res, error_bad_lines=False)
 data_json = json.loads(data.to_json(orient='records'))
 db_cm.remove()
 db_cm.insert(data_json)
     
if _name_ == "_main_":
 filepath = 'C://Users//guill//Desktop//TSE//cours//Fise 3//Big data//Projet//train.csv' # pass csv file path
 import_csvfile(filepath)
