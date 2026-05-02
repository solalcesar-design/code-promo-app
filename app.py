from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app) # Permet au HTML de parler au Python

@app.route('/test-promo', methods=['POST'])
def test_promo():
    # On récupère les infos envoyées par l'iPad
    site = request.form.get('site')
    file = request.files.get('file')
    
    # Simulation du travail de l'IA (Gemma)
    # Ici, tu pourras plus tard ajouter ton code Playwright
    time.sleep(5) # On simule 5 secondes de recherche
    
    resultat = {
        "status": "success",
        "economie": "12.50€",
        "code_gagnant": "MAMAN2024",
        "message": f"Super ! On a trouvé un code pour {site}."
    }
    
    return jsonify(resultat)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
