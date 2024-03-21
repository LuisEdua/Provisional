
from models.Area import Area
from database.database import session


def listar(floor_uuid):
    areas = session.query(Area).filter(Area.floor_uuid == floor_uuid).all()   
    response = []
    for area in areas:
        response.append({"uuid":area.uuid,"name":area.name,"floor_uuid":area.floor_uuid})
    print(200)
    return response, 200

    
   
    
    