"""Modèles de données pour les matchs"""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class CDG:
    """Comité Départemental ou de Gestion"""
    cg_no: int
    name: str
    external_updated_at: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "CDG":
        return cls(
            cg_no=data.get("cg_no"),
            name=data.get("name", ""),
            external_updated_at=data.get("external_updated_at")
        )


@dataclass
class Competition:
    """Représente une compétition"""
    cp_no: int
    season: int
    type: str
    name: str
    level: str
    cdg: Optional[CDG] = None
    external_updated_at: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "Competition":
        cdg = None
        if data.get("cdg"):
            cdg = CDG.from_dict(data["cdg"])
        
        return cls(
            cp_no=data.get("cp_no"),
            season=data.get("season"),
            type=data.get("type", ""),
            name=data.get("name", ""),
            level=data.get("level", ""),
            cdg=cdg,
            external_updated_at=data.get("external_updated_at")
        )


@dataclass
class Phase:
    """Phase de la compétition"""
    number: int
    type: str
    name: str
    external_updated_at: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "Phase":
        return cls(
            number=data.get("number"),
            type=data.get("type", ""),
            name=data.get("name", ""),
            external_updated_at=data.get("external_updated_at")
        )


@dataclass
class Poule:
    """Poule de la compétition"""
    stage_number: int
    name: str
    poule_unique: bool
    at_least_one_match_resultat: bool
    external_updated_at: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "Poule":
        return cls(
            stage_number=data.get("stage_number"),
            name=data.get("name", ""),
            poule_unique=data.get("poule_unique", False),
            at_least_one_match_resultat=data.get("at_least_one_match_resultat", False),
            external_updated_at=data.get("external_updated_at")
        )


@dataclass
class PouleJournee:
    """Journée de poule"""
    number: int
    name: str
    external_updated_at: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "PouleJournee":
        return cls(
            number=data.get("number"),
            name=data.get("name", ""),
            external_updated_at=data.get("external_updated_at")
        )


@dataclass
class ClubInfo:
    """Informations du club dans un match"""
    cl_no: int
    logo: Optional[str] = None
    external_updated_at: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "ClubInfo":
        return cls(
            cl_no=data.get("cl_no"),
            logo=data.get("logo"),
            external_updated_at=data.get("external_updated_at")
        )


@dataclass
class Team:
    """Équipe participant au match"""
    club: ClubInfo
    category_code: str
    category_label: str
    category_gender: str
    number: int
    code: int
    short_name: str
    short_name_ligue: str
    short_name_federation: str
    type: str
    engagements: List[dict] = field(default_factory=list)
    external_updated_at: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "Team":
        club = None
        if data.get("club"):
            club = ClubInfo.from_dict(data["club"])
        
        return cls(
            club=club,
            category_code=data.get("category_code", ""),
            category_label=data.get("category_label", ""),
            category_gender=data.get("category_gender", ""),
            number=data.get("number"),
            code=data.get("code"),
            short_name=data.get("short_name", ""),
            short_name_ligue=data.get("short_name_ligue", ""),
            short_name_federation=data.get("short_name_federation", ""),
            type=data.get("type", ""),
            engagements=data.get("engagements", []),
            external_updated_at=data.get("external_updated_at")
        )


@dataclass
class TerrainMatch:
    """Terrain où se joue le match"""
    te_no: int
    name: str
    address: Optional[str] = None
    zip_code: Optional[str] = None
    city: Optional[str] = None
    libelle_surface: Optional[str] = None
    external_updated_at: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "TerrainMatch":
        return cls(
            te_no=data.get("te_no"),
            name=data.get("name", ""),
            address=data.get("address"),
            zip_code=data.get("zip_code"),
            city=data.get("city"),
            libelle_surface=data.get("libelle_surface"),
            external_updated_at=data.get("external_updated_at")
        )


@dataclass
class MatchMembre:
    """Membre officiel du match (arbitre, etc.)"""
    mm_no: int
    po_cod: str
    prenom: str
    nom: str
    label_position: str
    position_ordre: int
    external_updated_at: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "MatchMembre":
        return cls(
            mm_no=data.get("mm_no"),
            po_cod=data.get("po_cod", ""),
            prenom=data.get("prenom", ""),
            nom=data.get("nom", ""),
            label_position=data.get("label_position", ""),
            position_ordre=data.get("position_ordre"),
            external_updated_at=data.get("external_updated_at")
        )
    
    @property
    def full_name(self) -> str:
        """Retourne le nom complet"""
        return f"{self.prenom} {self.nom}"


