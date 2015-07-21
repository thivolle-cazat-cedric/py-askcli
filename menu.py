# -*- coding: utf-8 -*-

class menu(object):
	'''
	permet de faire un menu à choix
	'''
	title = ''
	choice = []
	choose = -1

	def __init__(self, choice, title=''):
		'''
		:param list choice: liste des choix possible
		:param str tilte: titre du menu

		permet d'initialiser les attribut de l'objet.

		 * **choose** Liste des choix possible
		 * **choice** Choix effectuer. par défaut -1. est automatiquement seter quand on appel la méthode launch()
		 * **title**  Titre du menu *optionnel*
		'''

		self.choice = choice
		self.title = title
		self.choose = -1

	def __repr__(self):
		return "<menu {0} choice>".format(len(self.choice))

	def __str__(self):
		i = 1
		if len(self.title) == 0:
			value = ''
		else:
			value = self.title

		for txt in self.choice:
			value += "\n  {0} - {1}".format(i, txt)
			i += 1
		return value

	def launch(self, text='choix', err=' X - Saisie incorrecte, merci de selectiner une valeur dans le champ'):
		"""
		:param str text: text à afficher avant la saisie. par Défaut **choix**. Ne pas insérer le ' : ' à la fin.
		:param str err: text à afficher en cas d'erreur de saisie. Par Défaut **X - Saisie incorrecte, merci de selectiner une valeur dans le champ**.

		permet de lancer le menu avec la saisie à la fin.
		Des tests sont fait sur la saisie, si la valeur est 
		"""
		print(self.__str__())

		ask = True
		while ask:
			key = raw_input(text+' : ')
			try:
				key = int(key)
				if key in range(1, len(self.choice)):
					ask = False
					self.choose = key
				else:
					ask = True

			except Exception:
				ask = True
			if ask:
				print(err)

		return self.choose

