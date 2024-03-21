from flask import Blueprint, request
from controllers import Floor




DataRoutes = Blueprint("floor", __name__)

@DataRoutes.route('/floor/listar', methods=['GET'])
def inciarAnalisis():    
    floors,  status = Floor.listar()
       
    return floors, status
