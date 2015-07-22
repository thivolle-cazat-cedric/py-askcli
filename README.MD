# py-askcli 0.2.0-b

Un petit module qui peut vous servir si vous editer un script et qu'il y a des menu du type : 

 1. action 1
 2. action 2
 3. [...]

===

## Exemple simple liste numérique

```python
from askcli.menu import Menu
# Création du menu
m = Menu(['action 1','action 2', 'action 3'])

# Affichage et demande de saisie de l'utilisateur
m.launch()

print('_______')
print("vous avez selectione le menu {0} : {1}".format(m.choose, m.get_choosen_text()))
```

**resultat**

```
  1 - action 1
  2 - action 2
  3 - action 2
? choix : a
 X - Saisie incorrecte, merci de selectiner une valeur dans le champ
? choix : 3
_______
vous avez selectione le menu 3 : action 3
```

## Exemple liste alpha/numérique

```python
from askcli.menu import Menu, Item
items = list()

# creation des items (choix)
choix_action_a = Item('a', 'Action A')
choix_action_b = Item('b', 'Action B')
choix_exit = Item('q', 'Quitter')
items = [choix_action_a, choix_action_b, choix_exit]

# Création du menu
m = Menu(items)

# Affichage et demande de saisie de l'utilisateur
m.launch()

print('_______')
print("vous avez selectione le menu {0} : {1}".format(m.choose, m.get_choosen_text()))
```

**resultat**

```   
    a - Action A
    b - Action B
    q - Quitter
? choix : 1
 X - Saisie incorrecte, merci de selectionner une valeur dans le champ
? choix : q
_______
vous avez selectione le menu q : Quitter

```

===

## TODO liste
- [X] Ordonner la liste 
- [ ] Module de Yes/no
- [ ] Test
- [ ] DOC