from ..db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

class Card(db.Model):
    __tablename__ = 'card'

    card_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes_count: Mapped[int] = mapped_column(default=0)
    board_id: Mapped[Optional[int]] = mapped_column(ForeignKey("board.board_id"))
    board: Mapped[Optional["Board"]] = relationship(back_populates="cards")

    def to_dict(self):
            return dict(
                card_id=self.card_id,
                message=self.message,
                likes_count=self.likes_count
            )
    
    @classmethod
    def from_dict(cls, card_data):
        return cls(message=card_data["message"],
                   board_id=card_data["board_id"])
