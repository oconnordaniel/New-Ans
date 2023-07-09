# mkdir
## project


import os
import argparse
import shutil
import subprocess

def main():
    parser = argparse.ArgumentParser(
        description='Create a new Ansible project')
    parser.add_argument(
        'project_name', 
        metavar='project_name', 
        type=str, 
        help='The name of the project')

    parser.add_argument(
        '-p', 
        '--path', 
        metavar='path', 
        type=str, 
        help='The path to create the project in')

    args = parser.parse_args()

    # Set the project directory
    if args.path: 
        proj_dir = args.path
    else:
        proj_dir = os.getcwd()
    
    proj_name = args.project_name
    print('Creating project: ' + proj_name + ' in ' + proj_dir)

    # Make the project directory folder and the files folder
    if not os.path.exists(proj_dir + '/' + proj_name):
        os.makedirs(proj_dir + '/' + proj_name)
    
    if not os.path.exists(proj_dir + '/' + proj_name + '/files'):
        os.makedirs(proj_dir + '/' + proj_name + '/files')
    
    # Copy the template files to the project directory
    shutil.copyfile('files/ansible.cfg', proj_dir + '/' + proj_name + '/ansible.cfg')

    if not os.path.exists(proj_dir + '/' + proj_name + 'files/inventory.yml'):
        shutil.copyfile('files/inventory.yml', proj_dir + '/' + proj_name + '/files/inventory.yml')
    
    if not os.path.exists(proj_dir + '/' + proj_name + '/main.yml'):
        shutil.copyfile('files/main.yml', proj_dir + '/' + proj_name + '/main.yml')

    if not os.path.exists(proj_dir + '/' + proj_name + '/ReadMe.md'):
        shutil.copyfile('files/ReadMe.md', proj_dir + '/' + proj_name + '/ReadMe.md')
    
    if not os.path.exists(proj_dir + '/' + proj_name + 'files/passwords.yml'):
        shutil.copyfile('files/passwords.yml', proj_dir + '/' + proj_name + '/files/passwords.yml')

    if not os.path.exists(proj_dir + '/' + proj_name + 'files/id_ed25519_ansible'):
        shutil.copyfile('files/id_ed25519_ansible', proj_dir + '/' + proj_name + '/files/id_ed25519_ansible')

    if not os.path.exists(proj_dir + '/' + proj_name + 'files/id_ed25519_ansible.pub'):
        shutil.copyfile('files/id_ed25519_ansible.pub', proj_dir + '/' + proj_name + '/files/id_ed25519_ansible.pub')

    # Run ansoible-galaxy init main to create the roles directory
    print('ansible-galaxy init main')
    subprocess.run(['ansible-galaxy', 'init', 'main'], cwd=proj_dir + '/' + proj_name)

if __name__ == '__main__':
    main()
