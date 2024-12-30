from flask import abort, make_response
from ..db import db

from flask import abort, make_response
from ..db import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        abort(make_response({"message": f"{cls.__name__} id {model_id} invalid"}, 400))
    
    primary_key_column = list(cls.__table__.primary_key.columns)[0]
    primary_key_name = primary_key_column.name

    column_attr = getattr(cls, primary_key_name)

    query = db.select(cls).where(column_attr == model_id)
    model = db.session.scalar(query)

    if not model:
        abort(make_response({ "message": f"{cls.__name__} {model_id} not found"}, 404))

    return model

def create_model(cls, model_data):
    try:
        new_model = cls.from_dict(model_data)
    except (KeyError, ValueError):
        response = {"details": "Invalid data"}
        abort(make_response(response, 400))
    
    db.session.add(new_model)
    db.session.commit()

    return new_model.to_dict(), 201


# def validate_model(cls, model_id):
#     try:
#         model_id = int(model_id)
#     except:
#         abort(make_response({"message":f"{cls.__name__} id {(model_id)} invalid"}, 400))
    
#     query = db.select(cls).where(cls.id == model_id)
#     model = db.session.scalar(query)

#     if not model:
#         abort(make_response({ "message": f"{cls.__name__} {model_id} not found"}, 404))
    
#     return model