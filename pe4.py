"""Pair Exercise 4: compare sequential and threaded Wikipedia downloads."""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from time import perf_counter
import re

import wikipedia
from wikipedia import wikipedia as wikipedia_api

QUERY = "generative artificial intelligence"
SEQUENTIAL_OUTPUT = Path("pe4_output/sequential")
CONCURRENT_OUTPUT = Path("pe4_output/concurrent")


def save_references(topic, output_dir):
    """Download one page and save its external references as UTF-8 text."""
    page = wikipedia.page(topic, auto_suggest=False)
    title = page.title
    references = page.references
    # Replace characters that cannot appear in filenames on common platforms.
    filename = re.sub(r'[<>:"/\\|?*]', "_", title).rstrip(". ")
    destination = output_dir / f"{filename}.txt"
    with destination.open("w", encoding="utf-8") as output_file:
        for reference in references:
            output_file.write(f"{reference}\n")
    return destination


def wiki_dl_and_save(topic):
    """Download and save one topic for the concurrent run."""
    return save_references(topic, CONCURRENT_OUTPUT)


def main():
    # wikipedia 1.4.0 defaults to HTTP. Wikimedia's API supports HTTPS.
    wikipedia_api.API_URL = "https://en.wikipedia.org/w/api.php"
    wikipedia.set_user_agent("IST303-PairExercise4/1.0 (https://github.com/JKBaboyan/303_Fall_26)")

    topics = wikipedia.search(QUERY)
    if not topics:
        raise SystemExit("Wikipedia returned no topics.")

    SEQUENTIAL_OUTPUT.mkdir(parents=True, exist_ok=True)
    start = perf_counter()
    for topic in topics:
        save_references(topic, SEQUENTIAL_OUTPUT)
    print(f"Sequential: {len(topics)} topics in {perf_counter() - start:.2f} seconds")

    topics = wikipedia.search(QUERY)
    CONCURRENT_OUTPUT.mkdir(parents=True, exist_ok=True)
    start = perf_counter()
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Consume the iterator so exceptions in worker threads are raised here.
        list(executor.map(wiki_dl_and_save, topics))
    print(f"Concurrent: {len(topics)} topics in {perf_counter() - start:.2f} seconds")


if __name__ == "__main__":
    main()
