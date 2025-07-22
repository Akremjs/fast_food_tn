# fast_food_tn
module Fast-Food Tunisien

 un fast-food tunisien est un excellent projet, car il vous permettra de gérer les commandes, le stock, les ventes, la caisse, et éventuellement la gestion du personnel. Je vais vous donner une structure simple et claire pour démarrer votre module Odoo.
 
 
 
 
 Objectif fonctionnel
Gérer les commandes clients avec :

Nom du client

Date de commande

Lignes de commande (produit, quantité, prix)

Calcul automatique du total

Génération automatique d’un numéro de commande (FFTN-00001, etc.)

📁 Structure du module
pgsql
Copier
Modifier
fast_food_tn/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── fast_food_order.py
├── views/
│   └── fast_food_order_views.xml
├── data/
│   └── sequence.xml
├── security/
│   └── ir.model.access.csv
