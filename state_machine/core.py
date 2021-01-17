#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-16 10:30:34


import logging

from .backends import RedisBackend
from .base import Event


class StateMachineMetaClass(type):

    def __new__(cls, class_name, bases, attrs, **kwargs):
        new_class = super(StateMachineMetaClass, cls).__new__(cls, class_name, bases, attrs)
        logging.info("create a new state machine class")
        for key, value in attrs.items():
            if isinstance(value, Event):
                def event_function(self):
                    logging.info(f"calling {key}")
                setattr(new_class, key, event_function)
        return new_class


class StateMachine(metaclass=StateMachineMetaClass):
    backend = RedisBackend
