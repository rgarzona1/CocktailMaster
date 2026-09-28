from django.http import JsonResponse
from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    return render (request, 'Drinks\home.html')

def obtener_cocteles(request):
    destacados = []
    for i in range(3):
        response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
        if response.status_code==200:
            data= response.json()
            cocktail= data ['drinks'][0]
            destacados.append({
                'nombre': cocktail['strDrink'],
                'imagen': cocktail['strDrinkThumb'],
                'categoria': cocktail['strCategory'],
                'instrucciones': cocktail['strInstructions'],
            })
    return JsonResponse({'destacados': destacados} )

#SECCION DE COCTELES POR CATEGORIA

def tragos_por_alcohol(request, alcohol):
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"

    response = requests.get(
        url,
        params={"i": alcohol}
    )

    if response.status_code == 200:
        data = response.json()
        tragos = data.get("drinks") or []
    else:
        tragos = []

    return render(
        request,
        "Drinks/tragos_por_alcohol.html",
        {
            "alcohol": alcohol,
            "tragos": tragos
        }
    )