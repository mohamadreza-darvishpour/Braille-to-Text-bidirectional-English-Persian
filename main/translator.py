
lang_braille_base_dict ={
        'persian' : {
    '\u2800': ' ',
    '\u2840': 'آ',
    '\u2801': 'ا',
    '\u2803': 'ب',
    '\u2809': 'پ',
    '\u2819': 'ت',
    '\u2811': 'ث',
    '\u280B': 'ج',
    '\u281B': 'چ',
    '\u2813': 'ح',
    '\u280A': 'خ',
    '\u281A': 'د',
    '\u2805': 'ذ',
    '\u2807': 'ر',
    '\u280D': 'ز',
    '\u281D': 'ژ',
    '\u2815': 'س',
    '\u280F': 'ش',
    '\u281F': 'ص',
    '\u2817': 'ض',
    '\u280E': 'ط',
    '\u281E': 'ظ',
    '\u2825': 'ع',
    '\u2827': 'غ',
    '\u283A': 'ف',
    '\u282D': 'ق',
    '\u283D': 'ک',
    '\u2835': 'گ',
    '\u2802': '۱',
    '\u2806': '۲',
    '\u2812': '۳',
    '\u2832': '۴',
    '\u2822': '۵',
    '\u2814': '۶',
    '\u2816': '۷',
    '\u2836': '۸',
    '\u2826': '۹',
    '\u2810': '۰',    
    '\u2802': '1',
    '\u2806': '2',
    '\u2812': '3',
    '\u2832': '4',
    '\u2822': '5',
    '\u2814': '6',
    '\u2816': '7',
    '\u2836': '8',
    '\u2826': '9',
    '\u2810': '0',
    '': ''
            },

        'english' : {
    '\u2800': ' ',
    '\u2801': 'A',
    '\u2803': 'B',
    '\u2809': 'C',
    '\u2819': 'D',
    '\u2811': 'E',
    '\u280B': 'F',
    '\u281B': 'G',
    '\u2813': 'H',
    '\u280A': 'I',
    '\u281A': 'J',
    '\u2805': 'K',
    '\u2807': 'L',
    '\u280D': 'M',
    '\u281D': 'N',
    '\u2815': 'O',
    '\u280F': 'P',
    '\u281F': 'Q',
    '\u2817': 'R',
    '\u280E': 'S',
    '\u281E': 'T',
    '\u2825': 'U',
    '\u2827': 'V',
    '\u283A': 'W',
    '\u282D': 'X',
    '\u283D': 'Y',
    '\u2835': 'Z',
    '\u2802': '1',
    '\u2806': '2',
    '\u2812': '3',
    '\u2832': '4',
    '\u2822': '5',
    '\u2814': '6',
    '\u2816': '7',
    '\u2836': '8',
    '\u2826': '9',
    '\u2810': '0',
    '\u2841': 'a',
    '\u2843': 'b',
    '\u2849': 'c',
    '\u2859': 'd',
    '\u2851': 'e',
    '\u284B': 'f',
    '\u285B': 'g',
    '\u2853': 'h',
    '\u284A': 'i',
    '\u285A': 'j',
    '\u2845': 'k',
    '\u2847': 'l',
    '\u284D': 'm',
    '\u285D': 'n',
    '\u2855': 'o',
    '\u284F': 'p',
    '\u285F': 'q',
    '\u2857': 'r',
    '\u284E': 's',
    '\u285E': 't',
    '\u2865': 'u',
    '\u2867': 'v',
    '\u287A': 'w',
    '\u286D': 'x',
    '\u287D': 'y',
    '\u2875': 'z'
            }
    }


def find_value_by_key(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return '{?}'


def find_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return '{?}'


class translator():
    langs = lang_braille_base_dict.copy()
    alphabet_string_exam = "\nspace  =  {},\n⠁  =  {},\n⠂  =  {},\n⠃  =  {},\n⠄  =  {},\n⠅  =  {},\n⠆  =  {},\n⠇  =  {},\n⠈  =  {},\n⠉  =  {},\n⠊  =  {},\n⠋  =  {},\n⠌  =  {},\n⠍  =  {},\n⠎  =  {},\n⠏  =  {},\n⠐  =  {},\n⠑  =  {},\n⠒  =  {},\n⠓  =  {},\n⠔  =  {},\n⠕  =  {},\n⠖  =  {},\n⠗  =  {},\n⠘  =  {},\n⠙  =  {},\n⠚  =  {},\n⠛  =  {},\n⠜  =  {},\n⠝  =  {},\n⠞  =  {},\n⠟  =  {},\n⠠  =  {},\n⠡  =  {},\n⠢  =  {},\n⠣  =  {},\n⠤  =  {},\n⠥  =  {},\n⠦  =  {},\n⠧  =  {},\n⠨  =  {},\n⠩  =  {},\n⠪  =  {},\n⠫  =  {},\n⠬  =  {},\n⠭  =  {},\n⠮  =  {},\n⠯  =  {},\n⠰  =  {},\n⠱  =  {},\n⠲  =  {},\n⠳  =  {},\n⠴  =  {},\n⠵  =  {},\n⠶  =  {},\n⠷  =  {},\n⠸  =  {},\n⠹  =  {},\n⠺  =  {},\n⠻  =  {},\n⠼  =  {},\n⠽  =  {},\n⠾  =  {},\n⠿  =  {},\n⡀  =  {},\n⡁  =  {},\n⡂  =  {},\n⡃  =  {},\n⡄  =  {},\n⡅  =  {},\n⡆  =  {},\n⡇  =  {},\n⡈  =  {},\n⡉  =  {},\n⡊  =  {},\n⡋  =  {},\n⡌  =  {},\n⡍  =  {},\n⡎  =  {},\n⡏  =  {},\n⡐  =  {},\n⡑  =  {},\n⡒  =  {},\n⡓  =  {},\n⡕  =  {},\n⡔  =  {},\n⡗  =  {},\n⡖  =  {},\n⡘  =  {}"
    
 
    def braille_to_lang(self , lang='english', text = '' ):
        try:
            dict = self.langs[lang]
        except:
            dict = self.langs['english']
            string = 'could not find language chars...' 
            return string
        string  = ''
        for any in text:
            temp = find_value_by_key(dict , any )
            string += temp 
        return string

    def lang_to_braille(self , lang='english' , text='' ):
        try:
            dict = self.langs[lang]
        except:
            dict = self.langs['english']
            string = 'could not find language chars...' 
            return string
        string  = '' 
        for any in text:
            temp = find_key_by_value(dict , any)
            string += temp 
        return string

    def add_lang(self ,  lang_name:str , the_str):
        try:
            the_str = the_str.replace('\n' , '') 
            the_str = the_str.replace('  ' , '') 
            the_str = the_str.replace('}' , '') 
            the_str = the_str.replace('{' , '') 
            the_str = the_str.split(',') 
            temp_dict = {}
            for item in the_str:
                temp = item.split('=')
                temp_dict[temp[0]] = temp[1]
            print("\nn\n\n****    3     ***** \n\n\n")
            temp_dict['⠀'] = temp_dict.pop('space' , ' ')
            self.langs[lang_name] = temp_dict
            print(self.langs)
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