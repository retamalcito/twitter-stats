from prepare_db import create_dfs
from most_retweets import most_retweets

users, tweets = create_dfs()

active = True
while active:
    print('[1] 10 tweets más retweeteados')
    print('[2] 10 usuarios con más tweets')
    print('[3] 10 días con más tweets')
    print('[4] 10 hashtags más usados')
    print('[5] Salir')
    pick = input('¿Qué función desea realizar? ')
    print()

    if pick == '1':
        result = most_retweets(users, tweets, 10)
        print(result.head(10))
        print()

    elif pick == '2':
        pass

    elif pick == '3':
        pass

    elif pick == '4':
        pass

    elif pick == '5':
        active = False
        print('¡Adiós!')

    else:
        print('Comando no válido')
        print()
