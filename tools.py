def lotin_krill(txt: str) -> str:
    lat_to_cyr = {
            'a': 'а', 'b': 'б', 'd': 'д', ' e': 'э', 'ye': 'е','yu': 'ю','yo': 'ё', 'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'ҳ',
            'i': 'и', 'j': 'ж', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', "o'": 'ў', 'p': 'п',
            'q': 'қ', 'r': 'р', 's': 'с', 'ch': 'ч','sh': 'ш', 't': 'т', 'u': 'у', 'v': 'в', 'w': 'в', 'x': 'х',
            'y': 'й', 'z': 'з',
            'A': 'А', 'B': 'Б', 'D': 'Д', ' E': 'Э', 'Ye': 'Е', 'Yu': 'Ю','Yo': 'Ё', 'E': 'Е', 'F': 'Ф', 'G': 'Г', 'H': 'Ҳ',
            'I': 'И', 'J': 'Ж', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', "O'": 'Ў', 'P': 'П',
            'Q': 'Қ', 'R': 'Р', 'S': 'С', 'Ch': 'Ч', 'Sh': 'Ш', 'T': 'Т', 'U': 'У', 'V': 'В', 'W': 'В', 'X': 'X',
            'Y': 'Й', 'Z': 'З',
            'а': 'a', 'б': 'b', 'д': 'd', 'ё':'yo',  'ф': 'f', 'г': 'g', 'ҳ': 'h',
            'и': 'i', 'ж': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
            'қ': 'q', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ў': "o’", 'в': 'v', 'в': 'w', 'х': 'x',
            'й': 'y', 'з': 'z',
            'А': 'A', 'Б': 'B', 'Д': 'D', 'Ё':'Yo', 'Е': 'Ye', 'Ф': 'F', 'Г': 'G', 'Ҳ': 'H',
            'И': 'I', 'Ж': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P',
            'Қ': 'Q', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ў': "O’", 'В': 'V', 'В': 'W', 'Х': 'X',
            'Й': 'Y', 'З': 'Z'
        }

    new_txt = ''
    l = len(txt)
    i = 0
    while i<l:
        if i+1 != l:
            if txt[i] in 'Yy':
                if txt[i+1] in 'eou':
                    new_txt += lat_to_cyr.get(txt[i:i+2], txt[i])
                    i+=1
                elif txt[i+1] in 'OUE':
                    new_txt += lat_to_cyr.get(txt[i:i+2].title(), txt[i])
                    i+=1
                else:
                    new_txt += lat_to_cyr.get(txt[i], txt[i])
            elif txt[i] in 'SscC':
                if txt[i+1] == 'h':
                    new_txt += lat_to_cyr.get(txt[i:i+2], txt[i])
                    i+=1
                elif txt[i+1] == 'H':
                    new_txt += lat_to_cyr.get(txt[i:i+2].title(), txt[i])
                    i+=1
                else:
                    new_txt += lat_to_cyr.get(txt[i], txt[i])
            elif txt[i] in 'oO':
                if txt[i+1] in "'’`":
                    new_txt += lat_to_cyr.get(txt[i]+"'", txt[i])
                    i+=1
                else:
                    new_txt += lat_to_cyr.get(txt[i], txt[i])
            elif txt[i] in 'eE':
                if i == 0:
                    new_txt += lat_to_cyr.get(' ' + txt[i], txt[i])
                elif txt[i-1] == " ":
                    new_txt += lat_to_cyr.get(txt[i-1:i+1], txt[i])
                else:
                    new_txt += lat_to_cyr.get(txt[i], txt[i])
            else:
                new_txt += lat_to_cyr.get(txt[i], txt[i])
        else:
            new_txt += lat_to_cyr.get(txt[i], txt[i])
        i += 1
    return new_txt