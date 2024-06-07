from datetime import date, datetime


def convert_date_to_datetime_dict(data: dict) -> dict:
    if data["birthdate"]:
        birthdate: date = data.get("birthdate")
    else:
        birthdate: date = data.get("birth_date")

    birth_str = birthdate.isoformat() + " 00:00:00"
    birth_datetime = datetime.strptime(birth_str, "%Y-%m-%d %H:%M:%S")

    if data["birthdate"]:
        data["birthdate"] = birth_datetime
    else:
        data["birth_date"] = birth_datetime

    return data


def convert_date_to_datetime_field(birthdate: date) -> datetime:
    min_time = datetime.min.time()
    birth_datetime = datetime.combine(birthdate, min_time)
    return birth_datetime


def convert_date_to_datetime_obj(obj: object):
    if hasattr(obj, "birthdate"):
        birthdate: date = obj.birthdate
    else:
        birthdate: date = obj.birth_date

    birth_str = birthdate.isoformat() + " 00:00:00"
    birth_datetime = datetime.strptime(birth_str, "%Y-%m-%d %H:%M:%S")

    if hasattr(obj, "birthdate"):
        obj.birthdate = birth_datetime
    else:
        obj.birth_date = birth_datetime

    return obj
