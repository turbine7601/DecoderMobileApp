import base64


class Decoder:
    @staticmethod
    def decode(text):
        print(text)
    @staticmethod    
    def decode_caesar(text:str, shift:int, *args):
        newtext = ""
        if not str(shift.isdigit()):
            shift = -1
        else:
            shift = int(shift)-2*int(shift)

        for i in text:
            if i.isalpha():
                d = shift % 26
                if i.islower():
                    if ord(i)+d > ord("z"):
                        newtext += chr((ord(i)+d)-26)
                    elif ord(i)+d < ord("a"):
                        newtext += chr((ord(i)+d)+26)
                    else:
                        newtext += chr(ord(i)+d)
                else:
                    if ord(i)+d > ord("Z"):
                        newtext += chr((ord(i)+d)-26)
                    elif ord(i)+d < ord("A"):
                        newtext += chr((ord(i)+d)+26)
                    else:
                        newtext += chr(ord(i)+d)
            else:
                newtext += i
        return(newtext)
    
    @staticmethod
    def decode_caesar_ru(text, shift, *args):
        newtext, n = [], ""

        if not str(shift.isdigit()):
            shift = -1
        else:
            shift = int(shift)-2*int(shift)

        
        dicti, dictiUpper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        for i in range(len(text)):
            if text[i] in dicti:
                n = dicti
            elif text[i] in dictiUpper:
                n = dictiUpper
            else:
                newtext.append(text[i])
            if text[i] in n:
                for j in range(len(n)):
                    if 0 <= j + shift < len(n) and text[i] == n[j]:
                        newtext.append(n[j+shift])
                    elif j + shift >= len(n) and text[i] == n[j]:
                        newtext.append(n[(1-j-shift)%(len(n)-1)])
                    elif j + shift < 0 and text[i] == n[j]:
                        newtext.append(n[(j+shift)%len(n)])
        return "".join(newtext)
    
    @staticmethod
    def Atbash(text, lang):
        nt=[]
        if lang == "ru":
            dict = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        elif lang == "en":
            dict = 'abcdefghijklmnopqrstuvwxyz'
        AtbashDict = ""
        for i in range(-1, (-1*len(dict)-1), -1):
            AtbashDict += dict[i]
        AtbashDictUpper = AtbashDict.upper()
        for v in text:
            if v.isalpha():
                if v.islower():
                    nt.append(AtbashDict[dict.find(v)])
                elif v.isupper():
                    nt.append(AtbashDictUpper[dict.upper().find(v)])
            else:
                nt.append(v)
        return "".join(nt)
    
    @staticmethod
    def Vignere(text, key, lang, mode='decrypt'):
        if lang == "ru":
            dict = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        elif lang == "en":
            dict = 'abcdefghijklmnopqrstuvwxyz'
        dictUp = dict.upper()

        nkey = (key*(len(text)//len(key)+1))[:len(text)]

        nt = []
        if mode == "decrypt":
            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i].islower():
                        shift = (dict.find(text[i])-dict.find(nkey[i]))%len(dict)
                        nt.append(dict[shift])
                    else:
                        shift = (dictUp.find(text[i])-dict.find(nkey[i].upper()))%len(dict)
                        nt.append(dictUp[shift])
                else:
                    nt.append(text[i])

        elif mode == 'encrypt':
            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i].islower():
                        shift = (dict.find(text[i])+dict.find(nkey[i]))%len(dict)
                        nt.append(dict[shift])
                    else:
                        shift = (dictUp.find(text[i])+dict.find(nkey[i].upper()))%len(dict)
                        nt.append(dictUp[shift])
                else:
                    nt.append(text[i])

        return "".join(nt)
    
    @staticmethod
    def BASE64(text, mode="d"):
        if mode == "d":
            return base64.b64decode(text.encode("utf-8")).decode("utf-8")
        else:
            return base64.b64encode(bytes(text, "utf-8")).decode("utf-8")
