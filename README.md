# BigDataProject2020

le fichier "creer_EC2.py" lance une nouvelle instance aws /!\ à ne lancer qu'une fois

Le fichier "mainBigData.py" est le fichier principal sur la machine client
il s'appelle avec "python mainBigData.py <PATHNAME>" avec <PATHNAME> l'emplacement du fichier a traiter.
Il sera créé un fichier au meme endroit que <PATHNALE> suivi de "Complet".
Par exemple "python mainBigData.py ../dataset/predict.csv" créera un fichier "predictComplet.csv" dans le dossier "dataset".

Le fichier "bigDataProject.pem" est la clée utilisée par "mainBigData.py" pour se connecter a aws.

Le fichier "make_prediction.py" est le fichier principal sur le serveur pour classifier les utilisateurs.

Le fichier "finalized_model2.sav" est le fichier sur le serveur qui contient le model d'apprentissage. Il est appelé par "make_prediction.py" pour faire les prédictions