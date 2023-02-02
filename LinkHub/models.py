from LinkHub import db


class Link(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    provider_name: str = db.Column(db.String(100))
    about: str = db.Column(db.String(100))
    link: str = db.Column(db.String(500))
    email: str = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"<Link {self.id}\n{self.about}\n{self.link}\n{self.provider_name} />"
