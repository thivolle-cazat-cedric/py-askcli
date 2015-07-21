# py-askcli 0.0.1

Un petit module qui peut vous servir si vous editer un script et qu'il y a des menu à list

===

## exemple

```python
from menu import menu
m = menu({
	'1' : 'action 1',
	'2' : 'action 2',
	'3' : 'action 2',
	'q' : 'quitter'
})
m.launch()
print('_______')
print("vous avez selectione le menu {0} : {1}".format(m.choose, m.get_choosen_text()))
```
**resultat**

```
  1 - action 1
  q - quitter
  3 - action 2
  2 - action 2
? choix : a
 X - Saisie incorrecte, merci de selectiner une valeur dans le champ
? choix : q
_______
vous avez selectionner le menu q : quitter
```
===

## TODO liste
- [ ] Ordonner la liste 
- [ ] Module de Yes/no
- [ ] Test
- [ ] DOC