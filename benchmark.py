import time
import original_app
import optimized_app


NUMBER_OF_STUDENTS = 100000


# Test original application
start_time = time.perf_counter()

original_app.process_students(NUMBER_OF_STUDENTS)

original_time = time.perf_counter() - start_time


# Test optimized application
start_time = time.perf_counter()

optimized_app.process_students(NUMBER_OF_STUDENTS)

optimized_time = time.perf_counter() - start_time


# Calculate improvement
improvement = (
    (original_time - optimized_time) / original_time
) * 100


print("\nPerformance Comparison")
print("======================")

print(f"Original execution time : {original_time:.6f} seconds")
print(f"Optimized execution time: {optimized_time:.6f} seconds")
print(f"Performance improvement : {improvement:.2f}%")