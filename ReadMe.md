# New Ansible Projects

## Description

This is a script to create a new ansible project with basic layout and default role.

This scrip will create the new project in the current directory unless the --dir option is used. It will make the following files directories:

```bash
.
├─ files
│  ├─ id_ed25519_ansible 
│  ├─ id_ed25519_ansible.pub
│  ├─ invintory.yml
│  ├─ passwords.yml
│  └─ logs 
├─ main_role
│  ├── defaults
│  ├── files
│  ├── handlers
│  ├── meta
│  ├── tasks
│  ├── templates
│  ├── tests
│  ├── vars
│  └── README.md
├─ .gitignore
├─ ansible.cgf
├─ License
├─ main.yml
└─ ReadMe.md
```

## Usage and options

```bash
usage: new-ans.py [-h] [-p path] project_name

Create a new Ansible project

positional arguments:
  project_name          The name of the project

options:
  -h, --help            show this help message and exit
  -p path, --path path  The path to create the project in
```
