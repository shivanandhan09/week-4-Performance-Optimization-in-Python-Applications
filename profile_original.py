import cProfile
import original_app


NUMBER_OF_STUDENTS = 100000


cProfile.run(
    "original_app.process_students(NUMBER_OF_STUDENTS)",
    "original_profile.prof"
)

print("Original application profiling completed.")