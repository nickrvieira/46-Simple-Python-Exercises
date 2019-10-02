# Exercise 25:
# ======================
# In English, the present participle is formed by adding the suffix ­ing to the infinite form: go ­> going.
# A simple set of heuristic rules can be given as follows:
# 1. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# 2. If the verb ends in ie, change ie to y and add ing 
# 3. For words consisting of consonant­vowel­consonant, double the final letter before adding ing 
# 4. By default just add ing
# Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
# returns its present participle form. Test your function with words such as lie, see, move and hug.
# However, you must not expect such simple rules to work for all cases.

def check_consonant_ending(verb):
    vowels = ['a','e','i','o','u']
    return verb[-1] not in vowels and verb[-2] in vowels and verb[-3] not in vowels


def make_ing_form(verb):
    exceptions = ['be','see','flee','knee']
    if verb.endswith('ie'):
        return verb[:-2]+'ying'        
    elif verb.endswith("e") and verb not in exceptions:
        return verb[:-1]+'ing'
    elif check_consonant_ending(verb):
        return verb+verb[-1]+'ing'
    else:
        return verb+'ing'


if __name__ == '__main__':
    print(make_ing_form('lie')) #lying 
    print(make_ing_form('see')) #seeing
    print(make_ing_form('move')) #moving
    print(make_ing_form('hug')) #hugging
    print(make_ing_form('travel')) #travelling