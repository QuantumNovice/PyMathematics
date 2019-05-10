formulas = {'r**2':'a**2+b**2'}


x = 'r**2'
for i in formulas:
    if i in x:
        x=x.replace(i, formulas[i])
