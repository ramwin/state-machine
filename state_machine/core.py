#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-16 10:30:34


import logging

from . import exceptions
from .backends import RedisBackend
from .base import Event


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class StateMachineMetaClass(type):

    def __new__(cls, class_name, bases, attrs, **kwargs):
        new_class = super(StateMachineMetaClass, cls).__new__(cls, class_name, bases, attrs, **kwargs)
        # for key, value in attrs.items():
        #     if isinstance(value, Event):
        #         log.info(f"key: {key}")
        #         log.info(f"value: {value}")
        #         def event_function(self):
        #             log.info(f"current state: {self.state}")
        #             if self.state not in value.from_states:
        #                 raise exceptions.StateUnexcepedException
        #             log.info(Event)
        #         setattr(new_class, "save_" + key, event_function)
        return new_class


class StateMachine(metaclass=StateMachineMetaClass):
    backend = None
    _state = None
    state_key = "state"

    def __init__(self, *args, **kwargs):
        if self.backend is None:
            raise Exception("please add backend=RedisBackend() in your StateMachine")
        state_value = kwargs.pop(self.state_key)
        setattr(self, "_state", state_value)

    @property
    def state(self):
        return self.backend.get_state(f"{self.backend_key}", self._state)

    @state.setter
    def state(self, value):
        self.backend.change_state(f"{self.backend_key}", from_state=self._state, to_state=value)
        self._state = value
        return self._state

    @property
    def backend_key(self):
        return str(self)
