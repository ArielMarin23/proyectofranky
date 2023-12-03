from flask import Flask, render_template, jsonify, request, redirect, url_for
from referenciales.ciudad.ciudadDao import CiudadDao

app = Flask(__name__)

@app.context_processor
def inject_active_page():
    return dict(active_page=request.endpoint)
@app.route('/')
def index():
    return  render_template('base.html')

@app.route('/index-persona')
def index_persona():
    return render_template('vistas_personas/index-persona.html')
#Operadores rest[GET, POST, PUT, PATCH, DELETE]
@app.route('/save-persona', methods=['POST'])
def save_persona():
    print(request.json['nombres'])
    return jsonify({
        'mensaje': 'Se recibio correctamente el json del navegador',
        'objeto_recibo': request.json
    })

@app.route('/index-ciudad')
def index_ciudad():
    cdao = CiudadDao()
    lista = cdao.getCiudades()
    diccionario = []
    if len(lista) > 0:
        for item in lista:
            diccionario.append(
                {
                    'id': item[0],
                    'descripcion': item[1]
                }
            )
    return render_template('vistas_ciudades/index-ciudades.html', ciudades=diccionario,)
#Ruta Agregar Ciudad
@app.route('/agregar-ciudad')
def agregar_ciudad():
    return render_template('vistas_ciudades/index-ciudades.html')


@app.route('/saved-ciudad', methods=['POST'])
def save_ciudad():
    cdao = CiudadDao()
    txtciudad = request.form['txtciudad']
    isSaved = False
    if txtciudad != None and len(txtciudad.strip()) > 0:
        isSaved = cdao.insertCiudad(txtciudad.strip().upper())
    if isSaved:
        return redirect(url_for('index_ciudad'))
    else: 
        return redirect(url_for('agregar_ciudad'))

#Ruta Editar
@app.route('/editar-ciudad/<id>')
def editar_ciudad(id):
    cdao = CiudadDao()
    ciudadFound = cdao.getCiudadById(id)
    if ciudadFound:
        return render_template('vistas_ciudades/editar-ciudad.html', ciudad=ciudadFound)
    return redirect(url_for('index_ciudad'))
#Vista de actualizacion.

@app.route('/update-ciudad', methods=['POST'])
def update_ciudad():
    cdao = CiudadDao()
    idtxtciudad = request.form['idtxtciudad']
    txtciudad = request.form['txtciudad']
    isUpdate = False
    if idtxtciudad == None or len(idtxtciudad.strip())==0:
        return redirect(url_for('index_ciudad'))
    
    if txtciudad != None and len(txtciudad.strip()) > 0:
        isUpdate = cdao.updateCiudad(idtxtciudad.strip(), txtciudad.strip().upper())
    if isUpdate:
        return redirect(url_for('index_ciudad'))
    else:
        return redirect(url_for('editar_ciudad', id=idtxtciudad))    
#Vista eliminar
@app.route('/delete-ciudad/<id>')
def delete_ciudad(id):
    cdao = CiudadDao()
    cdao.deleteCiudad(id)
    return redirect(url_for('index_ciudad'))
#Facturacion editando sin terminar
@app.route('/facturacion')
def facturacion():
    return render_template('facturacion.html')

@app.route('/get-ciudad')
def getCiudad():
    cdao = CiudadDao()
    lista = cdao.getCiudades()
    diccionario = []
    if len(lista) > 0:
        for item in lista:
            diccionario.append(
                {
                    'id': item[0],
                    'descripcion': item[1]
                }
            )
        return jsonify(diccionario)
    else:
        return 'no hay ciudades'
    


if __name__ == '__main__':
    app.run(debug=True)