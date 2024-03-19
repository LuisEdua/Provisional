
from models.Floor import Floor
def listar():
    from database.database import session
    areas = session.query(Floor).all()   
    response = []
    for area in areas:
        response.append({"uuid":area.uuid,"level":area.level})
    print(200)
    return response, 200

    
   
    
    