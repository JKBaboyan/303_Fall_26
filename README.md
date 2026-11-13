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

## Pair Exercise #3: Functions and Classes

Partners:

- Johnathan Baboyan ([JKBaboyan](https://github.com/JKBaboyan))
- Zehao Li ([parsifal12138](https://github.com/parsifal12138))

The assignment implementation is in `pe3.py`.

- `encode(input_text, shift)` returns the lowercase English alphabet and the encoded text.
- `decode(input_text, shift)` reverses the shift. Both functions produce lowercase text and preserve punctuation, digits, and spaces.
- `BankAccount` checks the creation date, rejects negative deposits, and displays the balance after transactions.
- `SavingsAccount` permits withdrawals after 180 days and prevents overdrafts.
- `CheckingAccount` charges $30 each time a withdrawal leaves a negative balance.

### Run the instructor's tests

Keep `pe3.py`, `test_pe3.py`, and `pytest.ini` in the same folder. From that folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
python -m pytest -v test_pe3.py
```

Expected result: **25 passed, 2 xfailed**. The two expected failures are intentionally marked in the instructor's tests.

Verified on October 7, 2026, using Python 3.14.7 and pytest 9.1.1: **25 passed, 2 xfailed**. Additional checks verified the 180-day savings withdrawal boundary, overdraft rejection for a mature savings account, repeated checking overdraft fees, and cipher wraparound.

`test_pe3.py` is the unmodified instructor-provided test file. `pytest.ini` contains the supplied settings converted from rich text to plain text, with the savings marker description corrected.
