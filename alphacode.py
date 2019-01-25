def alphacode(pin):
    """
    Convert numeric pin code to an
    easily pronounced mnemonic.
    args:
        pin:  code as positive integer
    returns:
        mnemonic as string
    """
    mnemonic = str(pin)
    n = 2
    mnemonic = [mnemonic[i:i+n] for i in range (0, len(mnemonic), n)]

    for i in mneomic:
        vowel_conversion = int(









CONSONANTS = "bcdfghjklmnpqrstvwyz"
VOWELS = "aeiou"
counter = 0
def alphacode(pin):
    """
    Convert numeric pin code to an
    easily pronounced mnemonic.
    args:
       pin: code as positive integer
    returns:
       mnemonic as string
    """
    #FIXME: Your code replaces the next line
    mnemonic = pin
    CONSONANTS_LIST = list(CONSONANTS)
    VOWELS_LIST = list(VOWELS)
    
    number_string = str(pin) #Turns PIN into string
    
    string_length = len(number_string) #Determines length of the PIN

    x = 0

    while x < string_length:
        if (string_length % 2) == 0:
            #--------------------------------------------------------------------    
            first_half = (number_string[0+x])+(number_string[1+x]) #This works
            #print(first_half)
            first_half_int = int(first_half)
            first_half_result_5k = first_half_int//5
            first_half_result_remainder = int(abs(first_half_int - first_half_result_5k*5))
            first_digit = CONSONANTS_LIST[first_half_result_5k]
            second_digit = VOWELS_LIST[first_half_result_remainder]
            first_digit_string = str(first_digit)
            second_digit_string = str(second_digit)
            combination0 = first_digit_string + second_digit_string

            x = x + 2

            print(combination0)
        else:
            print("Please input a PIN with even numbers")
            x = string_length

alphacode(4327)
print('-'*15)
alphacode(43274327)
alphacode(65473)
