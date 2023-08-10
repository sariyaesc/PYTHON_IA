#%%
import requests
from bs4 import BeautifulSoup

#%%
def obtener_contenido_pagina(url):
    respone=requests.get(url)
    return respone.text

def analizar_contenido_html(html):
    return BeautifulSoup(html,'html.parser')

#%%


def procesar_pagina(soup):
    titulos=[]
    tomatoers=[] 
    audience_scores=[]
    estrenos=[]

    #titulos
    titulo_items=soup.find_all('span',class_='p--small')
    
    for item in titulo_items:
        titulo=item.text.strip()
        titulos.append(titulo)

    #tomatoers
    tomatoers_items=soup.find_all('score-icon-critic',class_='pr')
    print(tomatoers_items)


# %%

#pa hacer pruebas jiji

html=obtener_contenido_pagina(url="https://www.rottentomatoes.com/browse/movies_in_theaters/")
soup=analizar_contenido_html(html)

procesar_pagina(soup)
# %%
