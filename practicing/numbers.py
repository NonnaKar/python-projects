num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num += 1 # num = num + 1
    tot += fval # tot = tot + fval

print(tot,num,tot/num)