#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-16 10:32:22


import logging
import unittest

from state_machine import StateMachine, State, Event, RedisBackend

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    )
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logging.getLogger("default").addHandler(ch)


class Job(StateMachine):
    backend = RedisBackend
    states = [
        State("NEW"),
        State("STARTED"),
        State("DONE"),
        State("CANCELED"),
    ]
    start = Event(from_states=["NEW", "CANCELED"], to_state="STARTED")

    def __init__(self, jobid):
        pass


class TestCore(unittest.TestCase):

    def test_states(self):
        logging.info("test_states start")
        job1_0 = Job(jobid=1)
        job1_1 = Job(jobid=1)
        job2_0 = Job(jobid=2)
        job2_1 = Job(jobid=2)
        job1_0.start()
