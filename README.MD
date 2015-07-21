# py-askcli

Un petit module qui peut vous servir si vous editer un script et qu'il y a des menu à list

```
from menu import menu
m = menu(['choix a','choix b', 'quiter'])
m.launch()
print("vous avez selectione le menu {0}".format(m.choose))
```
> 1 - choix a
>
> 2 - choix b
>
> 3 - quiter
>
>  ? choix : 4
>
>   X - Saisie incorrecte, merci de selectiner une valeur dans le champ
>
>  ? choix : 2
>
> vous avez selectione le menu 2


