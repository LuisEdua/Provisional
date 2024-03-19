from flask import Blueprint, request
from controllers import Area




DataRoutes = Blueprint("/area", __name__)

@DataRoutes.route('/area/listar/<string:floor_uuid>', methods=['GET'])
def inciarAnalisis(floor_uuid):    
    areas,  status = Area.listar(floor_uuid)
       
    return areas, status
