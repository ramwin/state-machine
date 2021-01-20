#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-16 09:49:07


import redis
from . import exceptions

class BaseBackend:

    def expired(self, your_state=None, remote_state=None):
        raise exceptions.StateChangedException((
            f"State changed to {remote_state}, "
            f"your current {your_state} is deprecated"
        ))

    def block(self):
        raise exceptions.StateChangingException("the obj's state is changing by other process")


class RedisBackend(BaseBackend):
    timeout = 3600 * 24

    def __init__(self, con, *args, **kwargs):
        self.con = con
        pass

    def get_state(self, backend_key, default):
        state_key = f"state_machine:state:{backend_key}"
        self.con.setnx(state_key, default)
        self.con.expire(state_key, self.timeout)
        latest_state = self.get_remote_state(backend_key)
        if latest_state != default:
            self.expired(your_state=default, remote_state=latest_state)
        return latest_state

    def get_remote_state(self, backend_key):
        state_key = f"state_machine:state:{backend_key}"
        return self.con.get(state_key)

    def change_state(self, backend_key, from_state, to_state):
        """
        return True if success
        raise Exception if fail
        """
        lock_key = f"state_machine:lock:{backend_key}"
        state_key = f"state_machine:state:{backend_key}"
        lock = self.con.lock(lock_key)
        if not lock.acquire(blocking=False):
            return self.block()
        remote_state = self.get_state(backend_key, from_state)
        if remote_state != from_state:
            return self.expired(your_state=from_state, remote_state=remote_state)
        self.con.set(state_key, to_state)
        lock.release()
        return True
