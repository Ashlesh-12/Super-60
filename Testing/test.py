# The basic workflow for using venue:

# 1. Create a virtual environment
# python -m venv venv

# 2.Activate
#  venv\Scripts\activate

# 3.Deactivate
#  deactivate

# 4.Install Pytest
#  pip install pytest

# To run the tests:
# pytest
# pytest file_name.py
# pytest -v file_name1.py file_name2.py
# pytest dir_name
# pytest -v dir_name/file_name.py::function_name

# Basic Naming Convention for pytest:

# Test files should be named test_<something>.py or
# <something>_test.py

# Test Methods/Functions should be named test_<something>

# Test Classes should be named Test<something>

# Possible outcomes of a test:

# Passed (.): The test has passed successfully
# Failed (F): The test has failed
# SKIPPED (s): The test was skipped
# XFAIL (X): The test was expected to fail, it ran and failed
# XPASS (X): The test was marked with XFAIL but it ran and passed
# ERROR (E): An error occurred while running the test

# The -v or --verbose command-line flag 

# The --tb=no command-line flag is used to turn off Tracebacks

# Exercise
# 1. Create a new folder
# 2. Create a virtual environment
# 3. Activate the virtual environment
# 4. Install pytest
# 5. Write a few test files and using different types of assert statements
 