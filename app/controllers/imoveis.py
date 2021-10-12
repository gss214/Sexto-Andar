from app import app, cnx
from flask import request, render_template, session
from werkzeug.utils import redirect
from app.models.imovel_dao import ImovelDAO
from app.models.fotos_dao import FotosDAO
from app.decorators import auth


@app.route("/imoveis",  methods = ["GET", "POST"])
def imoveis():

    if request.method == 'GET':
        cursor = cnx.connection.cursor()

        apartamentos = ImovelDAO().find_all(cursor)
        apts = []
    
        #falta pegar a descricao e as caracteristicas
        for apt in apartamentos:
            fotos = FotosDAO().find_by_imovel(cursor, apt[0])
            apts.append([apt, fotos])

        return render_template("imoveis.html", apts=apts)