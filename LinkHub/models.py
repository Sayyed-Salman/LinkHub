from LinkHub import db


class Link(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    provider_name: str = db.Column(db.String(100))
    about: str = db.Column(db.String(100))
    link: str = db.Column(db.String(500))
    email: str = db.Column(db.String(100))

    def __init__(self, name, desc, link, email) -> None:
        self.provider_name = name
        self.about = desc
        self.link = link
        self.email = email

    def __repr__(self) -> str:
        return f"<Link {self.id}\n{self.about}\n{self.link}\n{self.provider_name} />"


def init_db():
    db.create_all()

    res = Link(name="Salman",
               desc="Reading chinese.",
               link="https://www.duolingo.com",
               email="sayyedsalman2000@gmail.com"
               )
    db.session.add(res)
    db.session.commit()


if __name__ == '__main__':
    init_db()
