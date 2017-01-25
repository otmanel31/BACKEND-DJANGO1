# Marche à suivre

## Forker le projet *BACKEND-Introduction to Django*
Le cloner ensuite sur la machine locale

## Créer un environnement virtuel, y installer Django 1.10
```bash
virtualenv -p python3 venv-nutrition
source venv-nutrition/bin/activate
pip install django
```

## Créer un projet Django dans ce répertoire
```bash
django-admin --help
django-admin startproject nutrition
cd nutrition
```

## Modifier le fichier *nutrition/nutrition/settings.py* selon les besoins
Si on change rien, BD = db.sqlite3

## Créer une migration initiale qui va créer les tables d'administration dans la base
```bash
python manage.py migrate
```

## Vérifier que tout est en place
```bash
python manage.py runserver
```
Ouvrir un navigateur à l'url : http://127.0.0.1:8000


## Créer une 'application' (au sens Django) appelée 'aliments'
```bash
python manage.py startapp aliments
```

## Afficher les schémas de la base de données fournie
```bash
sqlite3 stripped_ctdit_v11.db
> .schema
```

## Créer ~nutrition/aliments/models.py~ à partir de ces schémas
Voir fichier joints

## Ajouter l'application ~aliments~ à ~INSTALLED_APPS~ dans settings.py

## Créer et appliquer la migration associée à la création des nouveaux modèles
```bash
python manage.py makemigrations aliments
python manage.py migrate
```

## Faire un dump des tables de la BD fournies en re-ordonnant les champs
```bash
sqlite3 db.sqlite3
> .schema
...
^D
cd ..
sqlite3 stripped_ctdit_v11
> .output nutriment.dat
> select nutr_no,ifda_no,unit,tagname,nom from nutrieduc_nutriment;
> .output aliment.dat
> select id,shrt_desc,long_desc,ctdit_no,note,maxqty,pict,brand,israw,packpict,keywords from nutrieduc_aliment;
> .output portionaliment.dat
> select id,poids,nom,note,pict,aliment_id from nutrieduc_portionaliment;
> .output nutdata.dat
> select id,val,source,note,aliment_id,nutriment_id from nutrieduc_nutdata;
> ^D
```

## Importer ces données dans la base Django
```bash
cd nutrition
sqlite3 db.sqlite3
> .import nutriment.dat aliments_nutriment
> .import aliment.dat aliments_aliment
> .import portionaliment.dat aliments_portionaliment
> .import nutdata.dat aliments_nutdata
```

## Créer un super-utilisateur pour le site d'administration
```bash
python manage.py createsuperuser
```


## Tester le site d'administration
```bash
python manage.py runserver
```
Ouvrir un navigateur à l'url : http://127.0.0.1:8000

