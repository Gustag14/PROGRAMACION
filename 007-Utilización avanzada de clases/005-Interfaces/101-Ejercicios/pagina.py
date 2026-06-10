import requests
from lxml import html

paginas = [
"https://gustavo.com",
  
]

for pagina in paginas:
    print("Analizando:", pagina)

    try:
        respuesta = requests.get(pagina, timeout=10)
        respuesta.raise_for_status()

        arbol = html.fromstring(respuesta.content)
        titulos = arbol.xpath("//h1")

        for titulo in titulos:
            print("Título encontrado:", titulo.text_content().strip())

    except:
        print("No se ha podido analizar esta página")

    print("----------------------")