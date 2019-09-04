from flask import Flask 
import folium

app = Flask(__name__)

@app.route('/')
def home():
    map = folium.Map(
        location = [-6.302386, 106.652290],
        zoom_start = 15
    )
    return map._repr_html_()

if __name__ == '__main__' :
    app.run(debug = True)

