from flask import Flask, render_template, request, redirect, url_for

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
    return render_template('inicio.html')
  
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
            return redirect(url_for('respuesta_incorrecta'))
    # Renderizar la plantilla de la primera pregunta
    return render_template('pregunta1.html')

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
          return redirect(url_for('respuesta_incorrecta'))
  # Renderizar la plantilla de la segunda pregunta
  return render_template('pregunta2.html')

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
          return redirect(url_for('respuesta_incorrecta'))
  # Renderizar la plantilla de la primera pregunta
  return render_template('pregunta3.html')

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
          return redirect(url_for('respuesta_incorrecta'))
  # Renderizar la plantilla de la primera pregunta
  return render_template('pregunta4.html')

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
          return redirect(url_for('respuesta_incorrecta'))
  # Renderizar la plantilla de la primera pregunta
  return render_template('pregunta5.html')
  
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
          return redirect(url_for('respuesta_incorrecta'))
  # Renderizar la plantilla de la primera pregunta
  return render_template('pregunta6.html')

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
          return redirect(url_for('respuesta_incorrecta'))
  # Renderizar la plantilla de la primera pregunta
  return render_template('pregunta7.html')

# Fin Ganador
@app.route('/youwin')
def youwin():
  return render_template('fin_ganador.html')


# Respuesta incorrecta
@app.route('/respuesta_incorrecta')
def respuesta_incorrecta():
    return render_template('incorrecto_1.html')

@app.route('/fin', methods=['GET', 'POST'])
def fin():
    return render_template('fin.html')

if __name__ == '__main__':
    app.run(debug=True)