@dataclass
class Match:
    """Représente un match de football
    
    Attributes:
        ma_no: Numéro unique du match
        competition: Compétition
        home: Équipe à domicile
        away: Équipe à l'extérieur
        date: Date du match
        time: Heure du match
        home_score: Score de l'équipe à domicile
        away_score: Score de l'équipe à l'extérieur
        status: Statut du match
        terrain: Terrain du match
        match_membres: Officiels du match (arbitres)
    """
    ma_no: int
    competition: Competition
    phase: Phase
    poule: Poule
    poule_journee: PouleJournee
    home: Team
    away: Team
    season: int
    status: str
    status_label: str
    date: str
    time: str
    home_score: int
    away_score: int
    home_resu: str
    away_resu: str
    cr_nb_but: int
    terrain: Optional[TerrainMatch] = None
    initial_date: Optional[str] = None
    ma_ar: Optional[str] = None
    ma_inver: Optional[str] = None
    ma_arret: Optional[str] = None
    is_overtime: Optional[str] = None
    home_but_contre: int = 0
    home_nb_point: Optional[int] = None
    home_nb_tir_but: Optional[int] = None
    home_nb_point_pena: int = 0
    home_is_forfeit: str = "N"
    away_but_contre: int = 0
    away_nb_point: Optional[int] = None
    away_nb_tir_but: Optional[int] = None
    away_nb_point_pena: int = 0
    away_is_forfeit: str = "N"
    seems_postponed: str = ""
    match_membres: List[MatchMembre] = field(default_factory=list)
    match_feuille: Optional[str] = None
    external_updated_at: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "Match":
        """Crée une instance de Match depuis un dictionnaire"""
        competition = Competition.from_dict(data.get("competition", {}))
        phase = Phase.from_dict(data.get("phase", {}))
        poule = Poule.from_dict(data.get("poule", {}))
        poule_journee = PouleJournee.from_dict(data.get("poule_journee", {}))
        home = Team.from_dict(data.get("home", {}))
        away = Team.from_dict(data.get("away", {}))
        
        terrain = None
        if data.get("terrain"):
            terrain = TerrainMatch.from_dict(data["terrain"])
        
        match_membres = []
        if data.get("match_membres"):
            match_membres = [MatchMembre.from_dict(m) for m in data["match_membres"]]
        
        return cls(
            ma_no=data.get("ma_no"),
            competition=competition,
            phase=phase,
            poule=poule,
            poule_journee=poule_journee,
            home=home,
            away=away,
            season=data.get("season"),
            status=data.get("status", ""),
            status_label=data.get("status_label", ""),
            date=data.get("date", ""),
            time=data.get("time", ""),
            home_score=data.get("home_score", 0),
            away_score=data.get("away_score", 0),
            home_resu=data.get("home_resu", ""),
            away_resu=data.get("away_resu", ""),
            cr_nb_but=data.get("cr_nb_but", 0),
            terrain=terrain,
            initial_date=data.get("initial_date"),
            ma_ar=data.get("ma_ar"),
            ma_inver=data.get("ma_inver"),
            ma_arret=data.get("ma_arret"),
            is_overtime=data.get("is_overtime"),
            home_but_contre=data.get("home_but_contre", 0),
            home_nb_point=data.get("home_nb_point"),
            home_nb_tir_but=data.get("home_nb_tir_but"),
            home_nb_point_pena=data.get("home_nb_point_pena", 0),
            home_is_forfeit=data.get("home_is_forfeit", "N"),
            away_but_contre=data.get("away_but_contre", 0),
            away_nb_point=data.get("away_nb_point"),
            away_nb_tir_but=data.get("away_nb_tir_but"),
            away_nb_point_pena=data.get("away_nb_point_pena", 0),
            away_is_forfeit=data.get("away_is_forfeit", "N"),
            seems_postponed=data.get("seems_postponed", ""),
            match_membres=match_membres,
            match_feuille=data.get("match_feuille"),
            external_updated_at=data.get("external_updated_at")
        )
    
    def get_score(self) -> str:
        """Retourne le score formaté"""
        return f"{self.home_score} - {self.away_score}"
    
    def get_match_label(self) -> str:
        """Retourne un label du match"""
        return f"{self.home.short_name} vs {self.away.short_name}"
    
    def get_arbitre_principal(self) -> Optional[MatchMembre]:
        """Retourne l'arbitre principal"""
        for membre in self.match_membres:
            if membre.po_cod == "AC":
                return membre
        return None
    
    def is_finished(self) -> bool:
        """Vérifie si le match est terminé"""
        return self.status == "A"  # A = Arbitré/Terminé
    
    def __repr__(self) -> str:
        return f"Match(ma_no={self.ma_no}, {self.get_match_label()}, score={self.get_score()})"