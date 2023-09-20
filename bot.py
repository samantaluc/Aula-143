import os
from flask import Flask, request, jsonify, render_template
from googleapiclient.discovery import build

app = Flask(__name__)

# Configuração da chave de API do YouTube
DEVELOPER_KEY = 'AIzaSyDUltHC8dm851E4sEmIif8Cgrzvcwm80Fc'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/buscar', methods=['POST'])
def buscar_musicas():
    data = request.get_json()
    tag = data['tag']

    # Realiza a pesquisa no YouTube com base na tag
    search_response = youtube.search().list(
        q=tag,
        type='video',
        maxResults=5
    ).execute()

    # Extrai os resultados da pesquisa
    resultados = []
    for search_result in search_response.get('items', []):
        video_id = search_result['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        video_title = search_result['snippet']['title']
        resultados.append(f'<a href="{video_url}" target="_blank">{video_title}</a>')

    return jsonify({'resultado': '<br>'.join(resultados)})
    @app.route('/')
def index():
    return render_template('histórico.html')

@app.route('/buscar', methods=['POST'])
def buscar_musicas():
    tag = request.form.get('tag')

    # Realiza a pesquisa no YouTube com base na tag
    search_response = youtube.search().list(
        q=tag,
        type='video',
        maxResults=5
    ).execute()

    # Extrai os resultados da pesquisa
    resultados = []
    for search_result in search_response.get('items', []):
        video_id = search_result['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        video_title = search_result['snippet']['title']
        resultados.append(f'<a href="{video_url}" target="_blank">{video_title}</a>')

    return render_template('histórico.html', resultados=resultados)

@app.route('/')
def index():
    return render_template('histórico.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        usuario = request.form['usuario']
        email = request.form['email']
        senha = request.form['senha']
        
        # Aqui você pode processar os dados do formulário (por exemplo, salvar em um banco de dados)
        
        return "Cadastro realizado com sucesso!"

    return render_template('cadastro.html')


if __name__ == '__main__':
    app.run(debug=True)
