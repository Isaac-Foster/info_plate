from flask import Flask, request

app = Flask(__name__)

posts = {
    "postagens": [
        
    {
        'titulo':'minha historia', 
        'autor' : 'Amanda dias'
    
    },

    {
        'titulo':'Novo dispositivo', 
        'autor' : 'andre lucas'
    
    },

    {
        'titulo':'Lançamentos do ano', 
        'autor' : 'jeff Beos'
    
    }
]
}

# Rota padrão-get http://localhost:5000

@app.route('/')
def obter_postagens():
    return posts, 200


#Obter postagem por com id - GET http://localhost:5000/postagem/1
@app.route('/postagem/<indice>')
def obter_postagem_por_indice(indice):
    print(indice)
    indice = int(indice)
    return posts["postagens"][indice]



# CRIAR uma nova postagem - post http://localhost:5000/postagem

@app.route('/post', methods=['POST'])
def nova_postagem():
    post = request.get_json()
    posts["postagens"].append(post)

    return {} , 200


app.run(debug=True)