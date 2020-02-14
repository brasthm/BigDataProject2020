from paramiko import SSHClient
from paramiko import AutoAddPolicy
import argparse
import os
import sys
import time
import pandas as pd
import pymongo
import json


#file_in = "make_prediction.py"
file_in = "predict.csv"
if (len(sys.argv)==1):
    file_in = "../dataset/predict.csv"
else:
    file_in = sys.argv[1]
    
file_out = os.path.splitext(file_in)[0] + "Complet"+ os.path.splitext(file_in)[1]


# on fait la connection SSH avec la machine AWS
ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect("ec2-18-232-97-24.compute-1.amazonaws.com", username ="ec2-user", key_filename = "bigDataProject.pem")
#on ouvre la connection SFTP
ftp = ssh.open_sftp()


# on envoie le fichier 
ftp.put(file_in, "files/" + os.path.basename(file_in))

# on execute le script
ssh.exec_command("python make_prediction.py files/" + os.path.basename(file_in) + " files/" + os.path.basename(file_out))

# on recupere le nouveau fichier
time.sleep(0.5)

ftp.get("files/" + os.path.basename(file_out), file_out)

# on supprime d'aws le fichier non traité
if (file_in != file_out):
    ssh.exec_command("rm files/" + os.path.basename(file_in))

# on ferme les connectione
ftp.close()
ssh.close()


# fonction pour envoyer le fichier csv sur mongo
def import_csvfile(filepath):
 mng_client = pymongo.MongoClient('localhost', 27017)
 mng_db = mng_client['Big_Data'] # Replace mongo db name
 Nom = ['Insurance0','Insurance1','Insurance2','Insurance3','Insurance4','Insurance5','Insurance6','Insurance7','Insurance8']
 for i in range (9) :
     collection_name = Nom[i] # Replace mongo db collection name
     db_cm = mng_db[collection_name]
     data = pd.read_csv(filepath, error_bad_lines=False)
     data = data.loc[data['Response']==i]
     if data.size!=0:
         data_json = json.loads(data.to_json(orient='records'))
         db_cm.remove()
         db_cm.insert_many(data_json)
 
import_csvfile(file_out)

# on supprime le fichier traité de notre machine
os.remove(file_out)



