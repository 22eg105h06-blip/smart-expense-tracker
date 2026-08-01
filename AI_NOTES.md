# AI Usage Notes

## Overview

AI assistance was used during the development of the Smart Expense Tracker project as a development and troubleshooting aid.

The final code was reviewed, modified, executed, and tested locally before being included in the GitHub repository.

## Areas Where AI Assistance Was Used

AI assistance was used for the following areas:

1. **Project Structure**
   - Understanding how to organize the FastAPI application into `src/` and `tests/`.
   - Understanding the purpose of files such as `main.py`, test files, `README.md`, and `AI_NOTES.md`.

2. **FastAPI Development**
   - Assistance with understanding REST API implementation.
   - Reviewing API endpoint logic for creating, retrieving, filtering, updating, and deleting expenses.
   - Assistance with understanding request and response handling.

3. **Testing**
   - Assistance with creating and reviewing Pytest test cases.
   - Troubleshooting test execution and import-related errors.
   - Verifying the API using automated tests.

4. **Frontend**
   - Assistance with improving the HTML/JavaScript frontend.
   - Assistance with implementing the category-wise expense chart using Chart.js.
   - Troubleshooting frontend and API communication issues.

5. **Debugging**
   - AI assistance was used to understand errors such as:
     - `KeyError`
     - `NameError`
     - `ImportError`
     - `ModuleNotFoundError`
     - FastAPI internal server errors
   - Errors were investigated and changes were tested locally.

6. **Documentation**
   - AI assistance was used to prepare and improve the README documentation.
   - The documentation was reviewed to include installation, running the server, API documentation, and testing instructions.

## What Was Tested and Verified

The following areas were tested locally:

- Adding an expense
- Retrieving expenses
- Filtering expenses by category
- Calculating expense summaries
- Deleting expenses
- FastAPI API endpoints
- Swagger UI
- Frontend interaction with the API
- Automated Pytest tests

The final automated test execution was:


```text
python -m pytest -v
4 passed

Changes made to AI suggestions

AI suggestions were not blindly copied into the project.
The suggested code and solutions were reviewed against the actual project structure and requirements. Changes were made where necessary to make the code work with the existing FastAPI application, frontend, tests, and local JSON storage.
During development, some suggested approaches were modified or replaced after testing revealed compatibility or implementation issues.
For example, when the tests initially produced an import error for the src package, the project structure was adjusted by adding:
src/__init__.py
The tests were then executed again and successfully completed with:
4 passed


AI Suggestions That Were Not Used
Some AI suggestions were not used when they were unnecessary for the assignment or did not match the existing implementation.
Examples include:
Suggestions to add unnecessary advanced features that were outside the assignment requirements.
Suggestions to introduce a database when the current assignment could be completed using local JSON storage.
Suggestions that required changing the existing project structure unnecessarily.
Any solution that did not work correctly in the actual local environment was modified or discarded.
Developer Verification
All important functionality was manually checked and tested in the local development environment.
The final repository was reviewed before being pushed to GitHub.
The GitHub repository contains the source code, tests, README documentation, and this AI usage documentation.


Final Status
The project was completed, tested locally, and pushed to the public GitHub repository.
Final automated test result:
4 passed
