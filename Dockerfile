# Utiliser une image de base Python
FROM python:3.11

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer un port si nécessaire (exemple pour une API Flask)
EXPOSE 5000

# Commande de démarrage
CMD ["python", "programme.py"]
