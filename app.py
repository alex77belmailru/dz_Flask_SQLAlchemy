from datetime import datetime

from flask import Flask, render_template, request

from models import db, Book, Genre

BOOKS_TO_SHOW = 15

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    novel = Genre(name='Роман')
    sci_fi = Genre(name='Научная фантастика')

    db.session.add(novel)
    db.session.add(sci_fi)

    db.session.add(Book(name='Мастер и Маргарита', author='Булгаков М.А.', genre=novel,
                        added=datetime.strptime('2024-02-16', '%Y-%m-%d')))
    db.session.add(Book(name='Война и мир', author='Толстой Л.Н.', genre=novel,
                        added=datetime.strptime('2021-01-15', '%Y-%m-%d')))
    db.session.add(Book(name='Пикник на обочине', author='А. и Б. Стругацкие', genre=sci_fi,
                        added=datetime.strptime('2023-06-16', '%Y-%m-%d')))
    db.session.add(Book(name='Сто лет одиночества', author='Габриель Гарсиа Маркес', genre=novel,
                        added=datetime.strptime('2024-07-12', '%Y-%m-%d')))
    db.session.add(Book(name='Три мушкетера', author='Дюма А.', genre=novel,
                        added=datetime.strptime('2008-08-18', '%Y-%m-%d')))
    db.session.add(Book(name='Мертвые души', author='Гоголь Н. В.', genre=novel,
                        added=datetime.strptime('2015-01-16', '%Y-%m-%d')))
    db.session.add(Book(name='Идиот', author='Достоевский Ф.М', genre=novel,
                        added=datetime.strptime('2014-01-12', '%Y-%m-%d')))
    db.session.add(Book(name='Двадцать тысяч лье под водой', author='Верн Ж.', genre=sci_fi,
                        added=datetime.strptime('2020-09-16', '%Y-%m-%d')))
    db.session.add(Book(name='Солярис', author='Лем С.', genre=sci_fi,
                        added=datetime.strptime('2022-01-19', '%Y-%m-%d')))
    db.session.add(Book(name='Человек-амфибия', author='Беляев А.Р.', genre=sci_fi,
                        added=datetime.strptime('2021-01-10', '%Y-%m-%d')))
    db.session.add(Book(name='Герой нашего времени', author='Лермонтов М.Ю.', genre=novel,
                        added=datetime.strptime('2023-01-06', '%Y-%m-%d')))
    db.session.add(Book(name='Черный обелиск', author='Эрих Мария Ремарк', genre=novel,
                        added=datetime.strptime('2012-03-16', '%Y-%m-%d')))
    db.session.add(Book(name='451 по Фаренгейту', author='Брэдбери Р.', genre=sci_fi,
                        added=datetime.strptime('2010-01-17', '%Y-%m-%d')))
    db.session.add(Book(name='Я, робот', author='Азимов А.', genre=sci_fi,
                        added=datetime.strptime('2004-04-16', '%Y-%m-%d')))
    db.session.add(Book(name='Робинзон Крузо', author='Дефо Д.', genre=novel,
                        added=datetime.strptime('2000-01-26', '%Y-%m-%d')))
    db.session.add(Book(name='Машина времени', author='Уэллс Г.', genre=sci_fi,
                        added=datetime.strptime('2024-8-16', '%Y-%m-%d')))

    db.session.commit()


@app.route('/')
def book_list():
    books = Book.query.order_by(Book.added.desc()).limit(BOOKS_TO_SHOW)
    return render_template('book_list.html', books=books)


@app.route('/genre/<int:genre_id>/')
def books_by_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return render_template('books_by_genre.html', books=genre.book, genre_name=genre.name)


if __name__ == '__main__':
    app.run()
