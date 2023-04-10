# coding=utf8
import pandas as pd
from langdetect import detect, detect_langs
import re


def words_search(text):
    char_dict_eng_to_ua = {'A':'А','B':'В','C':'С','E':'Е','H':'Н','I':'І','K':'К','M':'М','O':'О','P':'Р','T':'Т','X':'Х','Y':'У',"'":'’'}
    char_dict_ua_to_eng = {'А':'A','В':'B','С':'C','Е':'E','Н':'H','І':'I','К':'K','М':'M','О':'O','Р':'P','Т':'T','Х':'X','У':'Y',"'":'’'}
    excel_data = pd.read_excel('db2.xlsx', engine='openpyxl')
    up_excel_data = pd.read_excel('db2.xlsx', engine='openpyxl')
    df = pd.DataFrame(excel_data)
    up_df = pd.DataFrame(up_excel_data)
    up_df[['eng', 'ukr']] = up_df.astype('string')
    df[['eng', 'ukr']] = df.astype('string')
    up_df['ukr'] = up_df['ukr'].fillna('').apply(lambda x: x.upper())
    up_df['eng'] = up_df['eng'].fillna('').apply(lambda x: x.upper())
    translation = []
    text = text.upper()
    text.replace(' | ', ' ')
    text.replace('|', '')
    new_list = text.split('\n')
    #new_list = " ".join(new_list)
    #new_list = re.split(r'(?<=[\:\;\.\!\?])\s*', new_list)
    print(new_list)

    for i in new_list:
        #i.replace('\r\n', '')
        if i == '':
            new_list.remove(i)

    for part in new_list:
        if detect(part) == 'uk' or detect(part) == 'ru' or detect(part) == 'be' or detect(part) == 'bg':
            part = part.translate(str.maketrans(char_dict_eng_to_ua))
            for i in up_df['ukr']:
                if i == part:
                    part_translation = df['eng'][up_df[up_df['ukr'] == i].index]
                    translation.append(part_translation.to_string(index=False, dtype=False))
                else:
                    pass

        else:
            part = part.translate(str.maketrans(char_dict_ua_to_eng))
            for i in up_df['eng']:
                if i == part:
                    part_translation = df['ukr'][up_df[up_df['eng'] == i].index]
                    translation.append(part_translation.to_string(index=False, dtype=False))
                else:
                    pass

    print(translation)
    return translation

