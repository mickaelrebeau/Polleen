<h1 align="center">
  <img alt="polleen" src="https://user-images.githubusercontent.com/75978618/170478814-56bf7a69-85e1-46ca-b532-d7951f839fd7.png" width="896px"/><br/>
  Logiciel CRM développer avec Django pour Pollen
</h1>

⚠️ Ce projet est développé sous windows. Il n'a pas été testé sur d'autres systèmes d'exploitation.

🚨 **Il est impératif de savoir utilisé [Django](https://docs.djangoproject.com/en/4.0/) pour continué ce project.**

# ⚡️installation
Utilisez la commande git clone pour installer le projet

```bash
git clone https://github.com/Mike97310/Polleen.git
```

Une fois le projet installé, exécutez la commande [pip](https://pip.pypa.io/en/stable/) afin d'installer le fichier requirements.txt

```bash
pip install -r requirements.txt
```

Voilà l'installation est terminé ! 🎉

# ⚙️ Pour commencer
La première chose à faire pour que le projet fonctionne correctement, c'est de se rendre dans le fichier 0.env et de renseigner les informations necessaire.

![0.env](https://user-images.githubusercontent.com/75978618/170491164-1e180c54-a56a-4713-950b-679fea71e256.png)

Voici un **[lien](https://djecrety.ir/)** pour génerer des secret keys pour django.

Vous pouvez utilisez la base de données que vous souhaitez.

⚠️ Il est nécessaire de renseigner un compte LinkedIn afin que le système de recommandation se lance correctement.

# 👀 Aperçu

✍ A noté que ces aperçu peuvent ne plus être d'actualité !

![Home](https://user-images.githubusercontent.com/75978618/170492654-bae98549-1279-4ce1-b4f1-f02ca385524a.png)
![Repertory](https://user-images.githubusercontent.com/75978618/170493474-f039f259-ebe9-4eed-8469-4b84de2b9000.png)
![PublicRepertory](https://user-images.githubusercontent.com/75978618/170493144-edf2dddf-b624-4458-837f-846131e28f0c.png)
![IA](https://user-images.githubusercontent.com/75978618/170493573-cc83f036-faaf-4c21-a984-c9d743e8346f.png)
![Documentation](https://user-images.githubusercontent.com/75978618/170493972-24168cf4-f16b-4c3c-b038-fa9fabd4f994.png)

# 🍯 Composition
Le CRM est composé de plusieurs parties principales:
  - Polleen
  - Agents
  - Docs
  - IA
  - Leads

Le dossier templates sert à stocké les différentes vues de bases du projet.
Le dossier static sert à stocké les différents éléments statiques du projet (CSS, JS, Images, etc..).

## 🐝 Polleen
Pollen est la partie administrateur du CRM.

Vous n'avez pas à renseigner le **DEBUG** et la **SECRET_KEY** dans le fichier settings.py puisque cette donnée provient du fichier .env

```python
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
```

Il en est de même pour la connection a la base de données. Ici, c'est de PostgreSQL.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}
```

## ⚔️ Agents
Agents est la partie qui gère les admins vous pouvez ajouter et supprimer des admins. Elle n'est pas visible sur le CRM.

Pour y avoir accès, il suffit de faire **"127.0.0.1:8000/agents"** dans votre barre de recherche lorsque le serveur est lancé.

Si le projet possède un nom de domaine alors il faudra le renseigner à la place de **127.0.0.1:8000**.

## 🗄 Docs
Docs est la partie où l'on retrouve l'historique des présentations Pollen.

## 🤖 IA, système de recommandation
IA est la partie consacré au système de recommendation.

## 👥 Leads
Leads est la partie qui s'occuper du répertoire et du répertoire public. Mais elle s'occupe également de quelques 
éléments supplémentaires que nous verrons dans le fichier leads/view.py.
