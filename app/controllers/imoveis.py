from app import app, cnx
from flask import request, render_template, session
from werkzeug.utils import redirect
from app.models.imovel_dao import ImovelDAO
from app.models.fotos_dao import FotosDAO
from app.decorators import auth

def convertImage(image_blob, id):
    path = f'app\static\imgs\imoveis\img{id}.jpeg'
    with open (path, 'wb') as file:
        file.write(image_blob)
        file.close()
    return path

@app.route("/imoveis",  methods = ["GET", "POST"])
def imoveis():

    if request.method == 'GET':
        cursor = cnx.connection.cursor()

        apartamentos = ImovelDAO().find_all(cursor)
        apts = []
    
        #falta pegar a descricao e as caracteristicas
        for apt in apartamentos:
            print(apt)
            fotos = FotosDAO().find_by_imovel(cursor, apt[0])
            #print(fotos.codigo)
            foto_path = convertImage(fotos.foto, fotos.codigo)
            foto_path = foto_path[3:]
            apts.append([apt, fotos, foto_path])
            print(foto_path)
            
        return render_template("imoveis.html", apts=apts)