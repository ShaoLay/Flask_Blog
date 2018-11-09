from app import app



app.config['SECRET_KEY'] = '12345678'
app.run(debug = True)