# AltOnline AB Database Tools (Milestone 4)

This project provides a command-line interface for interacting with the AltOnline AB MimerSQL database. It was developed as part of Milestone 4 to demonstrate database connectivity and manipulation using Python.

## Features

The application includes two main tools:

1.  **Department Browser**
    *   Navigate through the department hierarchy.
    *   Enter a Department ID to see its contents.
    *   **Non-leaf departments**: Displays a list of child departments.
    *   **Leaf departments**: Displays a list of products including their ID, Title, and calculated Discounted Price.

2.  **Discount Manager**
    *   Manage product discounts.
    *   Enter a Product ID to view its current details (Title and Discount).
    *   Update the discount percentage (0-100%) for the selected product.

## Prerequisites

*   **Python 3.8** or higher.
*   **MimerSQL Client Libraries**: You must have the MimerSQL client installed on your system (e.g., `libmimerapi.so` on Linux). The `mimerpy` adapter relies on these native libraries.
*   **Database Access**: Credentials to access the AltOnline AB database.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd altonlineab-milestone-4
    ```

2.  **Set up a virtual environment (recommended):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  Create a `.env` file in the root directory of the project.
2.  Add your database credentials to the file:

    ```dotenv
    DB_USER=your_username
    DB_PASSWORD=your_password
    DB_NAME=your_database_name
    ```

    *Note: The `.env` file is ignored by git to protect your credentials.*

## Usage

1.  **Activate your virtual environment** (if not already active):
    ```bash
    source .venv/bin/activate
    ```

2.  **Run the application:**
    ```bash
    python main.py
    ```

3.  **Follow the on-screen menu:**
    ```text
    Select a program:
    1. Department Browser
    2. Discount Manager
    q. Quit
    ```

## Project Structure

```text
.
├── main.py                 # Application entry point and CLI menu loop
├── requirements.txt        # Python package dependencies
├── .env                    # Environment variables (credentials) - NOT tracked by git
├── src/
│   ├── __init__.py
│   ├── database.py         # Database connection logic (includes Mock mode)
│   └── operations.py       # SQL queries and business logic functions
└── README.md               # Project documentation
```

## Troubleshooting

*   **`ModuleNotFoundError: No module named 'dotenv'`**: Ensure you have activated your virtual environment (`source .venv/bin/activate`) before running the script.
*   **`ImportError: Could not load Mimer API`**: This indicates that the MimerSQL native client libraries are missing from your system or not in the system path. The application will fall back to a **Mock Database** mode if this happens, allowing you to test the UI flow without a real connection.
