import requests
import folium
from flask import Flask, render_template, request
from markupsafe import Markup  # Alterado para importar Markup corretamente

app = Flask(__name__)

API_KEY = 'ccf2041c97680815dc7272db98f0493d'

# Função para obter dados meteorológicos
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt_br"
    response = requests.get(url)
    return response.json()

# Função para criar um mapa com os dados climáticos
def create_weather_map(city):
    weather_data = get_weather_data(city)

    if weather_data.get("cod") != 200:
        return None, f"Erro: {weather_data.get('message', 'Não foi possível encontrar dados para essa cidade.')}"

    # Extraindo as coordenadas da cidade
    lat = weather_data['coord']['lat']
    lon = weather_data['coord']['lon']

    # Criando o mapa com Folium
    weather_map = folium.Map(location=[lat, lon], zoom_start=10)

    # Adicionando um marcador no mapa com as informações do clima
    info = f"Temperatura: {weather_data['main']['temp']}°C<br>"
    info += f"Descrição: {weather_data['weather'][0]['description'].capitalize()}<br>"
    info += f"Humidade: {weather_data['main']['humidity']}%<br>"
    info += f"Vento: {weather_data['wind']['speed']} m/s"

    folium.Marker([lat, lon], popup=info).add_to(weather_map)

    # Gerando o HTML do mapa em vez de salvar como arquivo
    map_html = weather_map._repr_html_()

    return weather_data, map_html, None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    weather_data, map_html, error = create_weather_map(city)

    if error:
        return render_template('index.html', error=error)

    # Renderizando o template com os dados do clima e o mapa
    return render_template('weather_map.html', city=city, weather=weather_data, map_html=Markup(map_html))

if __name__ == '__main__':
    app.run(debug=True)
