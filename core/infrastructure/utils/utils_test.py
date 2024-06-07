import json
from datetime import datetime


def serialize_datetime(o: datetime) -> str:
    return o.isoformat()


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return serialize_datetime(o)
        return super().default(o)
