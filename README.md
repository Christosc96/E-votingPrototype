# E-votingPrototype


This is our prototype for an e-voting app, better suited for online polls rather than actual elections.

We initially designed the app to be a distributed system with multiple databases and opted for consistency and partition tolerance.
However, we decided that since voters will only do distinct writes to the system and the results are displayed at the end of the voting period,
there is no need for strong consistency and instead we took advantage of ACID databases (to make sure votes will be saved and not lost) to create a highly available partition tolerant system with eventual consistency.

Our approach consists of a write,merge and read step during a poll.

curl -d "vote=1&vote_id=1&id=12345&name=christos&surname=papad" -X POST http://127.0.0.1:5000/vote

```
from https://ekloges.ypes.gr/current/v/home/parties/
5,769,644 / 48h =  120,201 votes/h
120,201 / 3,600 ~= 34 concurrent votes/sec
```