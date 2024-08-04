# Cryptographie App

## Description

Cryptographie App est une application graphique développée en Python utilisant Tkinter, permettant de chiffrer du texte avec plusieurs méthodes de cryptographie. Les méthodes de chiffrement disponibles incluent César, Vigenère, Substitution, Transposition, Vernam, Affine, Hill, RSA et XOR.

## Fonctionnalités

- **Chiffrement César**: Chiffre le texte en décalant chaque lettre par un nombre fixe de positions dans l'alphabet.
- **RSA**: Utilise les clés RSA pour chiffrer le texte de manière sécurisée.
- Autres méthodes de chiffrement sont disponibles mais non implémentées dans cette version.

## Prérequis

Avant d'exécuter l'application, assurez-vous d'avoir Python et les bibliothèques nécessaires installés. 

### Installation des Dépendances

1. **Clonez le dépôt**:
   ```bash
   git clone https://github.com/votre-utilisateur/cryptographie-app.git
   cd cryptographie-app
Créez un environnement virtuel (facultatif mais recommandé):

bash
Copier le code
python -m venv .venv
Activez l'environnement virtuel:

Sous Windows:
bash
Copier le code
.venv\Scripts\activate
Sous macOS/Linux:
bash
Copier le code
source .venv/bin/activate
Installez les dépendances:

bash
Copier le code
pip install -r requirements.txt
Dépendances
Les dépendances nécessaires sont listées dans le fichier requirements.txt. Voici les principales :

cryptography
tkinter (incluse par défaut avec Python)
Utilisation
Exécutez l'application:

bash
Copier le code
python aa.py
Interface Utilisateur:

Sélectionnez une méthode de chiffrement depuis le menu.
Entrez le texte que vous souhaitez chiffrer.
Cliquez sur "Chiffrer" pour obtenir le texte chiffré.
Utilisez le bouton "Retour" pour revenir au menu de sélection des méthodes de chiffrement.
Captures d'Écran
Ajoutez ici des captures d'écran de votre application pour montrer à quoi elle ressemble.

Contribuer
Si vous souhaitez contribuer à ce projet :

Faites un fork du dépôt.
Créez une branche pour votre fonctionnalité ou correctif :
bash
Copier le code
git checkout -b ma-fonctionnalite
Faites vos modifications et committez :
bash
Copier le code
git commit -am 'Ajoute une nouvelle fonctionnalité'
Poussez vos modifications :
bash
Copier le code
git push origin ma-fonctionnalite
Créez une pull request.
Auteurs
Votre Nom - Développeur principal
Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
