# Project Name

[![CircleCI](https://circleci.com/gh/your-username/your-repo.svg?style=svg)](https://circleci.com/gh/your-username/your-repo)

This project demonstrates how to set up Continuous Integration and Continuous Deployment (CI/CD) using CircleCI for a Python project.

## Prerequisites

- Python 3.x
- Pip (Python package installer)
- Virtual environment (optional but recommended)

## Getting Started

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
Start using the project and make necessary modifications.

The CI/CD pipeline is defined in the .circleci/config.yml file. It performs the following steps:

Sets up a Python environment
Installs project dependencies
Runs tests using pytest
You can view the build status and details on the CircleCI website.

Contributing
Contributions are welcome! If you find any issues or want to suggest improvements, please open an issue or submit a pull request.

### Run the code
```
python main.py
```

### Test the code
```
python tests.py
```
