#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-16 10:57:45


# pylint:disable=missing-class-docstring

"""
all exceptions
"""


class StateMachineBaseException(Exception):
    """
    all exception show inherit the StateMachineBaseException
    """


class StateChangedException(StateMachineBaseException):

    message = "state diff from current state"


class StateChangingException(StateMachineBaseException):

    message = "the obj's state is changing by other process"


class StateUnexcepedException(StateMachineBaseException):

    message = "your state not in from_states"
