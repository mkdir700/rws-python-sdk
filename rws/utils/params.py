# -*- coding: utf-8 -*-
"""
Created on 2021/6/15 12:59
---------
@summary: 
---------
@author: mkdir700
@email:  mkdir700@gmail.com
"""
from collections.abc import Mapping
from enum import Enum
from typing import Any, List, Union
from urllib.parse import quote


def remove_empty_param_keys(params: Mapping) -> dict:
    """Returns a copy of ``params`` dict where any key with a value of ``None``
    or ``""`` (empty string) are removed.
    """
    return {k: v for k, v in params.items() if v is not None and v != ""}


# def clean_params_dict(params: Mapping, urlencode=False) -> dict:
#     """Clean multiple param values in a dict, returning a new dict
#     containing the original keys and cleaned values.
#     """
#     cleaned_params = dict()
#     for key, val in params.items():
#         try:
#             newval = clean_value(val)
#             if urlencode:
#                 newval = quote(val, safe="-_.~")
#             cleaned_params[key] = newval
#         except ValueError as exc:
#             raise MWSError(str(exc)) from exc
#     return cleaned_params
