"""Exemples d'utilisation de la bibliothèque fffdata"""

from fffdata import FFFClient, FFFAPIError


def exemple_basique():
    """Exemple basique d'utilisation"""
    print("=== Exemple basique ===\n")
    
    # Créer un client
    client = FFFClient()
    
    try:
        # Récupérer les données d'un match
        numero_match = 28541157  # Entier
        print(f"Récupération du match {numero_match}...")
        
        match = client.get_match_entities(numero_match)
        
        if match:
            print(f"✓ Match récupéré avec succès!")
            print(f"Match: {match.get_match_label()}")
            print(f"Score: {match.get_score()}")
            print(f"Compétition: {match.competition.name}")
        else:
            print(f"✗ Match {numero_match} non trouvé")
    
    except FFFAPIError as e:
        print(f"✗ Erreur API: {e}")
    
    finally:
        client.close()


def exemple_club():
    """Exemple de récupération d'un club"""
    print("\n=== Exemple récupération d'un club ===\n")
    
    with FFFClient() as client:
        try:
            numero_club = 10000  # Entier
            print(f"Récupération du club {numero_club}...")
            
            club = client.get_club(numero_club)
            
            if club:
                print(f"✓ Club récupéré avec succès!")
                print(f"Nom: {club.name}")
                print(f"Localisation: {club.location}")
                
                # Afficher quelques infos si disponibles
                if club.district:
                    print(f"District: {club.district.name}")
                
                phones = club.get_phone_numbers()
                if phones:
                    print(f"Téléphones: {', '.join(phones)}")
            else:
                print(f"✗ Club {numero_club} non trouvé")
                
        except FFFAPIError as e:
            print(f"✗ Erreur: {e}")


def exemple_context_manager():
    """Exemple avec context manager (recommandé)"""
    print("\n=== Exemple avec context manager ===\n")
    
    # Utilisation du context manager pour fermeture automatique
    with FFFClient() as client:
        try:
            numero_match = 28541157
            match = client.get_match_entities(numero_match)
            
            if match:
                print(f"✓ Match {numero_match} récupéré")
                print(f"{match.home.short_name} vs {match.away.short_name}")
                print(f"Date: {match.date} à {match.time}")
                
                if match.terrain:
                    print(f"Terrain: {match.terrain.name}")
                
                if match.is_finished():
                    print(f"Score final: {match.get_score()}")
            else:
                print(f"✗ Match {numero_match} non trouvé")
                
        except FFFAPIError as e:
            print(f"✗ Erreur: {e}")


def exemple_gestion_erreurs():
    """Exemple complet de gestion des erreurs"""
    print("\n=== Exemple de gestion des erreurs ===\n")
    
    with FFFClient() as client:
        # Test avec différents numéros
        numeros_match = [28541157, 999999]
        numeros_club = [10000, 99999]
        
        print("--- Tests matchs ---")
        for numero in numeros_match:
            try:
                print(f"Tentative pour le match {numero}...")
                match = client.get_match_entities(numero)
                
                if match:
                    print(f"  ✓ Succès: {match.get_match_label()}\n")
                else:
                    print(f"  ✗ Match {numero} introuvable (None retourné)\n")
                
            except FFFAPIError as e:
                print(f"  ✗ Erreur: {e}\n")
        
        print("--- Tests clubs ---")
        for numero in numeros_club:
            try:
                print(f"Tentative pour le club {numero}...")
                club = client.get_club(numero)
                
                if club:
                    print(f"  ✓ Succès: {club.name}\n")
                else:
                    print(f"  ✗ Club {numero} introuvable (None retourné)\n")
                
            except FFFAPIError as e:
                print(f"  ✗ Erreur: {e}\n")


def exemple_multiple_requetes():
    """Exemple avec plusieurs requêtes qui ne bloquent pas l'exécution"""
    print("\n=== Exemple de requêtes multiples ===\n")
    
    with FFFClient() as client:
        numeros = [28541157, 999999, 28541158, 888888]
        
        resultats = []
        for numero in numeros:
            try:
                match = client.get_match_entities(numero)
                if match:
                    resultats.append((numero, "trouvé"))
                    print(f"✓ Match {numero} trouvé: {match.get_match_label()}")
                else:
                    resultats.append((numero, "non trouvé"))
                    print(f"✗ Match {numero} non trouvé")
            except FFFAPIError as e:
                resultats.append((numero, f"erreur: {e}"))
                print(f"✗ Erreur pour {numero}: {e}")
        
        print(f"\n--- Résumé ---")
        print(f"Total requêtes: {len(numeros)}")
        print(f"Trouvés: {sum(1 for _, r in resultats if r == 'trouvé')}")
        print(f"Non trouvés: {sum(1 for _, r in resultats if r == 'non trouvé')}")


def exemple_details_match():
    """Exemple d'accès aux détails d'un match"""
    print("\n=== Détails complets d'un match ===\n")
    
    with FFFClient() as client:
        match = client.get_match_entities(28541157)
        
        if match:
            print(f"🏆 {match.competition.name} - Saison {match.season}")
            print(f"📅 {match.date} à {match.time}")
            print(f"🏟️  {match.terrain.name if match.terrain else 'Terrain non défini'}")
            print()
            print(f"🏠 {match.home.short_name} (Score: {match.home_score})")
            print(f"✈️  {match.away.short_name} (Score: {match.away_score})")
            print()
            
            arbitre = match.get_arbitre_principal()
            if arbitre:
                print(f"👨‍⚖️ Arbitre: {arbitre.full_name}")


if __name__ == "__main__":
    # Exécuter tous les exemples
    exemple_basique()
    exemple_club()
    exemple_context_manager()
    exemple_gestion_erreurs()
    exemple_multiple_requetes()
    exemple_details_match()