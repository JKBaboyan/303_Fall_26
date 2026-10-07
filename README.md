# Pair Exercise 3: Functions and Classes

Johnathan Baboyan

The assignment implementation is in `pe3.py`.

- `encode(input_text, shift)` returns the lowercase English alphabet and the encoded text.
- `decode(input_text, shift)` reverses the shift. Both functions produce lowercase text and preserve punctuation, digits, and spaces.
- `BankAccount` checks the creation date, rejects negative deposits, and displays the balance after transactions.
- `SavingsAccount` permits withdrawals after 180 days and prevents overdrafts.
- `CheckingAccount` charges $30 each time a withdrawal leaves a negative balance.

## Run the instructor's tests

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
