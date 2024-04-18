from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

#@app.route('/')
#def inicio():
#    return render_template('inicio.html')

@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
      # Obtener la respuesta del formulario
      respuesta = request.form['respuesta']
      # Procesar la respuesta
      if respuesta == 'SI':
          # Si la respuesta es correcta, redirigir a la siguiente pregunta
          return redirect(url_for('primera_pregunta'))
      else:
          # Si no se desea iniciar partida
          return redirect(url_for('fin'))
    # Renderizar la plantilla de la primera pregunta
    response = make_response(render_template('inicio.html'))
    # Configurar las cabeceras para evitar que el navegador almacene en caché la página
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
  
# PREGUNTA 1
@app.route('/pregunta1', methods=['GET', 'POST'])  
def primera_pregunta():
    if request.method == 'POST':
        # Obtener la respuesta del formulario
        respuesta = request.form['respuesta']
        # Procesar la respuesta
        if respuesta == 'c':
            # Si la respuesta es correcta, redirigir a la siguiente pregunta
            return redirect(url_for('segunda_pregunta'))
        else:
            # Si la respuesta es incorrecta, redirigir a la página de respuesta incorrecta
            return redirect(url_for('respuesta_incorrecta_1'))
    # Renderizar la plantilla de la primera pregunta
    response = make_response(render_template('pregunta1.html'))
    # Configurar las cabeceras para evitar que el navegador almacene en caché la página
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

# PREGUNTA 2
@app.route('/pregunta2', methods=['GET', 'POST'])  
def segunda_pregunta():
  if request.method == 'POST':
      # Obtener la respuesta del formulario
      respuesta = request.form['respuesta']
      # Procesar la respuesta
      if respuesta == 'b':
          # Si la respuesta es correcta, redirigir a la siguiente pregunta
          return redirect(url_for('tercera_pregunta'))
      else:
          # Si la respuesta es incorrecta, redirigir a la página de respuesta incorrecta
          return redirect(url_for('respuesta_incorrecta_2'))
  # Renderizar la plantilla de la segunda pregunta
  response = make_response(render_template('pregunta2.html'))
  # Configurar las cabeceras para evitar que el navegador almacene en caché la página
  response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
  response.headers['Pragma'] = 'no-cache'
  response.headers['Expires'] = '0'
  return response

# PREGUNTA 3
@app.route('/pregunta3', methods=['GET', 'POST'])  
def tercera_pregunta():
  if request.method == 'POST':
      # Obtener la respuesta del formulario
      respuesta = request.form['respuesta']
      # Procesar la respuesta
      if respuesta == 'a':
          # Si la respuesta es correcta, redirigir a la siguiente pregunta
          return redirect(url_for('cuarta_pregunta'))
      else:
          # Si la respuesta es incorrecta, redirigir a la página de respuesta incorrecta
          return redirect(url_for('respuesta_incorrecta_3'))
  # Renderizar la plantilla de la tercera pregunta
  response = make_response(render_template('pregunta3.html'))
  # Configurar las cabeceras para evitar que el navegador almacene en caché la página
  response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
  response.headers['Pragma'] = 'no-cache'
  response.headers['Expires'] = '0'
  return response

# PREGUNTA 4
@app.route('/pregunta4', methods=['GET', 'POST'])  
def cuarta_pregunta():
  if request.method == 'POST':
      # Obtener la respuesta del formulario
      respuesta = request.form['respuesta']
      # Procesar la respuesta
      if respuesta == 'b':
          # Si la respuesta es correcta, redirigir a la siguiente pregunta
          return redirect(url_for('quinta_pregunta'))
      else:
          # Si la respuesta es incorrecta, redirigir a la página de respuesta incorrecta
          return redirect(url_for('respuesta_incorrecta_4'))
  # Renderizar la plantilla de la cuarta pregunta 
  response = make_response(render_template('pregunta4.html'))
  # Configurar las cabeceras para evitar que el navegador almacene en caché la página
  response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
  response.headers['Pragma'] = 'no-cache'
  response.headers['Expires'] = '0'
  return response

# PREGUNTA 5
@app.route('/pregunta5', methods=['GET', 'POST'])  
def quinta_pregunta():
  if request.method == 'POST':
      # Obtener la respuesta del formulario
      respuesta = request.form['respuesta']
      # Procesar la respuesta
      if respuesta == 'a':
          # Si la respuesta es correcta, redirigir a la siguiente pregunta
          return redirect(url_for('sexta_pregunta'))
      else:
          # Si la respuesta es incorrecta, redirigir a la página de respuesta incorrecta
          return redirect(url_for('respuesta_incorrecta_5'))
  # Renderizar la plantilla de la quinta pregunta 
  response = make_response(render_template('pregunta5.html'))
  # Configurar las cabeceras para evitar que el navegador almacene en caché la página
  response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
  response.headers['Pragma'] = 'no-cache'
  response.headers['Expires'] = '0'
  return response
  
