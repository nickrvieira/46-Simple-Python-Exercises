# Exercise 24:
# ======================
# The third person singular verb form in English is distinguished by the suffix s,
# which is added to the stem of
# the infinitive form: run >
# runs. A simple set of rules can be given as follows:
# 1. If the verb ends in y, remove it and add ies
# 2. If the verb ends in o, ch, s, sh, x or z, add es
# 3. By default just add s
# Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form
# returns its third person singular form. Test your function with words like try, brush, run and fix. Note however
# that the rules must be regarded as heuristic, in the sense that you must not expect them to work for all
# cases. Tip: Check out the string method endswith().



def make_3sg_form(verb):
    if verb.endswith("y"): 
        return verb[:-1]+'ies'
    elif verb.endswith(('o','ch','s','sh','x','z')):
        return verb+'es'
    else:
        return verb+'s'


if __name__ == '__main__':
    print(make_3sg_form('brush'))
    print(make_3sg_form('run'))
    print(make_3sg_form('fix'))
    print(make_3sg_form('study'))