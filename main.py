from flask import Flask
import random

app = Flask(__name__)

tech_fact = [
    'Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka', 
    'MeJejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini',
    'Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja', 
    'Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten',
    'Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan'
    ]

random_coin = [
    'Gambar',
    'Angka'
]

@app.route("/")
def hello_world():
    return '<h1>Hello, World! <a href="/tech_fact">View interesting facts</a></h1><h1><a href="/lempar_coin">lempar coin</a></h1>'

@app.route("/tech_fact")
def techfact():
    return f'<p>{random.choice(tech_fact)}</p><h1>Naufal Ganteng:)<h1>'

@app.route("/lempar_coin")
def Ga():
    return f'<p>Koin mu Saat Ini = {random.choice(random_coin)}</p><h1>Naufal Ganteng:)<h1>'

app.run(debug=True)
