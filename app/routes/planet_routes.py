from flask import Blueprint
from app.models.planet import list_of_planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# wave 1 get all list of planets
@planets_bp.get("")
def get_planets():
    planets_response = []
    
    for planet in list_of_planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "diameter": planet.diameter
        })
    return planets_response

# wave 2 get one existing planet
@planets_bp.get("/planets/<planet_id>")
def get_one_planets(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"message": "Planet id must be an integer"}, 400
        
    for planet in list_of_planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "diameter": planet.diameter
            }        
    return {"message": "Planet not found!"}, 404
