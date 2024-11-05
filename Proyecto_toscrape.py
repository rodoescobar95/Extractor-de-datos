import bs4
import requests

# Loop for que recorra todas las paginas, todos los libros de cada pagina
# que vea si tiene 4 o 5 estrellas, y si se cumple, tomar el titulo

# crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar paginas
for pagina in range(1, 51):
    # crear sopa en cada pag
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # variable que selecciona datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:
        # checar que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar el libro a la lista de rating alto
            titulos_rating_alto.append(titulo_libro)

# Ver los libros de 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)
