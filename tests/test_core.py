#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-16 10:32:22


import logging
import unittest
from redis import Redis

from state_machine import StateMachine, State, Event, RedisBackend
from state_machine.exceptions import StateChangedException, StateUnexcepedException

from . import log  # pylint: disable=unused-import


log = logging.getLogger(__name__)
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
        log.info("the state has changed by job1_o")
        with self.assertRaises(StateChangedException):
            log.info("so an error will be raised if you run job1_1.state")
            job1_1.state
        log.info("yes it is")
        job1_2 = Job(jobid=1, state="STARTED")
        job1_2.state = "NEW"
        log.info("the state has changed back by job1_2")
        log.info("so the job1_1.state will run successfully")
        log.info(f"job1_1.state: {job1_1.state}")
        with self.assertRaises(StateChangedException):
            log.info("the job1_0.state will fail")
            job1_0.state


if __name__ == "__main__":
    unittest.main()
