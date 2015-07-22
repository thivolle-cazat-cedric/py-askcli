# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

class Item(object):

    key = ''
    txt = ''
    activate = False

    def __init__(self, key, txt, activate=False):
        
        self.key = str(key)
        self.txt = str(txt)
        self.activate = bool(activate)

    def __repr__(self):
        return "<menu.Item : {0} - {1}>".format(self.key, self.txt)

    def __str__(self):
        ret = "{0} - {1}".format(self.key, self.txt)

        if (self.activate):
            return ">{0}".format(ret)
        else:
            return " {0}".format(ret)

    def __eq__(self, other):

        try:
            return (self.key == other.key)
        except Exception:
            return False


class Menu(object):
    '''
    permet de faire un menu à choix
    '''
    title = ''
    _choice = list()
    choose = -1
    _choose_index = -1
    case = False

    def __init__(self, choice, title='', case=False):
        '''
        :param Item[] choice: dictinaire d'menu.Item des choix possible. acceptable une liste de str
        :param str tilte: titre du menu
        :param bool case: menu sensible à la casse (miniscule/majuscule)

        permet d'initialiser les attribut de l'objet.

         * **choose** Liste des choix possible
         * **choice** Choix effectuer. par défaut -1. est automatiquement seter quand on appel la méthode launch()
         * **title**  Titre du menu *optionnel*
         
        '''
        self._choice = list()

        if isinstance(choice, list):
            loop = 1

            for i in choice:

                if type(i).__name__ == 'Item':
                    self._choice.append(i)
                elif isinstance(i, str):
                    self._choice.append(Item(loop, i))
                else:
                    ValueError('the index {0} in list is [{1}]. This type are not suported'.format(loop-1, type(i).__name__))

                loop += 1

        self.title = title
        self.case = case
        self.choose = -1

    def __repr__(self):
        return "<menu {0} choice>".format(len(self.choice))

    def __str__(self):
        if len(self.title) == 0:
            value = ''
        else:
            value = '> ' + self.title

        for item in self._choice:
            value += "\n   {0}".format(item)

        return value

    def launch(self, text='choix', err=' X - Saisie incorrecte, merci de selectionner une valeur dans le champ'):
        """
        :param str text: text à afficher avant la saisie. par Défaut **choix**. Ne pas insérer le ' : ' à la fin.
        :param str err: text à afficher en cas d'erreur de saisie. Par Défaut **X - Saisie incorrecte, merci de selectionner une valeur dans le champ**.

        permet de lancer le menu avec la saisie à la fin.
        Des tests sont fait sur la saisie, si la valeur est 
        """

        print(self.__str__())

        ask = True
        while ask:
            key = raw_input('? '+text+' : ')

            if self.key_is_ok(key):
                ask = False
                self.set_choice(key)
            else:
                ask = True

            if ask:
                print(err)

    def get_choosen_text(self):
        """
        :rtype: str
        :return: le texte choisi
        
        si ``self.choose`` est inferieur à **0** alors on retourn une chaine vide ''
        """

        if self.choose > -1:
            return self._choice[self._choose_index].txt
        else:
            return ''

    def key_is_ok(self, key):

        key = str(key)

        index = 0
        loop = True
        is_ok = False
        while loop:

            if index > (len(self._choice)-1):
                loop = False

            elif (self.case and self._choice[index].key == key) or \
               (not self.case and self._choice[index].key.lower() == key.lower()):
                is_ok = True
                loop = False
                self._choose_index = index

            else:
                is_ok = False
                index += 1



        return is_ok

    def set_choice(self, choose):
        
        choose = str(choose)
        if self.key_is_ok(choose):
            self.choose = choose
        else:
            raise ValueError("the key {0} are not in choice list".format(choose))


