from app import db, ma

class Robot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    imei = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class RobotSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Robot
        load_instance = True
