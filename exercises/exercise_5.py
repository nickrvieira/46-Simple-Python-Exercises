# Exercise 5:
# ======================

# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's
# language"). That is, double every consonant and place an occurrence of "o" in between. For example,
# translate("this is fun") should return the string "tothohisos isos fofunon"

def translate_rovarspraket(str):
    new_str = ""
    for letter in str:
        if letter.lower() not in ['a','e','i','o','u',' ']:
            new_str += letter+'o'+letter.lower()
        else:
            new_str += letter
    return new_str

print(translate_rovarspraket('This is Fun')) #>Tothohisos isos Fofunon
print(translate_rovarspraket('This is Fun!')) # > Tothohisos isos Fofunon!o! - Wrong due to !



import string
def full_translator(str):
    new_str = ""
    all_characters = string.ascii_letters
    vowels = ['a','e','i','o','u', ]
    consonants = [ letter for letter in all_characters if letter.lower() not in vowels ]
    for letter in str:
        if letter in consonants:
            new_str += letter+'o'+letter.lower()
        else:
            new_str +=letter
    return new_str

print(full_translator('This_is_Fun!')) #>Tothohisos_isos_Fofunon!
print(full_translator('This is Fun!')) #>Tothohisos isos Fofunon!



#There are two approaches: One of them ignoring all special characters (or only considering space as one), and being more simplistic yet more ~clean~
#Or consider all consonants (and check all of them) in order to avoid issues such as: 
# translate_rovarspraket('This is Fun!')
# > Tothohisos isos Fofunon!o!
# (! traslanted as -> !o! )