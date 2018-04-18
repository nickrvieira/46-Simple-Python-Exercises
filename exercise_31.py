# Exercise 31:
# ======================
# Implement the higher order functions map(), filter() and reduce(). 
# (They are builtin but writing them yourself may be a good exercise.)

swe_dictionary = {"merry":"god","christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"} 


def custom_map(func, input_list):
    return [func(element) for element in input_list]


def custom_filter(func, input_list):
    return [element for element in input_list if func(element)]

def custom_reduce(func, input_list):
    evaluation_var = input_list[0]
    for value in input_list[1:]:
        evaluation_var = func(evaluation_var,value)
    return evaluation_var

#This way ignores any chracter non present in the swe_dict; (Returning None)

if __name__ == '__main__':
    print(custom_map(swe_dictionary.get,['merry','christmas','happy']))
    print(custom_map(lambda x: swe_dictionary.get(x),['merry','christmas','happy']))
    
    print(custom_filter(lambda x: len(x) > 3, ['word','teste','xatuba','hi']))
    
    print(custom_reduce(max,[1,2,3,5,10,25,2]))
    print(custom_reduce(min,[1,2,3,5,10,25,2]))
