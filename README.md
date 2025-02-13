<img src='https://the-public-domain-review.imgix.net/collections/w-e-b-du-bois-hand-drawn-infographics-of-african-american-life-1900/32764473915_e36c65737e_o.jpg?fit=max&w=1024&h=850&auto=format,compress'/>

# Introduction

Présentation du projet.#duboischallenge2005

# Structure

Les données uniquement non sensibles sont sur le github pour des soucis de confidentialité. 

On trouve les données brutes dans le dossier `data/raw`, données partagées par `DVS`, et par .d pour le `mirror`. 
On trouve dans `sources` les modules créés pour ce projet.
On trouve dans `model` les modeles de ML.
Les données pour les quelles, on souhaite faire des prédictions se trouvent dans le dossier `data/test`.
On trouve dans le dossier `rapport` les éléments nécessaires pour DVS. présentation, dont éléments pour intégration `html`.

# Exécutables

* `challenge{x}.py` va traiter les données brutes (`data/raw`) et créer une `visualisation` exportable, interprétée du travail orignal de W.E.B. Du Bois. #duboischallenge2005

* `mirror{x}.py` crée une visualisation sur la base du modele de `challenge{x}.py` mais traitant d'un big challenges / défi actuel.

* `predict{x}.py` utilise les dataframes de `challenge{x}.py` `mirror{x}.py` afn de prédire une visuation sur une thématique similaire.

# Utilisation

as you wish :)
