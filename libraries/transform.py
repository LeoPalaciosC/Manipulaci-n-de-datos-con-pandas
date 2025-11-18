import re
from collections import Counter


def process_text(text):

    # Remover signos de puntuación y convertir texto a minuscula
    text = re.sub(r'[\?\.\!,]','',text)

    # Split text into words
    words = text.split()

    # Cotar cantidad de palabras
    conteo_palabras = Counter(words)

    return conteo_palabras


def par_o_impar(numero):
  """
   Esta función calcula si un número es par o impar
  """
  if numero %2 == 0:
    print('Es par')
  else:
       print('Es impar')


