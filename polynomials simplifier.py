import re
# import the re module

def simplify(poly):
    # creates the function for simplifying polynomials
    # only takes in a string type "poly"
    
    matches = re.findall(r'([+-]?)(\d*)([a-z]+)', poly)
    # poly string is divided into a 2d list, each element consists of all string types [operator], [coefficient digit], [variable]
    # list named matches
    
    expanded = [[int(i[0] + (i[1] if i[1] != "" else "1")), ''.join(sorted(i[2]))] for i in matches]
    # from list matches, join [opertor] and [coefficient digit], converted to integers type, then added with [vairable] in a list 
    # if [coefficient digit] is empty, then is assigned to "1"
    # stored into a new 2d list named expanded consists of interger type [joined coefficient], string type [variable]
    
    varb = sorted(list(set(i[1] for i in expanded)), key=lambda x: (len(x), x))
    # from list expanded, variables duplicates are removed, then sorted firstly by length, secondly by alphabetical order
    # stored into a new list named varbconsists of string type [variable]
    
    coef = {v:sum(i[0] for i in expanded if i[1] == v) for v in varb}
    # from list varb, from list expanded,  if [variable] in expanded matches [variable] in varb, integer type [joined coefficient] in expanded are summed together
    # stored into a new dictionary named coef consists of -[variable] : integertype [joined coefficient]-
    
    temp=[str(coef[v]) + v if coef[v] not in [-1,1] else (str(coef[v]).replace('1','') + v) for v in varb if coef[v] != 0]
    # from list varb, if [variable] matches key [variable] from dictionary coef, value [joined coefficient] is converted to string type, then join with [variable] as string
    # if [joined coefficient] is 0 then ignored
    # if [joined coefficient] is "-1" or "1" then "1" is removed
    # stored into a new list temp consists of string type [polynomials]
    
    return '+'.join(temp).replace('+-','-')
    # list temp is joined together with character operator "+"
    # if both character "+" and "-" is found together, then "+" is removed
    # reuturn the string type final simplified polynomial 