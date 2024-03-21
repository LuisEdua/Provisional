
from models.Floor import Floor
from database.database import session

def listar():
    areas = session.query(Floor).all()   
    response = []
    for area in areas:
        response.append({"uuid":area.uuid,"level":area.level})
    print(200)
    return response, 200

    
   
    
    