from paramiko import SSHClient
from paramiko import AutoAddPolicy
import argparse
import os
import sys
import time


#file_in = "make_prediction.py"
file_in = "predict.csv"
if (len(sys.argv)==1):
    file_in = "predict.csv"
else:
    file_in = sys.argv[1]
    
file_out = os.path.splitext(file_in)[0] + "Complet"+ os.path.splitext(file_in)[1]



# on fait la connection SSH avec la machine AWS
ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect("ec2-18-232-97-24.compute-1.amazonaws.com", username ="ec2-user", key_filename = "bigDataProject.pem")
#on ouvre la connection SSH
ftp = ssh.open_sftp()


# on envoie le fichier 
ftp.put(file_in, "files/" + os.path.basename(file_in))

# on execute le script
ssh.exec_command("python make_prediction.py files/" + os.path.basename(file_in) + " files/" + os.path.basename(file_out))

# on recupere le nouveau fichier
time.sleep(0.5)

ftp.get("files/" + os.path.basename(file_out), file_out)
if (file_in != file_out):
    ssh.exec_command("rm files/" + os.path.basename(file_in))
ftp.close()
ssh.close()




