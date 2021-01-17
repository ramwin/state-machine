#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-16 10:32:22


import unittest
from redis import Redis
from log import log

from state_machine import StateMachine, State, Event, RedisBackend


log.info("run test_core")
con = Redis(decode_responses=True)
con.flushall()


class Job(StateMachine):
    backend = RedisBackend(con=Redis(decode_responses=True))

    def __init__(self, state=None, jobid=None):
        self.jobid = jobid
        super().__init__(state=state, jobid=jobid)

    def __str__(self):
        return f"Job: {self.jobid}"


class TestCore(unittest.TestCase):

    def test_state_changed(self):
        log.info("test state changed if another object changed")
        job1_0 = Job(jobid=1, state="NEW")
        job1_1 = Job(jobid=1, state="NEW")
        job1_0.state = "STARTED"
        self.assertEqual(job1_1.state, "STARTED")


if __name__ == "__main__":
    unittest.main()
