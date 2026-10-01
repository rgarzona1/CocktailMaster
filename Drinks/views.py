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

#SECCION DE COCTELES POR ALCOHOL, API SOLO DEVUELVE 1 COCKTAIL POR LO TANTO
#SE CREARAN LISTAS CON NOMBRES PARA DEJAR DEFINIDOS LOS QUE SE VERAN EN CUADRICULA


cocteles_por_alcohol = { "vodka": [
        "Moscow Mule",
        "Vodka Martini",
        "Bloody Mary",
        "White Russian",
        "Black Russian",
        "Cosmopolitan",
        "Screwdriver",
        "Vodka Tonic",
        "Lemon Drop",
        "Espresso Martini",
        "Sea Breeze",
        "Cape Codder",
    ],

    "gin": [
        "Gin Tonic",
        "Negroni",
        "Tom Collins",
        "Gin Fizz",
        "Gimlet",
        "Martini",
        "French 75",
        "Singapore Sling",
        "Aviation",
        "Bee's Knees",
        "Southside",
        "Clover Club",
    ],

    "rum": [
        "Mojito",
        "Daiquiri",
        "Piña Colada",
        "Cuba Libre",
        "Mai Tai",
        "Dark and Stormy",
        "Hurricane",
        "Rum Punch",
        "Planter's Punch",
        "Zombie",
        "Bahama Mama",
        "Painkiller",
    ],

    "tequila": [
        "Margarita",
        "Tequila Sunrise",
        "Paloma",
        "Tequila Sour",
        "Matador",
        "Mexican Mule",
        "Juan Collins",
        "El Diablo",
        "Tequila Mockingbird",
        "Brave Bull",
        "Acapulco",
        "Tequila Smash",
    ],

    "whiskey": [
        "Old Fashioned",
        "Whiskey Sour",
        "Manhattan",
        "Mint Julep",
        "Boulevardier",
        "Irish Coffee",
        "Rusty Nail",
        "John Collins",
        "Whiskey Smash",
        "Rob Roy",
        "New York Sour",
        "Godfather",
    ],
}
    

def tragos_por_alcohol(request, alcohol):
    cocteles = cocteles_por_alcohol.get(alcohol.lower(), [])

    tragos = []

    for nombre in cocteles:

        url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"

        response = requests.get(
            url,
            params={"s": nombre}
        )

        if response.status_code == 200:

            data = response.json()

            resultados = data.get("drinks") or []

            if resultados:
                tragos.append(resultados[0])

    return render(
        request,
        "Drinks/tragos_por_alcohol.html",
        {
            "alcohol": alcohol,
            "tragos": tragos
        }
    )
    
