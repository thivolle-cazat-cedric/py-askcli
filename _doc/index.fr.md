# ![Image of Yaktocat](http://doc.thivolle-cazat.fr/public/askcli/logo-50.png)   Askcli
 
---

Un module python qui vous permet de générer des menus interactifs avec un utilisateur final dans un script python.

*Exemple simple d'utilisation :* 

```nohighlight
? Valider votre choix [Y/n] : 
```

 *ou encore : *

```nohighlight
  1 - action 1
  2 - action 2
  3 - action 2
  q - quitter
? choix : 
```

# Installation

**virtualenv**
```bash
pip install askcli
```
**cloning project**
```bash
source env_dir/bin/activate
cd your_lib_project
git clone https://github.com/thivolle-cazat-cedric/py-askcli.git
cd py-askcli
python setup.py install
``


### 2. Simulation d'installation dans l'environement *(pip)*

```bash
#!/bin/bash

$ cd <your_project_dir/res_dir>
$ git clone https://github.com/thivolle-cazat-cedric/py-askcli.git
$ source <your_virtualenv_path>/bin/activate
(envName)$ ln -s `pwd`/py-askcli/askcli $VIRTUAL_ENV/lib/python2.7/site-packages/
```

```python
from askcli import Menu

[...]
```

# Utilisation

Dans le module askcli vous y trouverais 2 objetcs :

## [Menu](./1.Menu)

Un objet qui vous permet de creer des menus à choix multiple avec controle de saisie. Avec ce module il est possible de créer des menu à choix alpha/numérique.

[Regadez sa documentaion et ces utilisations](./1.Menu)

## [AskBool](./2.AskBool)

[Regadez sa documentaion et ces utilisations](./2.AskBool)

