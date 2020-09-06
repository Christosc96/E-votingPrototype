# E-votingPrototype

This is our prototype for an e-voting app, better suited for online polls rather than actual elections.

We initially designed the app to be a distributed system with multiple databases and opted for consistency and partition tolerance.
However, we decided that since voters will only do distinct writes to the system and the results are displayed at the end of the voting period,
there is no need for strong consistency and instead we took advantage of ACID databases (to make sure votes will be saved and not lost) to create a highly available partition tolerant system with eventual consistency.

Our approach consists of a write,merge and read step during a poll.

start back-end:
```
cd back-end
python app.py
```

start front-end:
```
cd front-end
npm start
```

run tests:

- through Postman Collection Runner importing collection from ```batch-requests/postman```

- or using a custom npm script 
 ```
  cd batch-requests
  npm start
  ```