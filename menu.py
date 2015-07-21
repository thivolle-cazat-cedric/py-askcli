# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

class menu(object):
	'''
	permet de faire un menu à choix
	'''
	title = ''
	_choice = {}
	choose = -1
	case = False

	def __init__(self, choice, title='', case=False):
		'''
		:param dict choice: dictionnaire des choix possible
		:param str tilte: titre du menu
		:param bool case: menu sensible à la casse (miniscule/majuscule)

		permet d'initialiser les attribut de l'objet.

		 * **choose** Liste des choix possible
		 * **choice** Choix effectuer. par défaut -1. est automatiquement seter quand on appel la méthode launch()
		 * **title**  Titre du menu *optionnel*

		exemple de choice : 
		 {
		 	'1' : menu A,
		 	'2' : menu B,
		 	'Q' : Exit
		 }
		'''

		if isinstance(choice, dict):
				self._choice = dict()
				for key in choice:
					if case:
						self._choice[str(key).lower()] = choice[key]
					else:
						self._choice[str(key)] = choice[key]


		if isinstance(choice, list):
			i = 1
			self._choice = dict()
			for txt in choice:
				print(txt)
				self._choice[i.__str__().lower()] = txt
				i += 1

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

		for key in self._choice:
			if self.case:
				value += "\n  {0} - {1}".format(key, self._choice[key])
			else:
				value += "\n  {0} - {1}".format(str(key).lower(), self._choice[key])


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

			if (self.case and key in self._choice) or \
			   (not self.case and str(key).lower() in self._choice):
				ask = False
				self.choose = key
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
			return self._choice[self.choose]
		else:
			return ''

