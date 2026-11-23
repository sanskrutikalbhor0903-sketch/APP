import logging
import threading
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] %(message)s",
    datefmt="%H:%M:%S",
)


def count_numbers(limit: int = 5) -> None:
    """Count sequentially from 1 to limit with brief I/O-like pauses."""
    logging.info("Starting counting task up to %d", limit)
    for i in range(1, limit + 1):
        logging.info("Count: %d", i)
        time.sleep(0.2)
    logging.info("Finished counting task")


def calculate_squares(numbers: list[int]) -> None:
    """Compute and log squares of the given numbers."""
    logging.info("Starting square calculation task")
    for num in numbers:
        logging.info("Square of %d = %d", num, num ** 2)
        time.sleep(0.2)
    logging.info("Finished square calculation task")


def calculate_cubes(numbers: list[int]) -> None:
    """Compute and log cubes of the given numbers."""
    logging.info("Starting cube calculation task")
    for num in numbers:
        logging.info("Cube of %d = %d", num, num ** 3)
        time.sleep(0.2)
    logging.info("Finished cube calculation task")


def main() -> None:
    numbers = [1, 2, 3, 4, 5]
    logging.info("Creating threads for concurrent execution")

    threads = [
        threading.Thread(target=count_numbers, args=(5,), name="CountThread"),
        threading.Thread(target=calculate_squares, args=(numbers,), name="SquareThread"),
        threading.Thread(target=calculate_cubes, args=(numbers,), name="CubeThread"),
    ]

    start_time = time.perf_counter()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    elapsed = time.perf_counter() - start_time
    logging.info("All threads completed in %.3f seconds", elapsed)


if __name__ == "__main__":
    main()