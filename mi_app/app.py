from flask import Flask, render_template, request, redirect, url_for

# Crear instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para la página de inicio de sesión
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Capturar datos del formulario
        username = request.form['username']
        password = request.form['password']
        
        # Validación básica (puedes agregar validaciones más complejas)
        if username == 'admin' and password == 'password':
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Usuario o contraseña incorrectos')

    return render_template('login.html')

# Ruta para el dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=8000)




