# AltOnline AB Database Tools

This project contains Python tools for interacting with the AltOnline AB MimerSQL database, developed for Milestone 4. It includes two main utilities:

1. **Department Browser**: Navigate through the department hierarchy and view products in leaf departments.
2. **Discount Manager**: View and update discounts for specific products.

## Prerequisites

- Python 3.8 or higher
- MimerSQL client libraries (specifically `libmimerapi.so` must be available on your system)

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd altonlineab-milestone-4
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the root directory. You can use the following template:

   ```env
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_NAME=your_database
   ```

2. Replace `your_username`, `your_password`, and `your_database` with your actual MimerSQL credentials.

## Usage

To run the application, execute the `main.py` script from the root directory:

```bash
python main.py
```

### Features

- **Department Browser**:
  - Enter a Department ID to view its contents.
  - If it's a leaf department (no sub-departments), it lists all products with their ID, Title, and Discounted Price.
  - If it's a non-leaf department, it lists all child departments.

- **Discount Manager**:
  - Enter a Product ID to view its current details (Title and Discount).
  - Enter a new discount percentage (0-100) to update the product's discount in the database.

## Project Structure

```text
.
├── main.py                 # Entry point of the application
├── src/
│   ├── __init__.py
│   ├── database.py         # Database connection logic
│   └── operations.py       # SQL queries and business logic
├── .env                    # Environment variables (credentials)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Troubleshooting

- **ImportError: Could not load Mimer API**: This usually means the MimerSQL client libraries are not installed or not found on your system path. Ensure you have the MimerSQL client installed for your operating system.
