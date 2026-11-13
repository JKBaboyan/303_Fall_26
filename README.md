# Pair Exercise #4: Concurrency

Pair listing: Johnathan Baboyan and Zehao Li (`parsifal12138`).

From the repository folder, using your activated Python environment:

```bash
python -m pip install wikipedia==1.4.0
python pe4.py
```

The script searches English Wikipedia for “generative artificial intelligence.” It writes
one reference per line into a text file named for the page title. The sequential loop
writes to `pe4_output/sequential/` and the four-worker thread pool writes to
`pe4_output/concurrent/`. Both timers cover downloads and file writes for the entire
list, excluding the search and folder setup. Internet access is required, and timings
vary with network conditions.
