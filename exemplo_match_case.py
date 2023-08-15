linguagem= input('Qual linguagem de programação você gostaria de aprender?')

match linguagem:
    case 'JavaScript':
        print('Você pode ser tornar um desenvolvedor web')
    case 'Python':
        print('Você pode ser tornar um Cientista de Dados')
    case 'PHP':
        print('Você pode ser tornar um desenvolvedor backend')
    case 'Java':
        print('Você pode ser tornar um desenvolvedor mobile')
    case 'Solidity':
        print('Você pode ser tornar um desenvolvedor Blockchain')
    case _:
        print('Não conheço essa linguagem!!!')
