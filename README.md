# Previsão do Tempo 🌦️

Este é um aplicativo web simples que utiliza Flask e Folium para exibir dados meteorológicos em um mapa interativo
com base na cidade inserida pelo usuário. Os dados são fornecidos pela API OpenWeatherMap.

## 🚀 Funcionalidades

- **Busca de clima**: O usuário insere o nome de uma cidade e recebe informações como temperatura, descrição do clima, umidade e velocidade do vento.
- **Mapa interativo**: Exibe a localização da cidade em um mapa com as informações climáticas.
- **Interface limpa**: Utiliza HTML, CSS e Bootstrap para um layout responsivo e fácil de usar.

## 🛠 Tecnologias Utilizadas

- **Back-end**: Flask
- **Front-end**: HTML, CSS (Bootstrap)
- **API**: OpenWeatherMap
- **Mapas**: Folium
- **Linguagem** Python

## 📦 Estrutura do Projeto

```bash
previsao-do-tempo/
├── main.py          # Código principal do aplicativo Flask
├── static/
│   └── style.css    # Arquivo de estilização CSS
├── templates/
│   ├── index.html   # Página inicial do aplicativo
│   └── weather_map.html # Página com o mapa e detalhes climáticos
└── requirements.txt # Lista de dependências Python
```

## 📋 Pré-requisitos

Antes de executar o projeto, você precisará ter instalado em sua máquina:

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

## 📚 Bibliotecas Utilizadas
  O projeto utiliza as seguintes bibliotecas Python:

- **Flask**: Framework web para Python.
- **Requests**: Biblioteca para fazer requisições HTTP, utilizada para consumir a API OpenWeatherMap.
- **Folium**: Utilizada para criar mapas interativos.
- **MarkupSafe**: Necessária para manipulação segura de HTML em Flask.
  
  Pode instalar as bibliotecas uma por uma diretamente no terminal ou no prompt de comando. Execute os comandos:
  ```bash
  pip install Flask
  pip install requests
  pip install folium
  pip install MarkupSafe
  ```

  ## 🚀 Como Executar
  1. Clone este repositório para a sua máquina local:
     ```bash
     git clone https://github.com/seu-usuario/previsao-do-tempo.git
     ```
  2. Navegue até o diretório do projeto:
     ```bash
     cd previsao-do-tempo
     ```
  3. Instale as dependências necessárias:
     ```bash
     pip install -r requirements.txt
     ```
  4. Substitua a variável (API_KEY) no arquivo (main.py) com sua chave da API OpenWeatherMap.
  5. Execute o arquivo main.py.
  6. Abra seu navegador e acesse http://127.0.0.1:5000.

  ## 🌐 API Utilizada
  Este projeto utiliza a OpenWeatherMap API para buscar os dados meteorológicos. Para utilizá-la,
  é necessário se registrar e obter uma chave de API.

  ## 📝 Exemplo de Uso
  1. Acesse a página inicial do aplicativo e insira o nome de uma cidade.
  2. Clique em "Ver Clima".
  3. Veja as informações climáticas e o mapa interativo.
  4. Se a cidade não for encontrada, uma mensagem de erro será exibida.

  ## 🔧 Melhorias Futuras
  - Adicionar suporte para múltiplos idiomas.
  - Incluir gráficos com previsões estendidas.
  - Adicionar suporte para mais cidades em um único mapa.

  ## 📬 Contato
Desenvolvido por [ Lucca de Carvalho, 
