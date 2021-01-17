#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-16 10:57:45


class BaseException(Exception):
    pass


class StateChangedException(BaseException):

    message = "state diff from current state"


class StateChangingException(BaseException):

    message = "the obj's state is changing by other process"


class StateUnexcepedException(BaseException):

    message = "your state not in from_states"
