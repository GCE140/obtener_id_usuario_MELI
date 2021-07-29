import requests, json
from requests.api import request
from requests.exceptions import HTTPError


def ver_id(nickname):
    for url in [f'https://api.mercadolibre.com/sites/MLA/search?nickname={nickname}']:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error: {http_err}')
        except Exception as err:    
            print(f'Otro error sucedió: {err}')
        else:
            print('Conexión correta!')
            json_data = json.loads(response.text)
    print()

    seller_id = json_data["seller"]["id"]
    print("El ID del usuario es:\t" + str(seller_id))
    print()


if __name__ == "__main__":
    print("\nBIENVENIDO/A ESTE PROGRAMA OBTIENE EL ID DE UN USUARIO DE MERCADO LIBRE DANDO EL NOMBRE DE USUARIO:\n")

    print("Ejemplo: https://www.mercadolibre.com.ar/perfil/SPORTLINE+OFICIAL?brandId=273, el nombre es SPORTLINE+OFICIAL\n")
    nickname = input("Ingrese el nombre del usuario de Mercado Libre: ")
    print()
    ver_id(nickname)
