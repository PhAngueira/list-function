var = int(input('Número: '))

#1 ou 2 ou 3
#4 ou 5 ou 6
#7 ou 8 ou 9
# nenhum

if var==1 or var==2 or var ==3:
    print('1, 2 ou 3')
elif var==4 or var ==5 or var==6:
    print('4, 5 ou 6')
elif var==7 or var==8 or var==9:
    print('7, 8 ou 9')
else:
    print('nenhuma opção!')

#===================================

match var:
    case 1|2|3:
        print('1, 2 ou 3')
    case 4|5|6:
        print('4, 5 ou 6')
    case 7|8|9:
        print('7, 8 ou 9')
    case _:
        print('nenhuma opção!')


        
