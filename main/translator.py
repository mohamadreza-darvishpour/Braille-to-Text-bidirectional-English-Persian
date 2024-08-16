
lang_braille_base_dict ={
        'persian' : {
    '\n': '\n',
    '⠀': ' ',
    '⠜': 'آ',
    '⠁': 'ا',
    '⠃': 'ب',
    '⠏': 'پ',  
    '⠞': 'ت',
    '⠹': 'ث',
    '⠚': 'ج',
    '⠉': 'چ',
    '⠱': 'ح',
    '⠭': 'خ',
    '⠙': 'د',
    '⠮': 'ذ',
    '⠗': 'ر',
    '⠵': 'ز',
    '⠬': 'ژ',
    '⠎': 'س',
    '⠩': 'ش',
    '⠯': 'ص',
    '⠫': 'ض',
    '⠾': 'ط',
    '⠿': 'ظ',
    '⠷': 'ع',
    '⠣': 'غ',
    '⠋': 'ف',
    '⠟': 'ق',
    '⠅': 'ک',
    '⠛': 'گ',
    '⠇': 'ل',
    '⠍': 'م',
    '⠝': 'ن',
    '⠺': 'و',
    '⠓': 'ه',
    '⠊': 'ی',

                    },

'english' : {    
            '⠀': ' ',            
            '⠁': 'A',
            '⠃': 'B',    
            '⠉': 'C',    
            '⠙': 'D',    
            '⠑': 'E',  
            '⠋': 'F',  
            '⠛': 'G',  
            '⠓': 'H',  
            '⠊': 'I',  
            '⠚': 'J',  
            '⠅': 'K',  
            '⠇': 'L',  
            '⠍': 'M',  
            '⠝': 'N',  
            '⠕': 'O',  
            '⠏': 'P',  
            '⠟': 'Q',  
            '⠗': 'R',  
            '⠎': 'S',  
            '⠞': 'T',  
            '⠥': 'U',  
            '⠧': 'V',  
            '⠺': 'W',  
            '⠭': 'X',  
            '⠽': 'Y',  
            '⠵': 'Z',  
            '⠁': 'a',
            '⠃': 'b',                
            '⠉': 'c',                
            '⠙': 'd',         
            '⠑': 'e',            
            '⠋': 'f',              
            '⠛': 'g',              
            '⠓': 'h',              
            '⠊': 'i',              
            '⠚': 'j',         
            '⠅': 'k',              
            '⠇': 'l',              
            '⠍': 'm',              
            '⠝': 'n',              
            '⠕': 'o',              
            '⠏': 'p',           
            '⠟': 'q',              
            '⠗': 'r',              
            '⠎': 's',              
            '⠞': 't',              
            '⠥': 'u',              
            '⠧': 'v',             
            '⠺': 'w',              
            '⠭': 'x',              
            '⠽': 'y',              
            '⠵': 'z',
           }
    }
num_sign = {
    'english_numbers' : 
    {
        
    '⠁': '1',
    '⠃': '2',    
    '⠉': '3',    
    '⠙': '4',    
    '⠑': '5',  
    '⠋': '6',  
    '⠛': '7',  
    '⠓': '8',  
    '⠊': '9',  
    '⠚': '0',  
    },
    'persian_numbers' : {
    '⠁': '۱',
    '⠃': '۲',    
    '⠉': '۳',    
    '⠙': '۴',    
    '⠑': '۵',  
    '⠋': '۶',  
    '⠛': '۷',  
    '⠓': '۸',  
    '⠊': '۹',  
    '⠚': '۰',  

    },
    'sign' : {

        '⠼' : 'digit',
        '⠰' : 'operation',

    },
    'math_sign' : {
        '⠲' : '÷',
        '⠖' : '+',
        '⠦' : '×',
        '⠶' : '=',
        '⠤' : '-',

    }


}

    


