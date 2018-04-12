# Exercise 20:
# ======================
# Represent a small bilingual lexicon as a Python dictionary in the following fashion 
# {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} 
# and use it to translate your Christmas cards from English into Swedish.
# That is, write a function translate() that takes a list of English words and returns a list of Swedish words.

swe_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}

def translate(english_words_list):
    swenglish_list = [swe_dict.get(word.lower(), word) for word in english_words_list]
    return swenglish_list


if __name__ == "__main__":
    print("Happy new Year!")
    print(translate(['happy','new','year'])) #['gott', 'nytt', 'år']
    print(translate(['Hello','happy','new','year','my','friend'])) #['Hello', 'gott', 'nytt', 'år', 'my', 'friend']