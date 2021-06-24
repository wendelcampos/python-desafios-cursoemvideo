def checksite():
    from requests import get
    import urllib
    import urllib.request
    url = 'http://www.pudim.com.br'
    try:
        get(url, timeout=5)
        print('Consegui acessar o site Pudim com sucesso !')
    except ConnectionError:
        print('O site pudim nao esta acessivel no momento')


checksite()
