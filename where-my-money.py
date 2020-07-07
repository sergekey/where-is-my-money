print('\nДавай-ка посчитаем куда бабки потратились!\n')

еда = []
одежда = []
общее = []
налоги = []
квартплата = []
аптека = []
собака = []
кафе = []


enter = True
while enter:
    choose = input('Выбери тип затрат: \n1 - еда\n2 - одежда\n3 - общие\n4 - налоги\n5 - квартплата\n6 - аптека\n7 - собака\n8 - кафе\n0 - стоп\n')

    if choose == '1':
        food = int(input('сколько потратили на еду: '))
        еда.append(food)

    elif choose == '2':
        clothes = int(input('сколько потратили одежду: '))
        одежда.append(clothes)

    elif choose == '3':
        common = int(input('сколько потратили на всякую фигню: '))
        общее.append(common)

    elif choose == '4':
        fees = int(input('сколько потратили на налоги: '))
        налоги.append(fees)

    elif choose == '5':
        rent = int(input('сколько потратили на коммуналку: '))
        квартплата.append(rent)

    elif choose == '6':
        meds = int(input('сколько потратили на медицину: '))
        аптека.append(meds)

    elif choose == '7':
        dog = int(input('сколько потратили на собачку: '))
        собака.append(dog)

    elif choose == '8':
        rest = int(input('сколько потратили на красивую жизнь: '))
        кафе.append(rest)

    elif choose == 'стоп' or '0':
        enter = False

    else:
        enter = False


all_food = sum(еда)
print('всего наели на ' + str(all_food) + 'грн.')

all_clothes = sum(одежда)
print('всего оделись на ' + str(all_clothes) + 'грн.')

all_common = sum(общее)
print('всего накупили всякой фигни на ' + str(all_common) +'грн.')

all_fees = sum(налоги)
print('всего на налоги ушло ' + str(all_fees) +'грн.')

all_rent = sum(квартплата)
print('всего на коммуналку ушло ' + str(all_rent) +'грн.')

all_meds = sum(аптека)
print('всего на здоровье потрачено ' + str(all_meds) +'грн.')

all_dog = sum(собака)
print('всего на собакена потратили ' + str(all_dog) +'грн.')

all_rest = sum(кафе)
print('всего на кафешечки потрачено ' + str(all_rest) +'грн.')

total = all_common + all_clothes + all_food + all_fees + all_rent + all_meds + all_dog + all_rest
print('Итого было потрачено ' + str(total) + 'грн.\nИгра цифр, да?\nИди работай!\n :)')