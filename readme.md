# Python Text Adventure

A project playground for learning:

- Python
- Vagrant, Virtual Box

## Branches

- `main` -> The python project
- `vagrant` _> The vagrant project

### Python Project Brief

This project consists of making a 'choose your own adventure' text based story/game that executes in the console.

- Classes (cat least one, but if you want to get fancy and can work in inheritance, feel free)
- Functions
- Control flow (if/elif/else)
- Logging the decisions to log files or to csv (or both) <- the rest is flexible, but this is necessary

### Vagrant Project Brief

GitHub repo matching the following file structure:

- app/your-source-code
- env/python_provisioning.sh
- Vagrantfile

1. A python_provisioning.sh that provisions the VM to run your Python App
2. We should be able to run vagrant up and then vagrant ssh into the VM and run your Python Project
3. Final Thing - Create a Readme.md that explains the following:
   - How to run the environment?
   - What dependencies you need to run the environment (i.e. Vagrant, Virtualbox)
   - How to run your project on the VM? (What steps do I need to do to see your project working once I have ssh’d into it?)
