# Vagrant Branch

## Overview

On this Branch I have provisioned a Virtual Machine(VM) using Vagrant & Virtual Box.

The VM has a synced folder meaning the text-adventure python project can be ran on the VM.

The provisioning script `env/python_provisioning` sets up the VM.

The `Vagrantfile` configures it.

## Setup

You will need both:

- Vagrant
- Virtual Box

In the project home directory run

```bash
vagrant up
```

Once provisioning is completed run

```bash
vagrant ssh
```

Once connected to the machine run to start the project

```bash
python3 app/main.py
```
