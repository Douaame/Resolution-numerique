# 📐 Comparaison de Méthodes Numériques (Projet Python)

Ce dépôt contient un **projet universitaire**, développé dans le cadre du module **Analyse Numérique**.  
Il s'agit d'un programme **en Python**, qui implémente et compare trois méthodes de résolution d'équations non linéaires.

---

## ✨ Fonctionnalités

- ✂️ **Méthode de Dichotomie** — Recherche par bissection sur un intervalle donné  
- 🔁 **Méthode du Point Fixe** — Itération d'une fonction contractante `g(x)`  
- ⚡ **Méthode de Newton-Raphson** — Convergence quadratique via la dérivée `f'(x)`  
- 📊 **Visualisation des erreurs** — Courbes de convergence pour chaque méthode  
- 📈 **Comparaison globale** — Graphique superposé des trois méthodes  
- 🔢 **Calcul de l'ordre de convergence** — Estimation numérique de l'ordre `p`  

---

## 📌 Équation Résolue
f(x) = x³ − e⁻ˣ − 20 = 0
La racine est cherchée sur l'intervalle **[2, 3]** avec une précision **ε = 10⁻⁶**.

---

## 📊 Résultats

| Méthode | Point de départ | Racine approchée | Itérations |
|---|---|---|---|
| Dichotomie | [2, 3] | ≈ 2.7... | ~20 |
| Point Fixe | x₀ = 2 | ≈ 2.7... | ~10 |
| Newton-Raphson | x₀ = 2 | ≈ 2.7... | ~5 |

> Les valeurs exactes s'affichent à l'exécution du programme.

---

## 📸 Visualisations Générées

- 📉 Courbe de convergence — **Dichotomie**
- 📉 Courbe de convergence — **Point Fixe**
- 📉 Courbe de convergence — **Newton-Raphson**
- 📈 **Comparaison globale** des trois méthodes sur un même graphique

Toutes les courbes sont en **échelle logarithmique** sur l'axe des erreurs.

---

## 🗂️ Structure du Projet

    projet_numerique/
    └── methodes_numeriques.py    # Script principal contenant les 3 méthodes

---

## 🛠️ Technologies Utilisées

| Technologie | Rôle |
|---|---|
| 🐍 Python 3 | Langage principal |
| 📊 Matplotlib | Tracé des courbes de convergence |
| 🔢 Math | Fonctions mathématiques (exp, log) |

---

## ⚙️ Installation et Lancement

### Prérequis

```bash
pip install matplotlib
```

### Lancement

```bash
python methodes_numeriques.py
```

---

## 🎯 Objectif du Projet

Ce projet a été réalisé dans le cadre de notre cours universitaire.  
Il nous a permis de pratiquer et de renforcer nos compétences en :

- Implémentation des **méthodes itératives** de résolution numérique
- Compréhension et comparaison des **ordres de convergence**
- Choix d'une **fonction de point fixe** contractante et stable
- Utilisation de **Matplotlib** pour la visualisation scientifique
- Analyse du **comportement numérique** des algorithmes

---

## 🎨 Présentation du Projet

En plus du code source, nous avons réalisé une **présentation visuelle** afin d'expliquer plus clairement :

- Le contexte mathématique du projet
- Les trois méthodes numériques et leur principe
- La comparaison des vitesses de convergence
- Les graphiques et résultats obtenus

👉 [Voir la présentation](https://canva.link/qkk02b8qvvz43dg)

---

## 🎓 Informations Académiques

| | |
|---|---|
| **Université** | USTHB — Université des Sciences et de la Technologie Houari Boumediene |
| **Faculté** | Faculté d'Informatique |
| **Module** | Mathématiques & Informatique |
| **Groupe** | L2.ACAD.B |
| **Année** | 2025 / 2026 |
| **Enseignant(e)** | D. Dahmani |

---

## 📄 Licence

Ce projet est réalisé à des fins pédagogiques dans le cadre du module **Mathématiques & Informatique** à l'**USTHB**.

---

## 👥 Auteurs

- Mekhdani Douaa
- Zyat Maria
- Bouguerra Ayoub
