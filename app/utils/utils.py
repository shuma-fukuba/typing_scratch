from typing import Optional


def get_slice_from_skip_and_limit(
        skip: Optional[int], limit: Optional[int]) -> slice:
    stop = skip + limit if not (skip is None or limit is None) else None
    return slice(skip, stop)
