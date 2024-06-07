import math
from typing import Dict, List

from loguru import logger


def short_pagination(page_num: int, page_size: int, data_list: List, route: str) -> Dict:
    start = (page_num - 1) * page_size
    end = start + page_size
    data_length = len(data_list)
    pages = math.ceil(data_length / page_size)

    response = {
        "data": data_list[start:end],
        "total": len(data_list),
        "count": page_size,
        "pages": pages,
        "pagination": {},
    }

    if end >= data_length:
        response["pagination"]["next"] = None
        if page_num > 1:
            response["pagination"][
                "previous"
            ] = f"{route}?page_number={page_num-1}&page_size{page_size}"
        else:
            response["pagination"]["previous"] = None
    else:
        if page_num > 1:
            response["pagination"][
                "previous"
            ] = f"{route}?page_number={page_num-1}&page_size{page_size}"
        else:
            response["pagination"]["previous"] = None

        response["pagination"]["next"] = f"{route}?page_number={page_num+1}&page_size{page_size}"

    return response


def short_pagination_aps(
    page_num: int, page_size: int, data_list: List, total_pages: List, route: str
) -> Dict:
    start = (page_num - 1) * page_size
    end = start + page_size
    total = str(total_pages[0]).split(sep="=")
    total = total[1]
    pages = math.ceil(int(total) / page_size)
    response = {
        "data": data_list,
        "total": int(total),
        "count": page_size,
        "pages": pages,
        "pagination": {},
    }

    if end >= pages:
        response["pagination"]["next"] = None
        if page_num > 1:
            response["pagination"][
                "previous"
            ] = f"{route}?page_number={page_num-1}&page_size{page_size}"
        else:
            response["pagination"]["previous"] = None
    else:
        if page_num > 1:
            response["pagination"][
                "previous"
            ] = f"{route}?page_number={page_num-1}&page_size{page_size}"
        else:
            response["pagination"]["previous"] = None

        response["pagination"]["next"] = f"{route}?page_number={page_num+1}&page_size{page_size}"

    return response
