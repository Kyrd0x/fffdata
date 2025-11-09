"""Client principal pour l'API FFF"""

import requests
from typing import Dict, Any, Optional
from .exceptions import (
    FFFAPIError,
    MatchNotFoundError,
    InvalidMatchNumberError,
    APIConnectionError
)
from .models import Club, Match


class FFFClient:
    """Client pour interagir avec l'API FFF
    
    Args:
        base_url: URL de base de l'API (par défaut: https://api-dofa.fff.fr)
        timeout: Timeout en secondes pour les requêtes (par défaut: 30)
    
    Example:
        >>> client = FFFClient()
        >>> match_data = client.get_match_entities("3010203")
        >>> print(match_data['equipe_a'])
    """
    
    def __init__(
        self, 
        base_url: str = "https://api-dofa.fff.fr",
        timeout: int = 30
    ):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'fffdata-python-client/0.1.0',
            'Accept': 'application/json'
        })
    
    def _request(
        self, 
        method: str, 
        endpoint: str, 
        **kwargs
    ) -> Optional[Dict[str, Any]]:
        """Effectue une requête HTTP vers l'API
        
        Args:
            method: Méthode HTTP (GET, POST, etc.)
            endpoint: Endpoint de l'API
            **kwargs: Arguments additionnels pour requests
        
        Returns:
            Dict contenant la réponse JSON, ou None si ressource non trouvée (404)
        
        Raises:
            APIConnectionError: En cas d'erreur de connexion
            FFFAPIError: Pour toute autre erreur API
        """
        url = f"{self.base_url}{endpoint}"
        
        # Ajouter le timeout si non spécifié
        if 'timeout' not in kwargs:
            kwargs['timeout'] = self.timeout
        
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.Timeout:
            raise APIConnectionError(f"Timeout lors de la connexion à {url}")
        
        except requests.exceptions.ConnectionError:
            raise APIConnectionError(f"Impossible de se connecter à {url}")
        
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                return None  # Ressource non trouvée, on retourne None
            raise FFFAPIError(f"Erreur HTTP {response.status_code}: {e}")
        
        except requests.exceptions.JSONDecodeError:
            raise FFFAPIError("La réponse de l'API n'est pas un JSON valide")
        
        except requests.exceptions.RequestException as e:
            raise FFFAPIError(f"Erreur lors de la requête: {e}")
    
    def get_match_entities(self, numero_match: int) -> Optional[Match]:
        """Récupère les entités d'un match (équipes, joueurs, etc.)
        
        Args:
            numero_match: Numéro unique du match (entier)
        
        Returns:
            Instance de Match avec toutes les données structurées, ou None si le match n'existe pas
        
        Raises:
            InvalidMatchNumberError: Si le numéro de match est invalide
            FFFAPIError: Pour toute autre erreur API (connexion, timeout, etc.)
        
        Example:
            >>> client = FFFClient()
            >>> match = client.get_match_entities(3010203)
            >>> if match:
            >>>     print(f"{match.home.short_name} {match.home_score} - {match.away_score} {match.away.short_name}")
            >>>     print(f"Arbitre: {match.get_arbitre_principal().full_name}")
            >>> else:
            >>>     print("Match non trouvé")
        """
        if not isinstance(numero_match, int) or numero_match <= 0:
            raise InvalidMatchNumberError(
                "Le numéro de match doit être un entier positif"
            )
        
        endpoint = f"/api/match_entities/{numero_match}.json"
        data = self._request('GET', endpoint)
        
        if data is None:
            return None
        
        return Match.from_dict(data)
    
    def get_club(self, numero_club: int) -> Optional[Club]:
        """Récupère les informations d'un club
        
        Args:
            numero_club: Numéro unique du club (entier)
        
        Returns:
            Instance de Club avec toutes les données structurées, ou None si le club n'existe pas
        
        Raises:
            InvalidMatchNumberError: Si le numéro de club est invalide
            FFFAPIError: Pour toute autre erreur API (connexion, timeout, etc.)
        
        Example:
            >>> client = FFFClient()
            >>> club = client.get_club(10000)
            >>> if club:
            >>>     print(f"{club.name} - {club.location}")
            >>>     print(f"Téléphones: {', '.join(club.get_phone_numbers())}")
            >>> else:
            >>>     print("Club non trouvé")
        """
        if not isinstance(numero_club, int) or numero_club <= 0:
            raise InvalidMatchNumberError(
                "Le numéro de club doit être un entier positif"
            )
        
        endpoint = f"/api/clubs/{numero_club}.json"
        data = self._request('GET', endpoint)
        
        if data is None:
            return None
        
        return Club.from_dict(data)
    
    def close(self):
        """Ferme la session HTTP"""
        self.session.close()
    
    def __enter__(self):
        """Support du context manager"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Fermeture automatique avec context manager"""
        self.close()