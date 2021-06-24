def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÂO VOTA.'
    elif idade >= 16 and idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'
    elif idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'


idade = int(input('Em que ano você nasceu? '))
print(voto(idade))
