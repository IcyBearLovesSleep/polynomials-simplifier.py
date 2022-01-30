import re
def simplify(poly):
    matches = re.findall(r'([+-]?)(\d*)([a-z]+)', poly)
    expanded = [[int(i[0] + (i[1] if i[1] != "" else "1")), ''.join(sorted(i[2]))] for i in matches]
    varb = sorted(list(set(i[1] for i in expanded)), key=lambda x: (len(x), x))
    coef = {v:sum(i[0] for i in expanded if i[1] == v) for v in varb}
    a=[str(coef[v]) + v if coef[v] not in [-1,1] else (str(coef[v]).replace('1','') + v) for v in varb if coef[v] != 0]
    return '+'.join(a).replace('+-','-')
