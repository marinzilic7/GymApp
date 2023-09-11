from __init__ import session
from clan import Clan
from trener import Trener
from trening import Trening
from clanarina import Clanarina


import os 
from flask import Flask,render_template, request,redirect, url_for,flash



app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))
app.secret_key = 'ovo-je-moj-tajni-kljuc'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def index ():
    clan = session.query(Clan).all()
    trener = session.query(Trener).all()
    trening = session.query(Trening).all()
    clanarina = session.query(Clanarina).all()

    return render_template('gym.html', clanovi=clan, treneri=trener, treninzi=trening, clanarine=clanarina)


@app.route("/clan")
def clan ():
    clan = session.query(Clan).all()

    return render_template('clan.html', clan=clan)

@app.route('/dodaj-clana', methods=['POST'])
def dodaj_clana():
    ime = request.form.get('ime')
    prezime = request.form.get('prezime')
    kontakt = request.form.get('kontakt')
    novi_clan = Clan(ime=ime, prezime=prezime, kontakt=kontakt)
    session.add(novi_clan)
    session.commit()

    return redirect(url_for('clan'))


@app.route('/izbrisi_clana/<int:ID_clana>', methods=['POST'])
def izbrisi_clana(ID_clana):
    clan = session.query(Clan).get(ID_clana)
    
    if clan:
        
        session.delete(clan)
        session.commit()  
        flash('Clan je uspjesno izbrisan.', 'success')

    return redirect(url_for('clan'))




@app.route("/trener")
def trener ():
    trener = session.query(Trener).all()

    return render_template('trener.html', treneri=trener)


@app.route('/dodaj-trenera', methods=['POST'])
def dodaj_clanarinu():
    ime = request.form.get('ime')
    prezime = request.form.get('prezime')
    kontakt = request.form.get('kontakt')
    novi_trener = Trener(ime=ime, prezime=prezime, kontakt=kontakt)
    session.add(novi_trener)
    session.commit()

    return redirect(url_for('trener'))



@app.route('/izbrisi_trenera/<int:ID_trenera>', methods=['POST'])
def izbrisi_trenera(ID_trenera):
    trener = session.query(Trener).get(ID_trenera)
    
    if trener:
        
        session.delete(trener)
        session.commit()  
        flash('Trener je uspjesno izbrisan.', 'success')

    return redirect(url_for('trener'))


@app.route("/trening")
def trening ():
    trening = session.query(Trening).all()

    return render_template('trening.html', treninzi=trening)


@app.route('/dodaj-trening', methods=['POST'])
def dodaj_trening():
    ime = request.form.get('ime')
    vrsta = request.form.get('vrsta')
   
    novi_trening = Trening(ime=ime, vrsta=vrsta )
    session.add(novi_trening)
    session.commit()

    return redirect(url_for('trening'))



@app.route('/izbrisi_trening/<int:ID_trening>', methods=['POST'])
def izbrisi_trening(ID_trening):
    trening = session.query(Trening).get(ID_trening)
    
    if trening:
        
        session.delete(trening)
        session.commit()  
        flash('Trening je uspjesno izbrisan.', 'success')

    return redirect(url_for('trening'))

@app.route('/dodaj-clanarinu', methods=['POST'])
def dodajclanarinu():
    ID_clana  = request.form.get('ID_clana')
    ID_trenera = request.form.get('ID_trenera')
    ID_trening = request.form.get('ID_trening')
    trajanje = request.form.get('trajanje')
    clanarina = Clanarina(ID_clana=ID_clana, ID_trenera=ID_trenera, ID_trening=ID_trening, trajanje=trajanje)
    session.add(clanarina)
    session.commit()

    return redirect(url_for('index'))




@app.route('/izbrisi_clanarinu/<int:ID_Clanarina>', methods=['POST'])
def izbrisi_clanarinu(ID_Clanarina):
    clanarina = session.query(Clanarina).get(ID_Clanarina)
    
    if clanarina:
        
        session.delete(clanarina)
        session.commit()  
        flash('Clanarina uspjesno izbrisana', 'success')

    return redirect(url_for('index'))


@app.route('/uredi_clanarinu/<int:ID_Clanarina>')
def uredi_clanarinu(ID_Clanarina):
    clanarina = session.query(Clanarina).get(ID_Clanarina)
    clan = session.query(Clan).all()
    trener = session.query(Trener).all()
    trening = session.query(Trening).all()
    return render_template('uredi_clanarinu.html', clanarina=clanarina, clanovi=clan,treneri=trener,treninzi=trening)


@app.route('/update_clanarinu/<int:ID_Clanarina>', methods=['POST'])
def update_clanarinu(ID_Clanarina):
    clanarina = session.query(Clanarina).get(ID_Clanarina)
    if clanarina:
        
     
        clanarina.ID_trenera = request.form.get('ID_trenera')
        clanarina.ID_trening = request.form.get('ID_trening')
       
        clanarina.trajanje = request.form.get('trajanje')
        
       
        session.commit()
        
    
       

    return redirect(url_for('index'))


if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000)