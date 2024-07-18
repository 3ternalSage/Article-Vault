import cards

def main():
    c = cards.Card()
    c.create_new_card()
    print(c.card_id)

if __name__ == '__main__':
    main()