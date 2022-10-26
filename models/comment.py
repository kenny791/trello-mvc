from init import db, ma
from marshmallow import fields


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    date = db.Column(db.Date) #Date created

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'), nullable=False)

    user = db.relationship ("User", back_populates='comments')
    card = db.relationship ("Card", back_populates='comments')

class CommentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    card = fields.Nested('CardSchema')
    
    class Meta:
        fields = ('id', 'message', 'date', 'card', 'user')
        ordered = True