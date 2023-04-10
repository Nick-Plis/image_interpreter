from text_search import text_search
from words_search import words_search
from jpg_to_str import img_to_str

def main_func(image):
    text = img_to_str(image)
    ans = int(input("Text(1) or words(2)? "))
    if ans == 1:
        translation = text_search(text)
    elif ans == 2:
        translation = words_search(text)
    else:
        print('Error')

    input('Press Enter to finish')

    return translation






