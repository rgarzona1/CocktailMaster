from django.shortcuts import render
import requests

# Create your views here.

def home (request):
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
    return render(request, 'Drinks/home.html', {'destacados': destacados} )