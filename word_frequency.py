
def calculate_word_frequency(text):
    alpha = 'A'
    result = 0
    cipher_key = {}
    counted_list={}
    for i in range(1,27):
        for letter in text:
            if letter == alpha:
                result += 1  # same as result = result + 1
        counted_list.update({alpha:result})
        alpha = chr(ord(alpha) + 1)
        result = 0
    output_dict = dict(sorted(counted_list.items(),key=lambda item: item[1]))
    index = 1
    for key, value in output_dict.items():
        cipher_key = output_dict.update({key:index})
        index += 1
    output_dict = {k: v for k, v in output_dict.items()}
    return output_dict

def calculate_key(cipher_ordered_text):
    output ={}
    alphabet = {"L": 1, "Z": 2, "J": 3, "Q": 4, "X": 5, "K": 6, "V": 7, "W": 8, "B": 9, "Y": 10, "G": 11, "F": 12,
                "U": 13, "P": 14, "D": 15, "M": 16, "H": 17, "C": 18, "R": 19, "N": 20, "S": 21, "O": 22, "A": 23,
                "I": 24, "T": 25, "E": 26}
    inv_alphabet = {v: k for k, v in alphabet.items()}
    for key,value in inv_alphabet.items():
        for k,v in cipher_ordered_text.items():
            if v == key :
                cipher_ordered_text[k]= inv_alphabet[v]
    return cipher_ordered_text
def get_plain_text (ciphertext,cipher_key):
    plaintext = ['']*len(ciphertext)
    index = 1
    for char in ciphertext:

        if char == " ":
            replacement  = ''
        else:
            replacement = cipher_key[char]
        plaintext[index] = replacement
        index+=1
    return plaintext


Cipher_text  = "FWPAY FEALS NVXLO ETAYS XIRHQ XSAHQ OIZES AYVHR CYZWR AJNHR NCRYQ BYIHG DYHHC DIRHQ XSAHQ TJJEZ ECKMV LYRHA HJVKY ZMXLA NJNHC DIHGS BEFVK XBPHH BYVHR AKPUB IWREA EHMWQ NPNHC DCJMO DVEBU OVPSS BEMWQ NVRSA DADWK DDQTN PYDSR NIFVK XBPTB MVPKO PPNQY DEYKQ ASQIV FWVAB VSDLO AAAIS NSAFY FEALY DMPVD OWUMO AYNIS"
##alphabet=[("L" , 1),("Z" , 2),("J" , 3),("Q" , 4),("X" , 5),("K" , 6),("V" , 7),("W" , 8),("B" , 9),("Y" , 10),("G" , 11),("F" , 12),("U" , 13),("P" , 14),("D" , 15),("M" , 16),("H" , 17),("C" , 18),("R" , 19),("N" , 20),("S" , 21),("O" , 22),("A" , 23),("I" , 24),("T" , 25),("E" , 26)]
alphabet={"L" : 1,"Z" : 2,"J" : 3,"Q" : 4,"X" : 5,"K" : 6,"V" : 7,"W" : 8,"B" : 9,"Y" : 10,"G" : 11,"F" : 12,"U" : 13,"P" : 14,"D" : 15,"M" : 16,"H" : 17,"C" : 18,"R" : 19,"N" : 20,"S" : 21,"O" : 22,"A" : 23,"I" : 24,"T" : 25,"E" : 26}
print(calculate_word_frequency(Cipher_text))

print(calculate_key(calculate_word_frequency(Cipher_text)))
print(get_plain_text(Cipher_text,calculate_key(calculate_word_frequency(Cipher_text))))