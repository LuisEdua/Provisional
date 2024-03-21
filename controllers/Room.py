from models.Room import Room
from database.database import session

def listar(area_uuid):
    rooms = session.query(Room).filter(Room.area_uuid == area_uuid).all()
    response = []
    for room in rooms:
        response.append({"uuid": room.uuid, "number": room.number})
    return response, 200
