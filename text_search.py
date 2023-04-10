# coding=utf8
import pandas as pd
from langdetect import detect
import re


def text_search(text):
    char_dict_eng_to_ua = {'A':'А','B':'В','C':'С','E':'Е','H':'Н','I':'І','K':'К','M':'М','O':'О','P':'Р','T':'Т','X':'Х','Y':'У',"'":'’'}
    char_dict_ua_to_eng = {'А':'A','В':'B','С':'C','Е':'E','Н':'H','І':'I','К':'K','М':'M','О':'O','Р':'P','Т':'T','Х':'X','У':'Y',"'":'’'}
    excel_data = pd.read_excel('db.xlsx', engine='openpyxl')
    up_excel_data = pd.read_excel('db.xlsx', engine='openpyxl')
    df = pd.DataFrame(excel_data)
    up_df = pd.DataFrame(up_excel_data)
    up_df = up_df.apply(lambda x: x.astype(str).str.upper())
    translation = []
    text = text.upper()

    lst = list(text)
    str0 = ''
    for i in lst:
        str0 += i
    str0 = str0.replace(' | ', ' ')
    str0 = str0.replace(' - ', ' ')
    str0 = str0.replace('  ', ' ')
    lst1 = re.split("[\n]", str0)
    str1 = ""
    for i in lst1:
        str1 += i + " "
    str2 = str1[:-2]

    new_text = re.split("[.:|;]", str2)

    final_text = []
    for i in new_text:
        if i == '':
            new_text.remove(i)
        else:
            new_i = i.strip()
            new_i = new_i + '.'
            final_text.append(new_i)

    for part in final_text:
        if detect(part) == 'uk' or detect(part) == 'ru' or detect(part) == 'be' or detect(part) == 'bg':
            part = part.translate(str.maketrans(char_dict_eng_to_ua))
            for i in up_df['ukr']:
                if i == part:
                    part_translation = df['eng'][up_df[up_df['ukr'] == i].index]
                    print(part_translation)
                    translation.append(part_translation.to_string(index=False, dtype=False))
                else:
                    pass

        else:
            part = part.translate(str.maketrans(char_dict_ua_to_eng))
            for i in up_df['eng']:
                if i == part:
                    part_translation = df['ukr'][up_df[up_df['eng'] == i].index]
                    print(part_translation)
                    translation.append(part_translation.to_string(index=False, dtype=False))
                else:
                    pass

    return translation

