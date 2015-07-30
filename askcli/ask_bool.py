# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

class AskBool(object):

    desc = ''
    t_text = ''
    f_text = ''
    t_key = ''
    f_key = ''
    required = True
    default = False
    choosen = None

    def __init__(self, desc, t_text='Yes', f_text='No', t_key=None, f_key=None, required=True, default=False):
        """
        :param str desc: ce que écris le champs
        :param str t_text: text qui corespond à vrai 
        :param str f_text: text qui corespond à faux 
        :param str t_key: caractères de saisie qui sera valide (en plus du t_text) par défaut permier lettre de t_text
        :param str f_key: caractères de saisie qui sera valide (en plus du f_text) par défaut  permier lettre de f_text
        :param bool required: si faux alors il doit y avoir une valeur par défaut
        :param bool default: valeur par défaut
        """
        self.desc = str(desc)
        self.t_text = str(t_text)
        self.f_text = str(f_text)
        if t_key is None :
            self.t_key = str(self.t_text[0])
        else:
            self.t_key = str(t_key)

        if f_key is None:
            self.f_key = str(self.f_text[0])
        else:
            self.f_key = str(f_key)
        
        self.required = bool(required)
        self.default = bool(default)
        self.choosen = None

    def __repr__(self):
        """
        :rtype: str
        :return: representation de l'objet
        """
        return "<askcli.AskBool : {0}  [{1}/{2}]>".format(self.desc, self.t_key, self.f_key)

    def __str__(self):
        """
        :rtype: str
        :return: représentaion to string de l'objet
        """

        ret = "{0}  [{1}/{2}]>".format(self.desc, self.t_key, self.f_key)

    def _get_valid_array(self):
        """
        :return: une list avec touts les champs da validation possible
        :rtype: list 
        """
        return [self.t_text.lower(), self.t_key.lower()]


    def _get_invalid_array(self):
        """
        :return: une list avec touts les champs da validation possible
        :rtype: list 
        """
        return [self.f_text.lower(), self.f_key.lower()]


    def key_is_valid(self, key):
        """
        :param str key: clef à tester

        :rtype:bool
        :return: si la clef est valable ou non
        """

        try:
            key = str(key).lower()
        except Exception as e:
            return False
        
        valid = self._get_valid_array() + self._get_invalid_array()

        return (key in valid)

    def set_choice(self, key):
        """
        :param str key: clef que l'on souhaite affecter

        :Exception valueError: si la key n'est pas valide
        """

        key = str(key).lower()
        if self.key_is_valid(key):
            if key in self._get_valid_array():
                self.choosen =  True
            else:
                self.choosen =  False

        else:
            raise ValueError("askcli.AskBool : error key [{0}]. Is not valide ".format(key))

    def get_resp(self):
        """
        :return: si l'utilisateur à choisi le choix vraix ou False
        :rtype: bool

        :Exception: si choosen est a None
        """
        
        if self.choosen is None:
            raise Exception

        if isinstance(self.choosen, bool):
            return self.choosen

    def get_text(self):
        """
        :return: Le texte en fonction du choi
        :rtype: str
        """
        
        try:
            if self.get_resp():
                return self.t_text
            else:
                return self.f_text
        except Exception as e:
            return ''

    def launch(self, show_text_key=False, err_mess="error key"):
        '''
        :rtype: bool
        :return: vrai si il è choisi le t_key

        Permet de lancer la demande de saisie à l'utilisateur
        '''

        if show_text_key:
            print("   [{0}] {1} ".format(self.t_key, self.t_text))
            print("   [{0}] {1} ".format(self.f_key, self.f_text))
        
        if not self.required and show_text_key:
            def_explain = "   Default : [{0}]"
            if self.default:
                print(def_explain.format(self.t_key))
            else:
                print(def_explain.format(self.f_key))

        askprint = " ? {0} [{1}/{2}] : "

        if not self.required:
            if self.default:
                t_key = self.t_key.upper()
                f_key = self.f_key.lower()

            else:
                f_key = self.f_key.upper()
                t_key = self.t_key.lower()
        else:
            f_key = self.f_key.lower()
            t_key = self.t_key.lower()


        ask = True
        while ask:
            key = raw_input(askprint.format(self.desc, t_key, f_key))

            if self.required:
                if self.key_is_valid(key):
                    self.set_choice(key)
                    ask = False
                else:
                    ask = True

            else:
                if not key:
                    ask = False
                    mess_back = " > set default Value : {0}"
                    if self.default:
                        def_value = self.t_key
                    else:
                        def_value = self.f_key

                    self.set_choice(def_value)
                    print(mess_back.format(def_value))
                else:
                    if self.key_is_valid(key):
                        self.set_choice(key)
                        ask = False
                    else:
                        ask = True

            if ask:
                print(' x {0}'.format(err_mess))

        return self.get_resp()
