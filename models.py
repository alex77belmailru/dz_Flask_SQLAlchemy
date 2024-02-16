from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    added = db.Column(db.DateTime, nullable=False, default=func.now())
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id', ondelete='SET NULL'))
    genre = relationship('Genre', back_populates='book')

    def __repr__(self):
        return f'Книга {self.name}, автор {self.author}'


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    book = relationship('Book', back_populates='genre')

    def __repr__(self):
        return f'Жанр {self.name}'
