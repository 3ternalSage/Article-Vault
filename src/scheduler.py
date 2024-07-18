from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cards import Card

from cards import CardStatus

def handle_new_card(user: 'User', card: 'Card', review_difficulty: str):
    raise NotImplementedError

handle_card_of_status = {
    CardStatus.NEW: handle_new_card
}

def schedule(user: 'User', card: 'Card', review_difficulty: str):
    handle_card_of_status[card.status](user, card, review_difficulty)
