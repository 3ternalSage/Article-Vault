import datetime as dt
from datetime import date, time, datetime
from enum import Enum, auto

class CardMasteryLevel(Enum):
    NEW = 1
    FAMILIAR = 2
    PROFICIENT = 3
    EXPERT = 4
    MASTERED = 5

class CardStatus(Enum):
    NEW = 1
    LEARNING = 2
    SHORT_TERM = 3
    LONG_TERM = 4
    RELEARNING = 5

class CardInformation:
    def __init__(self) -> None:
        self.front: str = None
        self.back: str = None

class Card:
    def __init__(self) -> None:
        self.card_info: CardInformation = None

        self.card_id: int = None

        self.card_added: date = None
        self.first_review: date = None
        self.latest_review: date = None
        
        self.mastery: CardMasteryLevel = None
        self.status: CardStatus = None
        self.difficulty: int = None
        self.interval_factor: int = None

        self.next_review: datetime = None

        self.num_reviews: int = 0
        self.average_review_time: time = None
        self.total_review_time: time = None
    
    def create_new_card(self) -> None:
        self.card_added = date.today()
        self.mastery = CardMasteryLevel.NEW
        self.status = CardStatus.NEW
        self.difficulty = 100
        self.interval_factor = 100

        self.card_id = hash(self.card_added)

    def _save_card(self) -> None:
        raise NotImplementedError



