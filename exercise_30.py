# Exercise 30:
# ======================
# Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god",
# "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and
# use it to translate your Christmas cards from English into Swedish. Use the higher order function map() to
# write a function translate() that takes a list of English words and returns a list of Swedish words.

swe_dictionary = {"merry":"god","christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"} 

def translate(list_english):
    return list(map (swe_dictionary.get,list_english))

#This way ignores any chracter non present in the swe_dict; (Returning None)

if __name__ == '__main__':
    print(translate(['merry','christmas','happy']))