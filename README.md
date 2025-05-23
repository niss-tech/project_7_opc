﻿# AlgoInvest&Trade - Optimisation d'investissements en Python

Ce projet vise à développer un algorithme d'investissement performant pour maximiser les bénéfices d'un portefeuille d'actions dans un budget limité. Il comprend deux versions : une solution **brute-force** et une solution **optimisée** utilisant la **programmation dynamique**.

---

## Contexte
L'objectif est de trouver la meilleure combinaison d'actions à acheter pour maximiser les bénéfices après **2 ans**, avec les contraintes suivantes :
- Chaque action ne peut être achetée qu'une seule fois.
- Il n'est pas possible d'acheter une fraction d'action.
- Le budget maximal est de **500 euros**.

---

## Fonctionnalités
- **Lecture de fichiers CSV** pour récupérer les données des actions.
- **Solution brute-force** : explore toutes les combinaisons possibles.
- **Solution optimisée** : utilise la **programmation dynamique** pour un calcul rapide.
- Affichage du **coût total**, du **profit total**, et des **actions sélectionnées**.
- Gestion des erreurs pour garantir la robustesse du programme.

---

## Structure du projet
```
 AlgoInvest&Trade
├── Liste_actions.csv       # Liste d'actions fournie (données)
├── brute_force.py          # Solution brute-force
├── optimized.py            # Solution optimisée (rapide et efficace)
├── README.md               # Instructions et présentation du projet
```

---

## Installation

### 1️/ **Cloner le repository**
```bash
git clone https://github.com/niss-tech/project_7_opc.git
cd project_7_opc
```

### 2️/ **Installer Python**
Assurez-vous que **Python 3.12** (ou version ultérieure) est installé.  
[Télécharger Python ici](https://www.python.org/downloads/)

### 3️/ **Installer les dépendances**
Aucune dépendance externe requise pour ce projet.  
Les modules utilisés (`csv`, `itertools`) sont inclus nativement dans Python.

---

## Utilisation

### ➤ **Exécuter la solution brute-force**
```bash
python brute_force.py
```

### ➤ **Exécuter la solution optimisée**
```bash
python optimized.py
```

---

## Exemple de résultats

```
 Meilleure combinaison brute-force :
Action-2 - Coût : 30.0€ - Bénéfice : 3.0€
Action-4 - Coût : 70.0€ - Bénéfice : 14.0€
Action-10 - Coût : 34.0€ - Bénéfice : 9.18€

 Coût total : 134.00€
 Profit total : 26.18€
```


## Explication du choix des algorithmes
### **Brute-force**
- Teste **toutes les combinaisons possibles** pour garantir le résultat optimal.
- Convient uniquement pour de **petits ensembles de données** (≤ 20 actions).

### **Optimisé (programmation dynamique)**
- Utilise une **table de résultats intermédiaires** pour éviter de recalculer plusieurs fois les mêmes combinaisons.
- Permet de traiter efficacement **des centaines d'actions** tout en trouvant la solution optimale.
