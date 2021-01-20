# state-machine
a state machine that can change difference backends (current only redis backend, lately the filelockbackend)  
and keep state synchronously in different state even different host.

# Install
```
sudo pip3 install state-machine-2
```

# Usage
1. Create a State Backend
```
from state_machine import StateMachine, RedisBackend
from redis import Redis
# you will need to install redis
# see more information here: https://redis.io/download#installation
redis_backend = RedisBackend(con=Redis(decode_responses=True))
```
2. Create a State Machine Class
```
class Job(StateMachine):
    backend = redis_backend

    def __init__(self, state=None, jobid=None):
        self.jobid = jobid
        super().__init__(state=state, jobid=jobid)

    def __str__(self):
        return f"Job: {self.jobid}"
```
3. Use
```
# first progress
>>> job1_0 = Job(jobid=1, state="NEW")
>>> job1_0.state = "STARTED"
# second progress
>>> job1_1 = Job(jobid=1, state="NEW")
>>> job1_1.state = "STARTED"
Error: StateChangedException() # raise Exception because the state has changed by job1_0
```

# test and contribute
```
git clone git@github.com:ramwin/state-machine.git
pip3 install -e ./
cd tests
python3 __init__.py
```
