from market import db


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=20), nullable=False, unique=True)
    password = db.Column(db.String(length=20), nullable=False)
    user_detail = db.relationship('UserJobsModel', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'UserModel({self.id}, {self.name}, {self.password})'


class UserJobsModel(db.Model):
    __tablename__ = 'user_jobs'
    id = db.Column(db.Integer(), primary_key=True)
    company = db.Column(db.String(length=50), nullable=False)
    designation = db.Column(db.String(length=50), nullable=False)
    doj = db.Column(db.Date(), nullable=False)
    dor = db.Column(db.Date())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'UserDetailModel({self.id}, {self.company}, {self.designation}, {self.doj}, ' \
               f'{self.dor}, {self.user_id})'

