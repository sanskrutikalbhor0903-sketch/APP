import gc
import os
import time
import tracemalloc
import psutil


class CyclicNode:
    """Simple class used to demonstrate reference cycles."""

    def __init__(self, idx: int) -> None:
        self.idx = idx
        self.payload = [idx] * 50
        self.partner: "CyclicNode | None" = None


def create_cyclic_objects(count: int = 10000) -> int:
    """Create pairs of objects referencing each other so refcounting cannot free them."""
    for i in range(count):
        a = CyclicNode(i)
        b = CyclicNode(i)
        a.partner = b
        b.partner = a
    return count * 2


def display_memory_usage(label: str) -> None:
    """Display process RSS memory, tracemalloc heap stats, and GC object counts."""
    process = psutil.Process(os.getpid())
    rss_mb = process.memory_info().rss / (1024 * 1024)
    current_bytes, peak_bytes = tracemalloc.get_traced_memory()
    tracked_objects = len(gc.get_objects())
    gen_counts = gc.get_count()

    print(f"\n--- {label} ---")
    print(f"  Process RSS Memory : {rss_mb:.2f} MB")
    print(f"  Traced Heap Current: {current_bytes / 1024:.2f} KB (Peak: {peak_bytes / 1024:.2f} KB)")
    print(f"  GC Tracked Objects : {tracked_objects}")
    print(f"  GC Gen Counts      : {gen_counts}")


def benchmark_gc_modes(cycles: int = 15000) -> None:
    """Compare execution time with automatic GC enabled vs disabled + manual collect."""
    print("\n=== Performance Comparison (Automatic GC vs Manual Collect) ===")

    # Mode 1: Automatic GC enabled
    gc.enable()
    gc.collect()
    t0 = time.perf_counter()
    create_cyclic_objects(cycles)
    auto_time = time.perf_counter() - t0
    gc.collect()
    print(f"  Automatic GC enabled time         : {auto_time:.4f} s")

    # Mode 2: Automatic GC disabled during allocation, followed by manual collect
    gc.disable()
    t0 = time.perf_counter()
    create_cyclic_objects(cycles)
    alloc_only_time = time.perf_counter() - t0
    collected = gc.collect()
    manual_total_time = time.perf_counter() - t0
    gc.enable()
    print(
        f"  GC disabled alloc + manual collect: {manual_total_time:.4f} s "
        f"(alloc: {alloc_only_time:.4f} s, collected: {collected} objects)"
    )


def main() -> None:
    tracemalloc.start()
    original_thresholds = gc.get_threshold()

    print("=== Initial Garbage Collector Configuration ===")
    print(f"GC Enabled   : {gc.isenabled()}")
    print(f"GC Thresholds: {original_thresholds}")

    display_memory_usage("1. Initial State")

    # Disable automatic GC so reference cycles remain uncollected
    gc.disable()
    created_nodes = create_cyclic_objects(10000)
    print(f"\nCreated {created_nodes} cyclic objects with automatic GC disabled.")
    display_memory_usage("2. After Creating Cyclic Objects (GC Disabled)")

    # Enable GC debugging, run manual collection, then disable debug flags
    print("\n=== 3. Running Manual gc.collect() with DEBUG_STATS ===")
    gc.set_debug(gc.DEBUG_STATS)
    t0 = time.perf_counter()
    collected = gc.collect()
    elapsed = time.perf_counter() - t0
    gc.set_debug(0)

    print(f"\nManual gc.collect() freed {collected} unreachable cyclic objects in {elapsed:.4f} s.")
    display_memory_usage("4. After Manual gc.collect()")

    # Threshold inspection and modification
    print("\n=== 5. Modifying & Restoring GC Thresholds ===")
    gc.set_threshold(500, 5, 5)
    print(f"Updated Thresholds : {gc.get_threshold()}")
    gc.set_threshold(*original_thresholds)
    print(f"Restored Thresholds: {gc.get_threshold()}")
    gc.enable()

    benchmark_gc_modes()
    tracemalloc.stop()
    
if __name__ == "__main__":
    main()