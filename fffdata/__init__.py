"""Bibliothèque pour interagir avec l'API de la FFF"""

from .client import FFFClient
from .exceptions import (
    FFFAPIError, 
    MatchNotFoundError, 
    ClubNotFoundError,
    InvalidMatchNumberError
)

__version__ = "0.1.0"
__all__ = [
    "FFFClient", 
    "FFFAPIError", 
    "MatchNotFoundError",
    "ClubNotFoundError",
    "InvalidMatchNumberError"
]