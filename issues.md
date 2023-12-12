## Issues
- no setup.py or setup.cfg
- modules are not in editable form, editable mangles the name into __editable."project name"."version" unreadable
- make sure to install in contained environment to avoid conflict
- autoadd dependencies to build files (pyproject.toml, setup.py, setup.cfg, etc...)