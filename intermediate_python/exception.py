#this is an exception for a case when a key doesnt exsist

acronyms = {'LOL':'Laugh out loud', 'IDK':"I dont know", 'TBH': 'To be honest'}

try:
    definition = acronyms['BTW'] #this would result in a Key Error
#do this instead try/except :) 
except:
    print('The key does not exist')
finally:
    print('The acronyms we have defined are:')
    for acronym in acronyms:
        print(acronym)
print('The program keeps going...')

