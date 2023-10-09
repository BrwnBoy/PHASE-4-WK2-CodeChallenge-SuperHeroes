from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Hero(db.Model):
    __tablename__ = "heroes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    powers = db.relationship("Power", secondary="hero_powers", back_populates="heroes")


class Power(db.Model):
    __tablename__ = "powers"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    heroes = db.relationship("Hero", secondary="hero_powers", back_populates="powers")

    @validates("description")
    def validate_description(self, key, description):
        if description.strip() != "" and len(description) < 20:
            raise ValueError(
                "Description must be present and at least 20 characters long"
            )
        return description


class HeroPower(db.Model):
    __tablename__ = "hero_powers"
    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))

    @validates("strength")
    def validate_strength(self, key, strength):
        strengths = ["Strong", "Weak", "Average"]
        if not strength in strengths:
            raise ValueError(
                "Strength must be one of the following values: 'Strong', 'Weak', 'Average'"
            )
        return strength
