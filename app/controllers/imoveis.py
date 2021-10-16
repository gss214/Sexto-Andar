from app import app, cnx
from flask import request, render_template, session
from werkzeug.utils import redirect
from app.models.imovel_dao import ImovelDAO
from app.models.fotos_dao import FotosDAO, Fotos
from app.models.caracteristicas_dao import CaracteristicasDAO
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
        # arrumar depois
        tipo_imovel = request.form.getlist('tipoImovel')[0]
        cursor.callproc('selectImoveisPorTipo', [tipo_imovel])
        result = cursor.fetchall()
        back = True

    for imovel in result:
        fotos = FotosDAO().find_by_imovel(cursor, imovel[0])
        fotos = Fotos(fotos[0][0], fotos[0][1], fotos[0][2], fotos[0][3], fotos[0][4])
        caracteristicas = CaracteristicasDAO().find_by_id(cursor, imovel[0])
        foto_path = convertImage(fotos.foto, fotos.codigo)
        foto_path = foto_path[3:]
        imoveis.append([imovel, fotos, foto_path, caracteristicas])

    #print(imoveis)
        
    return render_template("imoveis.html", imoveis=imoveis, back=back)

@app.route("/view",  methods = ["GET", "POST"])
def view():
    codigo = request.args.get('imovel', None)
    #print(codigo)

    # arrumar dps
    cursor = cnx.connection.cursor()
    sql = f"SELECT * FROM anuncio WHERE codigo = '{codigo}'"
    cursor.execute(sql)
    anuncio = cursor.fetchone()

    fotos = FotosDAO().find_by_imovel(cursor, anuncio[0])
    imagens = []
    for foto in fotos:
        foto_path = convertImage(foto[2], foto[0])
        foto_path = foto_path[3:]
        imagens.append([foto, foto_path])


    print(anuncio)

    return render_template("view.html", fotos=imagens, anuncio=anuncio)