from flask import Blueprint, request
from controllers import Room



DataRoutes = Blueprint('/room', __name__)

@DataRoutes.route('/room/listar/<string:area_uuid>', methods=['GET'])
def listar(area_uuid):
    rooms, status = Room.listar(area_uuid)

    return rooms, status
