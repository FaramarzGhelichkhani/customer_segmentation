class PhoneFeaturesExtractor:
    def __init__(self, primary_phone):
        self.primary_phone = primary_phone
        
    def get_digit(self, postgres_index):
        """ Helper method to get the digit at the specified index with bounds checking. """
        if 1 <= postgres_index <= len(self.primary_phone):
            index =  postgres_index - 1 
            return self.primary_phone[index]
        return None

    def _7ragham(self):
        return 1 if (self.get_digit(5) == self.get_digit(6) == self.get_digit(7) != '0' and
                      self.get_digit(7) == self.get_digit(8) == self.get_digit(9) == self.get_digit(10) == self.get_digit(11)) else 0

    def _6raghamakhar(self):
        return 1 if (self.get_digit(5) != self.get_digit(6) and
                      self.get_digit(6) == self.get_digit(7) != '0' and
                      self.get_digit(7) == self.get_digit(8) == self.get_digit(9) == self.get_digit(10) == self.get_digit(11)) else 0

    def _6raghamaval(self):
        return 1 if (self.get_digit(5) == self.get_digit(6) == self.get_digit(7) != '0' and
                      self.get_digit(7) == self.get_digit(8) == self.get_digit(9) == self.get_digit(10) and
                      self.get_digit(10) != self.get_digit(11)) else 0

    def _5raghamvasat(self):
        return 1 if (self.get_digit(5) != self.get_digit(6) and
                      self.get_digit(10) != self.get_digit(11) and
                      self.get_digit(6) == self.get_digit(7) != '0' and
                      self.get_digit(7) == self.get_digit(8) == self.get_digit(9) and
                      self.get_digit(9) == self.get_digit(10)) else 0

    def _5raghamakhar(self):
        return 1 if (self.get_digit(6) != self.get_digit(7) and
                      self.get_digit(7) == self.get_digit(8) != '0' and
                      self.get_digit(8) == self.get_digit(9) == self.get_digit(10) == self.get_digit(11)) else 0

    def _4raghamakhar(self):
        return 1 if (self.get_digit(7) != self.get_digit(8) and
                      self.get_digit(8) == self.get_digit(9) != '0' and
                      self.get_digit(11) == self.get_digit(9) == self.get_digit(10)) else 0

    def _rond_millioni(self):
        sub_str = self.primary_phone[4:]  # Starting from character at index 5 (1-based index)
        count_of_zeros = sub_str.count('0')
        if (count_of_zeros == 4 and '0000' in sub_str) or \
            (count_of_zeros == 5 and '00000' in sub_str) or \
            (count_of_zeros == 6 and '000000' in sub_str):
            return 1
        else:
            return 0

    def _5raghamaval(self):
        return 1 if (
                      self.get_digit(5) == self.get_digit(6) != '0' and
                      self.get_digit(6) == self.get_digit(7) == self.get_digit(8) == self.get_digit(9)  and
                      self.get_digit(9) != self.get_digit(10) ) else 0

    def _4raghamaval(self):
        return 1 if (self.get_digit(5) == self.get_digit(6) != '0' and
                      self.get_digit(6) == self.get_digit(7) == self.get_digit(8) and
                      self.get_digit(8) != self.get_digit(9)) else 0

    def _3joftaaval(self):
        return 1 if (self.primary_phone[4:6] == self.primary_phone[6:8] == self.primary_phone[8:10] 
                    ) else 0

    def _3joftakhar(self):
        return 1 if (self.primary_phone[5:7] == self.primary_phone[7:9] and self.primary_phone[7:9] == self.primary_phone[9:11]
                      ) else 0

    def _joftjoftakhar(self):
        return 1 if (self.primary_phone[7:9] == self.primary_phone[9:11] ) else 0

    def _joftjoftaval(self):
        return 1 if (self.primary_phone[4:6] == self.primary_phone[6:8]) else 0

    def _3raghamaval(self):
        return 1 if (self.get_digit(5) == self.get_digit(6) and
                      self.get_digit(6) == self.get_digit(7) and self.get_digit(7) != self.get_digit(8) ) else 0

    def _3raghamakhar(self):
        return 1 if (
                      self.get_digit(8) != self.get_digit(9) and
                      self.get_digit(9) == self.get_digit(10) == self.get_digit(11)) else 0

    def _4raghamvasat(self):
        return 1 if ((self.get_digit(5) != self.get_digit(6) and
                      self.get_digit(9) != self.get_digit(10) and
                      self.get_digit(6) == self.get_digit(7) and
                      self.get_digit(7) == self.get_digit(8) == self.get_digit(9)) or
                    (self.get_digit(6)  != self.get_digit(7) and
                     self.get_digit(10) != self.get_digit(11) and
                     self.get_digit(7)  == self.get_digit(8) == self.get_digit(9)  == self.get_digit(10))
        ) else 0

    def _10000akhar(self):
        return 1 if ((self.get_digit(7) != '0' and
                      self.get_digit(11) != '0' and
                      self.get_digit(8) == '0' and
                      self.get_digit(9) == '0' and
                      self.get_digit(10) == '0') or
                      (self.get_digit(7) != '0' and
                      self.get_digit(8) == '0' and
                      self.get_digit(9) == '0' and
                      self.get_digit(10) == '0' and
                      self.get_digit(11) == '0')) else 0

    def _10000aval(self):
        return 1 if ((self.get_digit(6) != '0' and
                      self.get_digit(10) != '0' and
                      self.get_digit(7) == '0' and
                      self.get_digit(8) == '0' and
                      self.get_digit(9) == '0') or
                      (self.get_digit(5) != '0' and
                      self.get_digit(9) != '0' and
                      self.get_digit(6) == '0' and
                      self.get_digit(7) == '0' and
                      self.get_digit(8) == '0')) else 0

    def _sadsadi(self):
        return 1 if ((self.get_digit(6) != '0' and
                      self.get_digit(9) != '0' and
                      self.get_digit(7) == '0' and
                      self.get_digit(8) == '0' and
                      self.get_digit(10) == '0' and
                      self.get_digit(11) == '0') or
                      (self.get_digit(5) != '0' and
                      self.get_digit(8) != '0' and
                      self.get_digit(11) != '0' and
                      self.get_digit(6) == '0' and
                      self.get_digit(7) == '0' and
                      self.get_digit(9) == '0' and
                      self.get_digit(10) == '0')) else 0

    def _hezariakhar(self):
        return 1 if ((self.get_digit(8)   != '0' and
                      self.get_digit(11) != '0' and
                      self.get_digit(9)  == '0' and
                      self.get_digit(10) == '0') or

                      (self.get_digit(8)   != '0' and 
                       self.get_digit(9)   == '0' and 
                       self.get_digit(10)  == '0' and 
                       self.get_digit(11)   == '0') or

                       (self.get_digit(8)   != '0' and 
                        self.get_digit(9)   != '0' and
                        self.get_digit(10)  == '0' and
                        self.get_digit(11)   == '0')
                      ) else 0

    def _hezariaval(self):
        return 1 if ((self.get_digit(5) != '0' and
                      self.get_digit(6) == '0' and
                      self.get_digit(7) == '0') or

                      (self.get_digit(5) != '0' and 
                       self.get_digit(6) != '0' and 
                       self.get_digit(7) == '0' and 
                       self.get_digit(8) == '0') ) else 0

    def _dahdahiakhar(self):
        return 1 if (self.get_digit(8)   != '0' and
                      self.get_digit(9)  == '0' and
                      self.get_digit(10) != '0' and
                      self.get_digit(11) == '0') else 0

    def _dahdahiaval(self):
        return 1 if (self.get_digit(5) != '0' and
                      self.get_digit(6) == '0' and
                      self.get_digit(7) != '0' and
                      self.get_digit(8) == '0') else 0

    def __rond3pele(self):
        return 1 if ( (self.get_digit(5) == self.get_digit(7) and  self.get_digit(7) == self.get_digit(9) ) or
                     (self.get_digit(6) == self.get_digit(8)  == self.get_digit(10)) or
                      (self.get_digit(7) == self.get_digit(9) == self.get_digit(11) ) 
                      ) else 0
    
    def _rond3pele(self):
        return 0 if (self._7ragham()     == 1 or 
                     self._6raghamaval() == 1 or
                     self._5raghamvasat()== 1 or
                     self._5raghamakhar()== 1 or
                     self._4raghamakhar()== 1 or
                     self._5raghamaval() == 1 or
                     self._4raghamaval() == 1
                      ) else self.__rond3pele()
 
    def _pishshomare(self):
        prefixes = ['910', '911', '912', '913', '914', '915', '916', '917', 
                    '918', '919', '920', '921', '922', '923', '990', '991', 
                    '992', '993', '996', '905', '901', '904', '903', 
                    '902', '900', '930', '933', '935', '936', '937', '938', 
                    '939', '932', '999']
        # p = self.primary_phone[1:4]  
        p = self.primary_phone[4:11]  
        return 1 if any(prefix in p for prefix in prefixes) else 0

    def _tarazo(self):
        return 1 if (self.primary_phone[4:7] == self.primary_phone[8:11]) else 0

    def _tartibiakhar(self):
        return 1 if ((int(self.get_digit(11)) - int(self.get_digit(10)) == 1 and
                       int(self.get_digit(10)) - int(self.get_digit(9)) == 1) or
                      (int(self.get_digit(11)) - int(self.get_digit(10)) == -1 and
                       int(self.get_digit(10)) - int(self.get_digit(9)) == -1)) else 0

    def _tartibiaval(self):
        return 1 if ((int(self.get_digit(7)) - int(self.get_digit(6)) == 1 and
                       int(self.get_digit(6)) - int(self.get_digit(5)) == 1) or
                      (int(self.get_digit(7)) - int(self.get_digit(6)) == -1 and
                       int(self.get_digit(6)) - int(self.get_digit(5)) == -1)) else 0

    def _tavalod(self):
        return 1 if ((1300 < int(self.primary_phone[4:8]) < 1400) or
                      (1300 < int(self.primary_phone[7:11]) < 1400)) else 0

    def _reverseCondition(self):
        return 1 if (self.primary_phone[4:6][::-1] in self.primary_phone[6:11] or
                      self.primary_phone[5:7][::-1] in self.primary_phone[7:11]  or
                      self.primary_phone[6:8][::-1] in self.primary_phone[8:11]  or
                      self.primary_phone[6:8][::-1] in self.primary_phone[4:6] or
                      self.primary_phone[7:9][::-1] in self.primary_phone[9:11] or
                      self.primary_phone[7:9][::-1] in self.primary_phone[4:7]) else 0

    def _3raghamvasat(self):
        return  1 if ((self.get_digit(6) != self.get_digit(7)   and
                       self.get_digit(9) != self.get_digit(10)  and 
                       self.get_digit(7) == self.get_digit(8) == self.get_digit(9) ) or

                        (self.get_digit(5) != self.get_digit(6) and
                         self.get_digit(8) != self.get_digit(9) and 
                         self.get_digit(6) == self.get_digit(7) and
                         self.get_digit(7) == self.get_digit(8))) else 0
    
    def _tekrar2raghamyeki(self):
        return  1 if (self.get_digit(5) == self.get_digit(6)   and
                       
                       (self.get_digit(7) == self.get_digit(8)  or 
                        self.get_digit(8) == self.get_digit(9)  or
                        self.get_digit(9) == self.get_digit(10) or
                        self.get_digit(10)== self.get_digit(11) ) or

                       (self.get_digit(7) == self.get_digit(8)  and
                        (self.get_digit(9) == self.get_digit(10) or self.get_digit(10) == self.get_digit(11) )
                        ) or

                        (self.get_digit(8) == self.get_digit(9) and 
                         self.get_digit(10) == self.get_digit(11))) else 0
   
    def _peleaval(self):
        return 1 if ((self.get_digit(5) == self.get_digit(7) and
                      self.get_digit(6) != self.get_digit(8)) or
                     (self.get_digit(6) == self.get_digit(8) and
                      self.get_digit(7) != self.get_digit(9))) else 0

    def _peleakhar(self):
        return 1 if ((self.get_digit(8) == self.get_digit(10) and
                      self.get_digit(9) != self.get_digit(11)) or

                     (self.get_digit(9) == self.get_digit(11) and
                      self.get_digit(8) != self.get_digit(9))) else 0

    def _fourth(self):
        return int(self.get_digit(5))
    
    def _first_three(self):
        return int(self.primary_phone[1:4])

    def _rond_number(self):
        s = self._7ragham()  + self._6raghamaval() + self._6raghamakhar() + self._5raghamvasat() + self._5raghamakhar() + self._4raghamakhar() + \
        self._rond_millioni() + self._5raghamaval() + self._4raghamaval() + self._3joftaaval() + self._3joftakhar() + self._joftjoftakhar() +\
        self._joftjoftaval() + self._3raghamaval() + self._3raghamakhar() + self._4raghamvasat() + self._10000akhar() + self._10000aval() + \
        self._sadsadi() + self._hezariakhar() + self._hezariaval() + self._dahdahiakhar() + self._dahdahiaval() + self._pishshomare() +\
        self._tarazo() + self._tartibiakhar() + self._tartibiaval() + self._tavalod() + self._reverseCondition() + self._3raghamvasat() +\
        self._tekrar2raghamyeki() + self._peleaval() + self._peleakhar() + self.__rond3pele()
        return s
    
    def _mam(self):
        return 1  if self._round_number() == 0 else 0

    @classmethod
    def get_feature(cls, phonenumber):
        instance  = cls(phonenumber)
        out ={}
        out['7ragham'] = instance._7ragham() 
        out['6raghamaval'] = instance._6raghamaval() 
        out['6raghamakhar'] = instance._6raghamakhar() 
        out['5raghamvasat'] = instance._5raghamvasat() 
        out['5ragham akhar'] = instance._5raghamakhar() 
        out['4ragham akhar'] = instance._4raghamakhar() 
        out['rond millioni'] = instance._rond_millioni()
        out['5raghamaval'] = instance._5raghamaval()
        out['4raghamaval'] = instance._4raghamaval()
        out['3joftaaval'] = instance._3joftaaval()
        out['3joftakhar'] = instance._3joftakhar()
        out['joftjoftakhar'] = instance._joftjoftakhar()
        out['joftjoftaval'] = instance._joftjoftaval()
        out['3raghamaval'] = instance._3raghamaval()
        out['3raghamakhar'] = instance._3raghamakhar()
        out['4raghamvasat'] = instance._4raghamvasat()
        out['10000akhar'] = instance._10000akhar()
        out['10000aval'] = instance._10000aval()
        out['sadsadi'] = instance._sadsadi()
        out['hezariakhar'] = instance._hezariakhar()
        out['hezariaval'] = instance._hezariaval()
        out['dahdahiakhar'] = instance._dahdahiakhar()
        out['dahdahiaval'] = instance._dahdahiaval()
        out['pishshomare'] = instance._pishshomare()
        out['tarazo'] = instance._tarazo()
        out['tartibiakhar'] = instance._tartibiakhar()
        out['tartibiaval'] = instance._tartibiaval()
        out['tavalod'] = instance._tavalod()
        out['reverseCondition'] = instance._reverseCondition()
        out['3raghamvasat'] = instance._3raghamvasat()
        out['peleaval'] = instance._peleaval()
        out['peleakhar'] = instance._peleakhar()
        out['rond3pele'] = instance._rond3pele()
        out['rond_number'] = instance._rond_number()
        out['fourth'] = instance._fourth()
        out['first_three'] = instance._first_three()
        out['tekrar2raghamyeki'] = instance._tekrar2raghamyeki()
        return out 
