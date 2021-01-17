#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-16 10:04:47


class State(str):

    pass


class Event(object):

    def __init__(self, from_states=None, to_state=None):
        self.from_states = from_states
        self.to_state = to_state
