# 🎄 Advent of Code – Jour 4 : Printing Department 🎁

## 🎯 Objectif

Optimiser le travail des chariots élévateurs pour qu’ils libèrent du temps et percent le mur menant à la cafétéria. Les rouleaux de papier (@) sont disposés sur une grille : il faut déterminer lesquels sont accessibles, puis combien peuvent être retirés au total.

---

## ⭐ Partie 1 — Rouleaux accessibles

Un rouleau est accessible s’il a **strictement moins de 4 voisins @** parmi les 8 cases autour.
Compter tous les rouleaux accessibles dans la grille complète.

### Exemple

Dans la grille fournie en exemple, **13 rouleaux** sont accessibles (marqués x).

### 🎉 Résultat obtenu

**1367**

---

## ⭐ Partie 2 — Retrait progressif des rouleaux

Dès qu’un rouleau est accessible, il peut être retiré.
Le retrait peut rendre d’autres rouleaux accessibles, créant un effet en cascade.
Objectif : répéter ce processus jusqu’à ce qu’aucun rouleau supplémentaire ne soit accessible.

### Exemple

Dans l’exemple du puzzle, le processus permet d’en retirer **43**.

### 🎉 Résultat obtenu

*(*

---

## 🎁 Statut

Les deux parties sont complètes.
Récompense : 2 étoiles ⭐⭐

Joyeux code de Noël 🎅✨
