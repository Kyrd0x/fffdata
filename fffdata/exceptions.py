"""Exceptions personnalisées pour fffdata"""


class FFFAPIError(Exception):
    """Exception de base pour les erreurs d'API FFF"""
    pass


class MatchNotFoundError(FFFAPIError):
    """Exception levée quand un match n'est pas trouvé"""
    pass


class ClubNotFoundError(FFFAPIError):
    """Exception levée quand un club n'est pas trouvé"""
    pass


class InvalidMatchNumberError(FFFAPIError):
    """Exception levée quand le numéro de match ou club est invalide"""
    pass


class APIConnectionError(FFFAPIError):
    """Exception levée en cas de problème de connexion à l'API"""
    pass