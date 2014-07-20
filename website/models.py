from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class Article(db.Model):
    """ Articles """
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    slug = db.Column(db.String(256), unique=True)
    content = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    post_date = db.Column(db.DateTime)
    last_update = db.Column(db.DateTime, nullable=True)
    # tags - an article can have many tags
    # comments - an article can have many comments


class Category(db.Model):
    """ Articles categories """
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    slug = db.Column(db.String(128), unique=True)
    posts = db.relationship('Article', backref='category', lazy='dynamic')


class Tag(db.Model):
    """ Articles tags """
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    slug = db.Column(db.String(64), unique=True)
    # posts = db.relationship('Article', backref='tags', lazy='dynamic')




class Role(db.Model):
    """ Users can be admins, guests-posts, or regular """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    """ User information """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    fullname = db.Column(db.String(128), nullable=True)
    twitter = db.Column(db.String(128), unique=True, nullable=True)
    instagram = db.Column(db.String(128), unique=True, nullable=True)
    # email = db.Column(db.String(128), unique=True)
    # bio = db.Column(db.Text, nullable=True)
    # profile_pic = db.Column(db.String(256))
    # date_joined = db.Column(db.Date)
    # password =
    # validated
    # comments
    # following
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

# cups
class Cup(db.Model):
    """ Cup tournaments """
    __tablename__ = 'cups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    abbreviation = db.Column(db.String(16), unique=True, nullable=True)
    slug = db.Column(db.String(128), unique=True, nullable=True)
    twitter = db.Column(db.String(128), unique=True, nullable=True)
    overview = db.Column(db.Text, nullable=True)
    # current_winner
    # past_winners
    # year

    def __repr__(self):
        return '<Cup %r>' % self.name


# leagues
class League(db.Model):
    """ Leagues in the CONCACAF """
    __tablename__ = 'leagues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    abbreviation = db.Column(db.String(16), unique=True, nullable=True)
    slug = db.Column(db.String(128), unique=True, nullable=True)
    twitter = db.Column(db.String(128), unique=True, nullable=True)
    teams = db.relationship('Team', backref='league', lazy='dynamic')

    def __repr__(self):
        return '<League %r>' % self.name


# teams
class Team(db.Model):
    """ Teams that play in the CONCACAF """
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    abbreviation = db.Column(db.String(16), unique=True, nullable=True)
    nickname = db.Column(db.String(64), nullable=True)
    slug = db.Column(db.String(128), unique=True, nullable=True)
    league_id = db.Column(db.Integer, db.ForeignKey('leagues.id'))
    # other_leagues =
    twitter = db.Column(db.String(128), unique=True, nullable=True)

    def __repr__(self):
        return '<Team %r>' % self.name
