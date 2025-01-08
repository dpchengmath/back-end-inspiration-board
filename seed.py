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
        board3 = Board(title="Run a marathon", owner="Mikelle")
        board4 = Board(title="Learn machine learning", owner="Jane")
        board5 = Board(title="Write a novel", owner="Alice")
        board6 = Board(title="Master diving", owner="Elena")
        board7 = Board(title="Go backpacking in Europe", owner="Chris")
        
        db.session.add_all([board1, board2, board3, board4, board5,board6, board7,])
        db.session.commit()

        card1 = Card(message="Research how actual the idea for the Capstone", likes_count=0, board_id=board1.board_id)
        card2 = Card(message="Find a Capstone partner", likes_count=0, board_id=board1.board_id)
        card3 = Card(message="Buy dark chocolate bar", likes_count=0, board_id=board2.board_id)
        card4 = Card(message="Buy condensed milk", likes_count=0, board_id=board2.board_id)
        card5 = Card( message="Follow an 18-week training plan", likes_count=0,board_id=board3.board_id)
        card6 = Card(message="Buy running shoes", likes_count=0, board_id=board3.board_id)
        card7 = Card(message="Learn Python", likes_count=0, board_id=board4.board_id)
        card8 = Card(message="Book plane tickets and hostels",likes_count=0,board_id=board7.board_id)
        card9 = Card(message="Buy a backpack", likes_count=0, board_id=board7.board_id)


        db.session.add_all([card1, card2, card3, card4, card5, card6, card7, card8, card9])

        db.session.commit()
        print("Database seeded successfully!")
if __name__ == "__main__":
    seed_database()