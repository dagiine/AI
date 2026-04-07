# normalize_test(text)
# orolt ni text 
# garalt ni buh useg jijig, temdegtiig hoooson zaigaar solih, olon hooson zaig neg hooson zai bolgoh, 
# ehlel tugsguliig zaig baihgui bolgonono
from copy import replace

def normalize_text(text):
    text = text.lower()

    punctuations = "!?.,£$%^&*()_+-=~<>/;:"
    for ch in text:
        if ch in punctuations:
            text = text.replace(ch, " ")
    
    text = " ".join(text.split())
    text = text.strip()

    return text

# word_tokens(text) ugnuudiig neg negeer ni [[],[]] gej butsaana
def word_tokens(text):
    words = text.split()
    return words

a = "    hello!   &hi how are  you£$   ?"
print(normalize_text(a))
print(word_tokens(normalize_text(a)))