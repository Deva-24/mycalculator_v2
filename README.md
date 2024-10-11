# Python Calculator (Version 2)

## Overview
This Python calculator is a command-line application that performs basic arithmetic operations, including addition, subtraction, multiplication, division, modulus, and exponentiation (power). The program is designed using Object-Oriented Programming (OOP) principles, making it modular and easy to extend. It also maintains a history of calculations and allows users to view the complete history or the last operation.

## Features
- Supports six operations: addition, subtraction, multiplication, division, modulus, and power.
- Maintains history of operations.
- Allows users to view full history or just the last operation.
- Implements Object-Oriented Programming (OOP) principles, including abstraction, encapsulation, inheritance, and polymorphism.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Code Style](#code-style)
- [License](#license)

## Installation

### Prerequisites
- Python 3.x installed on your system.
- `pip` for managing Python packages.
- Ubuntu installed on your system.

### Creating a Virtual Environment (Ubuntu)
1. **Open a terminal.**
2. **Navigate to your project directory** (or create a new one if needed):
   ```bash
   mkdir mycalculator_v2
   cd mycalculator_v2
   ```

3. **Create a virtual environment** using `venv`:
   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

   You should see `(venv)` prefixed to your terminal prompt, indicating that the virtual environment is active.

### Clone the Repository
Clone this repository to your local machine using:
```bash
git clone https://github.com/Deva-24/mycalculator_v2.git
cd mycalculator_v2
```

### Install Dependencies
If there are any additional dependencies in the future, they can be listed in a `requirements.txt` file. For now, ensure you have `pytest` installed for testing:
```bash
pip install pytest
```

## Usage

### Running the Calculator
To run the calculator interactively, execute the following command:
```bash
python main.py
```

### Interacting with the Calculator
1. Choose an operation by entering the corresponding number:
   - `1`: Add (+) 
   - `2`: Subtract (-)
   - `3`: Multiply (*)
   - `4`: Divide (%)
   - `5`: Modulus (//)
   - `6`: Power (^)
   - `7`: View History 
   - `8`: Quit ()

2. For operations (1-6), you will be prompted to enter two numbers.
3. After performing an operation, you can choose to view the history of operations.

## Testing
To run the tests for the project, you can use `pytest`. Run the following command from the root of the project:
```bash
pytest
```

This will execute all tests defined in the `test` folder and show the results.

## Code Style
The project follows PEP 8 style guidelines for Python code. To check the code style, you can use `pylint`:
```bash
pylint app/calculator.py app/operations.py tests/test_calculator.py tests/test_operations.py main.py
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## Acknowledgments
- This project is built as part of a learning exercise in Python programming and Object-Oriented Programming concepts.
```
