# py-askcli 0.2.0

Un petit module qui peut vous servir si vous editer un script et qu'il y a des menu à list

===

## exemple

```python
from askcli.menu import Menu
m = Menu(['action 1','action 2', 'action 3'])
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
===

## TODO liste
- [X] Ordonner la liste 
- [ ] Module de Yes/no
- [ ] Test
- [ ] DOC