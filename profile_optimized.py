import cProfile
import optimized_app


NUMBER_OF_STUDENTS = 100000


cProfile.run(
    "optimized_app.process_students(NUMBER_OF_STUDENTS)",
    "optimized_profile.prof"
)

print("Optimized application profiling completed.")