def find_value_by_key(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return f'<{key}>'


def find_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return f'<{value}>'


class translator():
    langs = lang_braille_base_dict.copy()
    alphabet_string_exam = "\nspace  =  {},\n⠁  =  {},\n⠂  =  {},\n⠃  =  {},\n⠄  =  {},\n⠅  =  {},\n⠆  =  {},\n⠇  =  {},\n⠈  =  {},\n⠉  =  {},\n⠊  =  {},\n⠋  =  {},\n⠌  =  {},\n⠍  =  {},\n⠎  =  {},\n⠏  =  {},\n⠐  =  {},\n⠑  =  {},\n⠒  =  {},\n⠓  =  {},\n⠔  =  {},\n⠕  =  {},\n⠖  =  {},\n⠗  =  {},\n⠘  =  {},\n⠙  =  {},\n⠚  =  {},\n⠛  =  {},\n⠜  =  {},\n⠝  =  {},\n⠞  =  {},\n⠟  =  {},\n⠠  =  {},\n⠡  =  {},\n⠢  =  {},\n⠣  =  {},\n⠤  =  {},\n⠥  =  {},\n⠦  =  {},\n⠧  =  {},\n⠨  =  {},\n⠩  =  {},\n⠪  =  {},\n⠫  =  {},\n⠬  =  {},\n⠭  =  {},\n⠮  =  {},\n⠯  =  {},\n⠰  =  {},\n⠱  =  {},\n⠲  =  {},\n⠳  =  {},\n⠴  =  {},\n⠵  =  {},\n⠶  =  {},\n⠷  =  {},\n⠸  =  {},\n⠹  =  {},\n⠺  =  {},\n⠻  =  {},\n⠼  =  {},\n⠽  =  {},\n⠾  =  {},\n⠿  =  {},\n⡀  =  {},\n⡁  =  {},\n⡂  =  {},\n⡃  =  {},\n⡄  =  {},\n⡅  =  {},\n⡆  =  {},\n⡇  =  {},\n⡈  =  {},\n⡉  =  {},\n⡊  =  {},\n⡋  =  {},\n⡌  =  {},\n⡍  =  {},\n⡎  =  {},\n⡏  =  {},\n⡐  =  {},\n⡑  =  {},\n⡒  =  {},\n⡓  =  {},\n⡕  =  {},\n⡔  =  {},\n⡗  =  {},\n⡖  =  {},\n⡘  =  {}"
    num_sign = num_sign.copy()
 
    def braille_to_lang(self , lang='english', text = '' ):
        is_sign = False
        is_digit = False
        try:
            dict = self.langs[lang]
        except:
            dict = self.langs['english']
            string = 'could not find language chars...' 
            return string
        string  = ''
        for any in text:
            print(f'\n  ________  \n')

            if(any =='⠼'):
                print(f'\n\n  ____   9   ____  \n\n')
                is_digit = True
                is_sign = False
                
            elif(any == '⠰'):
                print(f'\n\n  ____   8   ____  \n\n')
                is_sign = True 
                is_digit = False 

            elif(any == '⠀' or any==' '):
                print(f'\n\n  ____   7   ____  \n\n')
                is_sign = False 
                is_digit = False
            else:
                print(f'\n\n  ____   6   ____  \n\n')
                pass

            if(any =='⠰' or any == '⠼'):
                print(f'\n\n  ____   55   ____  \n\n')
                pass

            elif(any==  '⠀' or any==' '):
                print(f'\n\n  ____   4   ____  \n\n')
                is_sign = False 
                is_digit = False
                string += ' '
                    
            elif (is_digit==True and is_sign==False):
                print(f'\n\n  ____   3   ____  \n\n')
                if(lang=='persian'):
                    temp = find_value_by_key(self.num_sign['persian_numbers'], any)
                else:
                    temp = find_value_by_key(self.num_sign['english_numbers'], any)
                string += temp 
        
            elif(is_digit==False and is_sign==True):
                print(f'\n\n  ____   2   ____  \n\n')
                temp = find_value_by_key(self.num_sign['math_sign'], any)
                string += temp
                is_sign = False

            else :
                print(f'\n\n  ____   1   ____  \n\n')
                temp = find_value_by_key(dict , any )
                string += temp 
                is_sign = False 
                is_digit = False  
            

        return string

    def lang_to_braille(self , lang='english' , text='' ):
        is_num_writing = False  
        try:
            dict = self.langs[lang]
        except:
            string = 'could not find language chars...' 
            return string
        string  = '' 
        for any in text:
            temp = None
            if(any in  '1234567890۱۲۳۴۵۶۷۸۹۰' and is_num_writing ==False ):
                is_num_writing = True 
                if(lang == 'persian'):
                    temp = find_key_by_value(self.num_sign['persian_numbers'], any)
                else:
                    temp = find_key_by_value(self.num_sign['english_numbers'], any)
                temp = f'⠼{temp}'

            elif(any in  '1234567890۱۲۳۴۵۶۷۸۹۰' and is_num_writing ==True ):
                is_operation_writing = False 
                if(lang == 'persian'):
                    temp = find_key_by_value(self.num_sign['persian_numbers'], any)
                else:
                    temp = find_key_by_value(self.num_sign['english_numbers'], any)
            elif (any ==' ' or any == '⠀'):
                temp = '⠀'
                is_num_writing = False 
            
            elif(any in '+=×-÷'):
                temp = find_key_by_value(self.num_sign['math_sign'], any)
                temp = f'⠰{temp}'
                is_num_writing = False 
            else:
                temp = find_key_by_value(dict , any)
                is_num_writing = False
            string += temp 
        return string

    def add_lang(self ,  lang_name:str , the_str):
        try:
            if(the_str=='' and lang_name in list(self.langs.keys())):
                self.langs.pop(lang_name)
                return f'{lang_name} deleted successfully.' 
            elif(the_str=='' ):
                return f'{lang_name} could not be added by empty input.' 

            the_str = the_str.replace('\n' , '') 
            the_str = the_str.replace('  ' , '') 
            the_str = the_str.replace('}' , '') 
            the_str = the_str.replace('{' , '') 
            the_str = the_str.split(',') 
            temp_dict = {}
            for item in the_str:
                temp = item.split('=')
                if(len(temp)>1 and temp[0]!= '' ):
                    temp_dict[temp[0]] = temp[1]
            temp_dict['⠀'] = temp_dict.pop('space' , ' ')
            self.langs[lang_name] = temp_dict
            return f'{lang_name} added successfully.' 
        except:
            return f'not success to add new language. try again.'

term = '''

space  =  {t},
⠁  =  {k},
⠂  =  {m},
⠃  =  {k},
⠄  =  {l},
⠅  =  {},
⠆  =  {},
⠇  =  {},
⠈  =  {},
⠉  =  {},
⠊  =  {},
⠋  =  {},
⠌  =  {},
⠍  =  {},
⠎  =  {},
⠏  =  {},
⠐  =  {},
⠑  =  {},
⠒  =  {},
⠓  =  {},
⠔  =  {},
⠕  =  {},
⠖  =  {},
⠗  =  {},
⠘  =  {},
⠙  =  {},
⠚  =  {},
⠛  =  {},
⠜  =  {},
⠝  =  {},
⠞  =  {},
⠟  =  {},
⠠  =  {},
⠡  =  {},
⠢  =  {},
⠣  =  {},
⠤  =  {},
⠥  =  {},
⠦  =  {},
⠧  =  {},
⠨  =  {},
⠩  =  {},
⠪  =  {},
⠫  =  {},
⠬  =  {},
⠭  =  {},
⠮  =  {},
⠯  =  {},
⠰  =  {},
⠱  =  {},
⠲  =  {},
⠳  =  {},
⠴  =  {},
⠵  =  {},
⠶  =  {},
⠷  =  {},
⠸  =  {},
⠹  =  {},
⠺  =  {},
⠻  =  {},
⠼  =  {},
⠽  =  {},
⠾  =  {},
⠿  =  {},
⡀  =  {},
⡁  =  {},
⡂  =  {},
⡃  =  {},
⡄  =  {},
⡅  =  {},
⡆  =  {},
⡇  =  {},
⡈  =  {},
⡉  =  {},
⡊  =  {},
⡋  =  {},
⡌  =  {},
⡍  =  {},
⡎  =  {},
⡏  =  {},
⡐  =  {},
⡑  =  {},
⡒  =  {},
⡓  =  {},
⡕  =  {},
⡔  =  {},
⡗  =  {u},
⡖  =  {y},
⡘  =  {z}
'''


# d = translator() 
# d.braille_to_lang('persian' , '⠗⠁⠓⠏⠽⠗⠺⠵')
# d.lang_to_braille('persian' , 'سر و صدا ')
# d.add_lang('spanish' , term)