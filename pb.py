#!/usr/bin/env python

import os
import sys
from collections import namedtuple

from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.executor.playbook_executor import PlaybookExecutor

variable_manager = VariableManager()
loader = DataLoader()

inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list='ec2.py')
#playbook_path = './mongodb/deploy.yml'
#playbook_path = 'test.yml'

p = './wordpress/provisioning.yml'
s = './wordpress/site.yml'

if not os.path.exists(p):
    print '[INFO] The playbook does not exist'
    sys.exit()

Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'remote_user', 'private_key_file', 'ssh_common_args', 'sftp_extra_args', 'scp_extra_args', 'ssh_extra_args', 'verbosity', 'listhosts', 'listtasks', 'listtags', 'syntax'])

options = Options(connection='local', module_path=None, forks=100, become=None, become_method=None, become_user='root', check=False, remote_user='root', private_key_file=' ~/.ssh/cf-wp.pem', ssh_common_args='', sftp_extra_args='', scp_extra_args='', ssh_extra_args='', verbosity=4, listhosts=False, listtasks=False, listtags=False, syntax=False)

variable_manager.extra_vars = {'aaa': 'bbb'} # This can accomodate various other command line arguments.`

passwords = {}

pbex = PlaybookExecutor(playbooks=[s], inventory=inventory, variable_manager=variable_manager, loader=loader, options=options, passwords=passwords)

results = pbex.run()
