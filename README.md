# fffdata

Client Python pour l'API publique de la FFF.


# Méthode simple
client = FFFClient()
match = client.get_match_entities("3010203")
print(match)
client.close()

# Ou avec context manager (recommandé)
with FFFClient() as client:
    match = client.get_match_entities("3010203")
    print(match)



from fffdata import FFFClient

with FFFClient() as client:
    # Match avec données structurées
    match = client.get_match_entities(28541157)
    if match:
        print(f"{match.home.short_name} {match.home_score} - {match.away_score} {match.away.short_name}")
        print(f"Compétition: {match.competition.name}")
        print(f"Terrain: {match.terrain.name}")
        print(f"Arbitre: {match.get_arbitre_principal().full_name}")
    
    # Club avec données structurées
    club = client.get_club(10000)
    if club:
        print(f"{club.name} - {club.location}")
        print(f"Téléphones: {', '.join(club.get_phone_numbers())}")
        print(f"District: {club.district.name}")