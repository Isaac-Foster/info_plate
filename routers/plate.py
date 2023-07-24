from flask import Blueprint, request

blue: Blueprint = Blueprint("plate", __name__, url_prefix="/plate")


@blue.route("/<plate>")
def query(plate: str):
    cookies = request.cookies.__dict__
    
    return {"message": "alguma coisa"}