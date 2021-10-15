from app import app, cnx
from flask import request, render_template, session
from werkzeug.utils import redirect
from app.models.imovel_dao import ImovelDAO
from app.models.fotos_dao import FotosDAO
from app.models.caracteristicas_dao import Caracteristicas, CaracteristicasDAO
from app.decorators import auth

def convertImage(image_blob, id):
    path = f'app\static\imgs\imoveis\img{id}.jpeg'
    with open (path, 'wb') as file:
        file.write(image_blob)
        file.close()
    return path

@app.route("/imoveis",  methods = ["GET", "POST"])
def imoveis():

    imoveis = []
    cursor = cnx.connection.cursor()
    
    if request.method == 'GET':
        result = ImovelDAO().find_all(cursor)
        back = False
    
    else:
        tipo_imovel = request.form.getlist('tipoImovel')[0]
        cursor.callproc('selectImoveisPorTipo', [tipo_imovel])
        result = cursor.fetchall()
        back = True

    for imovel in result:
        #print(imovel)
        fotos = FotosDAO().find_by_imovel(cursor, imovel[0])
        caracteristicas = CaracteristicasDAO().find_by_id(cursor, imovel[0])
        #print(fotos.codigo)
        foto_path = convertImage(fotos.foto, fotos.codigo)
        foto_path = foto_path[3:]
        #print(caracteristicas)
        imoveis.append([imovel, fotos, foto_path, caracteristicas])
        #print(foto_path)

    #print(result)
        
    return render_template("imoveis.html", imoveis=imoveis, back=back)