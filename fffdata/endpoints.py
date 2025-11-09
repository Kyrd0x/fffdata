"""
Endpoints de l'API FFF
======================

Ce fichier centralise toutes les routes disponibles de l'API FFF.
Chaque endpoint est documenté avec ses paramètres et ce qu'il retourne.

Base URL: https://api-dofa.fff.fr
"""

from typing import Dict, Any


class FFFEndpoints:
    """Classe centralisant tous les endpoints de l'API FFF"""
    
    BASE_URL = "https://api-dofa.fff.fr"
    
    # ==================== MATCHS ====================
    
    @staticmethod
    def match_entities(numero_match: int) -> str:
        """
        Récupère toutes les entités d'un match (équipes, joueurs, arbitres, etc.)
        
        Args:
            numero_match: Numéro unique du match (ex: 28541157)
        
        Returns:
            Endpoint: /api/match_entities/{numero_match}.json
            
        Données retournées:
            - Informations complètes du match
            - Équipes domicile/extérieur
            - Score et résultat
            - Compétition, phase, poule, journée
            - Terrain
            - Arbitres et officiels
            - Date et heure
        """
        return f"/api/match_entities/{numero_match}.json"
    
    @staticmethod
    def match_feuille(numero_match: int) -> str:
        """
        Récupère la feuille de match (composition des équipes, événements)
        
        Args:
            numero_match: Numéro unique du match
            
        Returns:
            Endpoint: /api/match_feuilles/{numero_match}.json
            
        Données retournées:
            - Compositions des équipes
            - Événements du match (buts, cartons, remplacements)
            - Statistiques détaillées
        """
        return f"/api/match_feuilles/{numero_match}.json"
    
    # ==================== CLUBS ====================
    
    @staticmethod
    def club(numero_club: int) -> str:
        """
        Récupère les informations d'un club
        
        Args:
            numero_club: Numéro unique du club (ex: 10000)
        
        Returns:
            Endpoint: /api/clubs/{numero_club}.json
            
        Données retournées:
            - Nom, localisation, couleurs
            - District et département
            - Coordonnées (adresse, téléphone)
            - Logo
            - Terrains
            - Membres
        """
        return f"/api/clubs/{numero_club}.json"
    
    @staticmethod
    def club_equipes(numero_club: int) -> str:
        """
        Récupère toutes les équipes d'un club
        
        Args:
            numero_club: Numéro unique du club
            
        Returns:
            Endpoint: /api/clubs/{numero_club}/equipes.json
            
        Données retournées:
            - Liste de toutes les équipes du club
            - Catégories (Seniors, U19, U17, etc.)
            - Engagements en compétition
        """
        return f"/api/clubs/{numero_club}/equipes.json"
    
    # ==================== COMPÉTITIONS ====================
    
    @staticmethod
    def competition(numero_competition: int) -> str:
        """
        Récupère les informations d'une compétition
        
        Args:
            numero_competition: Numéro unique de la compétition (ex: 423015)
            
        Returns:
            Endpoint: /api/competitions/{numero_competition}.json
            
        Données retournées:
            - Nom et type de compétition
            - Saison
            - Niveau (Fédéral, Ligue, District)
            - Organisation (CDG)
        """
        return f"/api/competitions/{numero_competition}.json"
    
    @staticmethod
    def competition_poules(numero_competition: int, phase: int = 1) -> str:
        """
        Récupère les poules d'une compétition
        
        Args:
            numero_competition: Numéro unique de la compétition
            phase: Numéro de phase (défaut: 1)
            
        Returns:
            Endpoint: /api/competitions/{numero_competition}/phases/{phase}/poules.json
            
        Données retournées:
            - Liste des poules
            - Équipes par poule
        """
        return f"/api/competitions/{numero_competition}/phases/{phase}/poules.json"
    
    @staticmethod
    def competition_classement(numero_competition: int, phase: int = 1, poule: int = 1) -> str:
        """
        Récupère le classement d'une poule
        
        Args:
            numero_competition: Numéro unique de la compétition
            phase: Numéro de phase
            poule: Numéro de poule
            
        Returns:
            Endpoint: /api/competitions/{numero_competition}/phases/{phase}/poules/{poule}/classement.json
            
        Données retournées:
            - Classement complet de la poule
            - Points, victoires, nuls, défaites
            - Buts pour/contre, différence de buts
        """
        return f"/api/competitions/{numero_competition}/phases/{phase}/poules/{poule}/classement.json"
    
    @staticmethod
    def competition_calendrier(numero_competition: int, phase: int = 1, poule: int = 1) -> str:
        """
        Récupère le calendrier d'une poule
        
        Args:
            numero_competition: Numéro unique de la compétition
            phase: Numéro de phase
            poule: Numéro de poule
            
        Returns:
            Endpoint: /api/competitions/{numero_competition}/phases/{phase}/poules/{poule}/calendrier.json
            
        Données retournées:
            - Tous les matchs de la poule
            - Dates, horaires, résultats
            - Journées
        """
        return f"/api/competitions/{numero_competition}/phases/{phase}/poules/{poule}/calendrier.json"
    
    # ==================== ÉQUIPES ====================
    
    @staticmethod
    def equipe(numero_equipe: int) -> str:
        """
        Récupère les informations d'une équipe
        
        Args:
            numero_equipe: Numéro unique de l'équipe
            
        Returns:
            Endpoint: /api/equipes/{numero_equipe}.json
            
        Données retournées:
            - Informations de l'équipe
            - Club
            - Catégorie
            - Engagements
        """
        return f"/api/equipes/{numero_equipe}.json"
    
    @staticmethod
    def equipe_effectif(numero_equipe: int) -> str:
        """
        Récupère l'effectif d'une équipe
        
        Args:
            numero_equipe: Numéro unique de l'équipe
            
        Returns:
            Endpoint: /api/equipes/{numero_equipe}/effectif.json
            
        Données retournées:
            - Liste complète des joueurs
            - Informations joueurs (nom, prénom, poste)
            - Licence
        """
        return f"/api/equipes/{numero_equipe}/effectif.json"
    
    @staticmethod
    def equipe_matchs(numero_equipe: int) -> str:
        """
        Récupère tous les matchs d'une équipe
        
        Args:
            numero_equipe: Numéro unique de l'équipe
            
        Returns:
            Endpoint: /api/equipes/{numero_equipe}/matchs.json
            
        Données retournées:
            - Historique des matchs
            - Résultats passés et matchs à venir
        """
        return f"/api/equipes/{numero_equipe}/matchs.json"
    
    # ==================== JOUEURS ====================
    
    @staticmethod
    def joueur(numero_licence: int) -> str:
        """
        Récupère les informations d'un joueur
        
        Args:
            numero_licence: Numéro de licence du joueur
            
        Returns:
            Endpoint: /api/joueurs/{numero_licence}.json
            
        Données retournées:
            - Nom, prénom
            - Date de naissance
            - Poste
            - Club et équipe
        """
        return f"/api/joueurs/{numero_licence}.json"
    
    # ==================== ARBITRES ====================
    
    @staticmethod
    def joueur(numero_arbitre: int) -> str:
        """
        Récupère les informations d'un arbitre
        
        Args:
            numero_arbitre: Numéro de licence de l'arbitre
            
        Returns:
            Endpoint: /api/arbitres/{numero_arbitre}.json
            
        Données retournées:
            - Nom, prénom
            - Date de naissance
            - Poste
            - Club et équipe
        """
        return f"/api/arbitres/{numero_arbitre}.json"
    
    # ==================== TERRAINS ====================
    
    @staticmethod
    def terrain(numero_terrain: int) -> str:
        """
        Récupère les informations d'un terrain
        
        Args:
            numero_terrain: Numéro unique du terrain
            
        Returns:
            Endpoint: /api/terrains/{numero_terrain}.json
            
        Données retournées:
            - Nom du terrain
            - Adresse complète
            - Type de surface
            - Coor
        """
        return f"/api/terrains/{numero_terrain}.json"