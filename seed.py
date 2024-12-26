from app import create_app, db
from dotenv import load_dotenv
from app.models.board import Board
from app.models.card import Card

load_dotenv()

def seed_database():
    app = create_app()
    with app.app_context():

        board1 = Board(title="Complete the best Capstone on Earth", owner="Ada")
        board2 = Board(title="Cook the best tres leches", owner="Adrian")

        db.session.add_all([board1, board2])
        db.session.commit()

        card1 = Card(message="Research how actual the idea for the Capstone", likes_count=0, board_id=board1.board_id)
        card2 = Card(message="Find a Capstone partner", likes_count=0, board_id=board1.board_id)
        card3 = Card(message="Buy dark chocolate bar", likes_count=0, board_id=board2.board_id)

        db.session.add_all([card1, card2, card3])

        db.session.commit()
        print("Database seeded successfully!")
if __name__ == "__main__":
    seed_database()