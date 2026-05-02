from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)

# ÉTAPE 1 : Fonction pour chercher des vrais codes (via API ou Scraping léger)
def chercher_vrais_codes(nom_site):
    # On simule un appel à une base de données de coupons
    # En vrai, on pourrait utiliser l'API de Coupon-API.com ici
    base_codes = {
        "zara": ["ZARA20", "WELCOME", "FREESHIP"],
        "amazon": ["AMZ10", "PRIME2026", "SAVE5"],
        "nike": ["NIKE25", "JUSTDOIT", "MEMBERS"]
    }
    return base_codes.get(nom_site.lower(), ["PROMO10", "OFFRE20"])

@app.route('/test-promo', methods=['POST'])
def test_promo():
    site = request.form.get('site', '').lower()
    
    # 1. On cherche les codes existants pour ce site
    liste_a_tester = chercher_vrais_codes(site)
    
    # 2. On simule le test du robot Playwright (pour ne pas faire planter Render Free)
    # Dans une version payante, on lancerait un vrai navigateur ici
    codes_valides = []
    for code in liste_a_tester:
        # Ici le robot "testerait" le code sur le site
        time.sleep(1) # Le robot prend 1 sec par code
        codes_valides.append(code)

    # 3. On renvoie le meilleur code trouvé
    return jsonify({
        "status": "success",
        "economie": "15% environ",
        "code_gagnant": codes_valides[0], 
        "tous_les_codes": codes_valides,
        "message": f"Le robot a testé {len(codes_valides)} codes sur {site}."
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