# PREGUNTA 6
@app.route('/pregunta6', methods=['GET', 'POST'])  
def sexta_pregunta():
  if request.method == 'POST':
      # Obtener la respuesta del formulario
      respuesta = request.form['respuesta']
      # Procesar la respuesta
      if respuesta == 'a':
          # Si la respuesta es correcta, redirigir a la siguiente pregunta
          return redirect(url_for('septima_pregunta'))
      else:
          # Si la respuesta es incorrecta, redirigir a la página de respuesta incorrecta
          return redirect(url_for('respuesta_incorrecta_6'))
  # Renderizar la plantilla de la sexta pregunta 
  response = make_response(render_template('pregunta6.html'))
  # Configurar las cabeceras para evitar que el navegador almacene en caché la página
  response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
  response.headers['Pragma'] = 'no-cache'
  response.headers['Expires'] = '0'
  return response

# PREGUNTA 7
@app.route('/pregunta7', methods=['GET', 'POST'])  
def septima_pregunta():
  if request.method == 'POST':
      # Obtener la respuesta del formulario
      respuesta = request.form['respuesta']
      # Procesar la respuesta
      if respuesta == 'a':
          # Si la respuesta es correcta, redirigir a la siguiente pregunta
          return redirect(url_for('youwin'))
      else:
          # Si la respuesta es incorrecta, redirigir a la página de respuesta incorrecta
          return redirect(url_for('respuesta_incorrecta_7'))
  # Renderizar la plantilla de la septima pregunta 
  response = make_response(render_template('pregunta7.html'))
  # Configurar las cabeceras para evitar que el navegador almacene en caché la página
  response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
  response.headers['Pragma'] = 'no-cache'
  response.headers['Expires'] = '0'
  return response

# Fin Ganador
@app.route('/youwin')
def youwin():
  return render_template('fin_ganador.html')


# Respuesta incorrecta 1
@app.route('/respuesta_incorrecta', methods=['GET', 'POST'])
def respuesta_incorrecta_1():
  if request.method == 'POST':
    # Obtener la respuesta del formulario
    respuesta = request.form['respuesta']
    # Procesar la respuesta
    if respuesta == 'SI':
      return redirect(url_for('inicio'))
    else:
      return redirect(url_for('fin'))
  return render_template('incorrecto_1.html')

# Respuesta incorrecta 2
@app.route('/respuesta_incorrecta_2', methods=['GET', 'POST'])
def respuesta_incorrecta_2():
  if request.method == 'POST':
    # Obtener la respuesta del formulario
    respuesta = request.form['respuesta']
    # Procesar la respuesta
    if respuesta == 'SI':
      return redirect(url_for('inicio'))
    else:
      return redirect(url_for('fin'))
  return render_template('incorrecto_2.html')

# Respuesta incorrecta 3
@app.route('/respuesta_incorrecta_3', methods=['GET', 'POST'])
def respuesta_incorrecta_3():
  if request.method == 'POST':
    # Obtener la respuesta del formulario
    respuesta = request.form['respuesta']
    # Procesar la respuesta
    if respuesta == 'SI':
      return redirect(url_for('inicio'))
    else:
      return redirect(url_for('fin'))
  return render_template('incorrecto_3.html')

# Respuesta incorrecta 4
@app.route('/respuesta_incorrecta_4', methods=['GET', 'POST'])
def respuesta_incorrecta_4():
  if request.method == 'POST':
    # Obtener la respuesta del formulario
    respuesta = request.form['respuesta']
    # Procesar la respuesta
    if respuesta == 'SI':
      return redirect(url_for('inicio'))
    else:
      return redirect(url_for('fin'))
  return render_template('incorrecto_4.html')

# Respuesta incorrecta 5
@app.route('/respuesta_incorrecta_5', methods=['GET', 'POST'])
def respuesta_incorrecta_5():
  if request.method == 'POST':
    # Obtener la respuesta del formulario
    respuesta = request.form['respuesta']
    # Procesar la respuesta
    if respuesta == 'SI':
      return redirect(url_for('inicio'))
    else:
      return redirect(url_for('fin'))
  return render_template('incorrecto_5.html')

# Respuesta incorrecta 6
@app.route('/respuesta_incorrecta_6', methods=['GET', 'POST'])
def respuesta_incorrecta_6():
  if request.method == 'POST':
    # Obtener la respuesta del formulario
    respuesta = request.form['respuesta']
    # Procesar la respuesta
    if respuesta == 'SI':
      return redirect(url_for('inicio'))
    else:
      return redirect(url_for('fin'))
  return render_template('incorrecto_6.html')

# Respuesta incorrecta 7
@app.route('/respuesta_incorrecta_7', methods=['GET', 'POST'])
def respuesta_incorrecta_7():
  if request.method == 'POST':
    # Obtener la respuesta del formulario
    respuesta = request.form['respuesta']
    # Procesar la respuesta
    if respuesta == 'SI':
      return redirect(url_for('inicio'))
    else:
      return redirect(url_for('fin'))
  return render_template('incorrecto_7.html')

@app.route('/fin', methods=['GET', 'POST'])
def fin():
    return render_template('fin.html')

#if __name__ == '__main__':
#    app.run(debug=True)
