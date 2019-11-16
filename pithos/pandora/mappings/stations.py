from .base import *

class Art(BaseModel):
    url: str
    size: int

class Station(BaseModel):
    stationId: str
    stationFactoryPandoraId: str
    pandoraId: str
    name: str
    dateCreated: str
    isNew: bool
    allowDelete: bool
    allowRename: bool
    allowEditDescription: bool
    allowAddSeed: bool
    isShared: bool
    isTransformAllowed: bool
    isOnDemandEditorialStation: bool
    isAdvertiserStation: bool
    canShuffleStation: bool
    canAutoshare: bool
    advertisingKey: str
    isArtistMessagesEnabled: bool
    isThumbprint: bool
    isShuffle: bool
    genre: List[str]
    adkv: Dict[str, str]
    creatorWebname: str

    # All fields below are optional and may not show up in certain responses.
    lastPlayed: str = None
    art: List[Art] = None
    totalPlayTime: int = None
    initialSeed: Dict[str, str] = None
    genreSponsorship: str = None
    artId: str = None
    adGenre: str = None
    antiTarget: bool = None
    seeds: Dict[str, str] = None
    positiveFeedbackCount: int = None
    negativeFeedbackCount: int = None
    dominantColor: str = None

# Responses

class GetStations(BaseModel):
    totalStations: int
    sortedBy: str
    index: int
    stations: List[Station]
