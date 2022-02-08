''' Web page main Flask framework module '''
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')



@app.route("/")
@app.route("/home")
def home():
    def get_now(path):
        jsondata = ''
        with open(path, 'r') as jsonfile:
            for i in jsonfile:
                jsondata += i
        dict_json = json.loads(jsondata)
        return dict_json

    data = get_now('data/now_home.json')
    data1 = get_now('data/now_out.json')
    return render_template('home.html', data=data, data1=data1)

@app.route("/temperature")
@app.route("/temperatura")
def temperatura():
    return render_template('wykres_temperatury.html')

@app.route("/humidity")
@app.route("/wilgotnosc")
def wilgotnosc():
    return render_template('wykres_wilgotnosci.html')

@app.route("/pressure")
@app.route("/cisnienie")
def cisnienie():
    return render_template('wykres_cisnienia.html')


@app.route("/pm25")
def pm25():
    return render_template('wykres_pm25.html')


@app.route("/pm10")
def pm10():
    return render_template('wykres_pm10.html')



if __name__ == '__main__':
    
    app.run(debug=True,  host="localhost")