"""
some useful functions
"""


import logging
from typing import List

from .core import StateMachine
from .exceptions import StateMachineBaseException


LOGGER = logging.getLogger(__name__)


def change_items_state(
        items: List[StateMachine],
        target_state,
) -> bool:
    """
    change all item from from_state to target_state
    if any of items failed, all the item will go back to origin state
    """
    origin_state = {}
    has_error = False
    for item in items:
        origin_state[item.backend_key] = item.state
        try:
            item.state = target_state
        except StateMachineBaseException:
            has_error = True
            # del origin_state[item.backend_key]
            break
    if has_error:
        for item in items:
            if item.backend_key in origin_state:
                item.state = origin_state.pop(item.backend_key)
        return False
    return True
