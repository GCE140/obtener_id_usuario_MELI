# Get Mercado Libre User ID

## Table of contents
* [General info](#general-info)
* [How it works](#how-it-works)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This script allows you to obtain the ID of a Mercado Libre user knowing its name.

## How it works
This program consults the Mercado Libre API as explained in https://developers.mercadolibre.com.ar/es_ar/producto-consulta-usuarios#ID-usuario.

The response obtained from the API is in JSON format, so to work with it, the json and requests modules are necessary in order to be able to send the GET to the API url.
	
## Technologies
Project is created with:
* Python 3.9
* requests 2.26.0
	
## Setup
To run this project, install locally:
* pip install requests
