"""Modèles de données pour les clubs"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class District:
    """Représente un district de football"""
    cg_no: int
    name: str
    short_name: str
    type_label: str
    cp_cod: List[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, data: dict) -> "District":
        """Crée une instance depuis un dict"""
        return cls(
            cg_no=data.get("cg_no"),
            name=data.get("name", ""),
            short_name=data.get("short_name", ""),
            type_label=data.get("type_label", ""),
            cp_cod=data.get("cp_cod", [])
        )


@dataclass
class Contact:
    """Représente un contact du club"""
    type: str
    type_label: str
    value: str
    
    @classmethod
    def from_dict(cls, data: dict) -> "Contact":
        """Crée une instance depuis un dict"""
        return cls(
            type=data.get("type", ""),
            type_label=data.get("type_label", ""),
            value=data.get("value", "")
        )


@dataclass
class Terrain:
    """Représente un terrain"""
    te_no: int
    name: str
    address: Optional[str] = None
    zip_code: Optional[str] = None
    city: Optional[str] = None
    libelle_surface: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    external_updated_at: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "Terrain":
        """Crée une instance depuis un dict"""
        return cls(
            te_no=data.get("te_no"),
            name=data.get("name", ""),
            address=data.get("address"),
            zip_code=data.get("zip_code"),
            city=data.get("city"),
            libelle_surface=data.get("libelle_surface"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            external_updated_at=data.get("external_updated_at")
        )


@dataclass
class Club:
    """Représente un club de football
    
    Attributes:
        cl_no: Numéro unique du club
        name: Nom complet du club
        short_name: Nom court du club
        location: Localisation du club
        affiliation_number: Numéro d'affiliation
        district: District du club
        department_code: Code département
        colors: Couleurs du club
        logo: URL du logo
        postal_code: Code postal
        contacts: Liste des contacts
        terrains: Liste des terrains
    """
    cl_no: int
    name: str
    short_name: str
    location: str
    affiliation_number: int
    district: Optional[District] = None
    department_code: Optional[int] = None
    colors: Optional[str] = None
    logo: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    address3: Optional[str] = None
    postal_code: Optional[str] = None
    distributor_office: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    contacts: List[Contact] = field(default_factory=list)
    terrains: List[Terrain] = field(default_factory=list)
    membres: List[dict] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, data: dict) -> "Club":
        """Crée une instance de Club depuis un dictionnaire
        
        Args:
            data: Dictionnaire contenant les données du club
            
        Returns:
            Instance de Club
        """
        district = None
        if data.get("district"):
            district = District.from_dict(data["district"])
        
        contacts = []
        if data.get("contacts"):
            contacts = [Contact.from_dict(c) for c in data["contacts"]]
        
        terrains = []
        if data.get("terrains"):
            terrains = [Terrain.from_dict(t) for t in data["terrains"]]
        
        return cls(
            cl_no=data.get("cl_no"),
            name=data.get("name", ""),
            short_name=data.get("short_name", ""),
            location=data.get("location", ""),
            affiliation_number=data.get("affiliation_number"),
            district=district,
            department_code=data.get("department_code"),
            colors=data.get("colors"),
            logo=data.get("logo"),
            address1=data.get("address1"),
            address2=data.get("address2"),
            address3=data.get("address3"),
            postal_code=data.get("postal_code"),
            distributor_office=data.get("distributor_office"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            contacts=contacts,
            terrains=terrains,
            membres=data.get("membres", [])
        )
    
    def get_full_address(self) -> str:
        """Retourne l'adresse complète formatée"""
        parts = [
            self.address1,
            self.address2,
            self.address3,
            f"{self.postal_code} {self.distributor_office}" if self.postal_code else None
        ]
        return ", ".join(filter(None, parts))
    
    def get_phone_numbers(self) -> List[str]:
        """Retourne tous les numéros de téléphone"""
        return [c.value for c in self.contacts if c.type.startswith("T")]
    
    def __repr__(self) -> str:
        return f"Club(cl_no={self.cl_no}, name='{self.name}', location='{self.location}')"