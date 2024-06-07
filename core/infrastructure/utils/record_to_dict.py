from typing import Any, Dict


def record_to_dict(record: Any) -> Dict:
    original = dict(record)
    in_db = {}
    for k, v in original.items():
        if k == "created_by" or k == "updated_by":
            v = str(v)
        in_db[k] = v
    return in_db
