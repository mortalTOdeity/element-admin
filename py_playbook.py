#!/usr/bin/env python
#encoding=utf-8
 
import json
import shutil,requests
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase
from ansible import context
import ansible.constants as C
from optparse import Values
 
class ResultCallback(CallbackBase):

    def v2_runner_on_ok(self, result, **kwargs):
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))

    def v2_runner_on_failed(self, result, ignore_errors=False):
        host = result._host.get_name()
        #self.runner_on_failed(host, result._result, ignore_errors)
        print(json.dumps({host:result._result},indent=4))

    def v2_runner_on_unreachable(self, result):
        host = result._host.get_name()
        print(json.dumps({host:result._result},indent=4))

    def v2_playbook_on_no_hosts_matched(self):
        self.playbook_on_no_hosts_matched()
        self.status_no_hosts=True

    def v2_playbook_on_play_start(self, play):
        self.playbook_on_play_start(play.name)
        self.playbook_path=play.name

class AnsiblePlayBook():
    def __init__(self):
        self.options = {'verbosity': 0, 'ask_pass': False, 'private_key_file': None, 'remote_user': None,
                    'connection': 'smart', 'timeout': 10, 'ssh_common_args': '', 'sftp_extra_args': '',
                    'scp_extra_args': '', 'ssh_extra_args': '', 'force_handlers': False, 'flush_cache': None,
                    'become': False, 'become_method': 'sudo', 'become_user': None, 'become_ask_pass': False,
                    'tags': ['all'], 'skip_tags': [], 'check': False, 'syntax': None, 'diff': False,
                    'listhosts': None, 'subset': None, 'extra_vars': [], 'ask_vault_pass': False,
                    'vault_password_files': [], 'vault_ids': [], 'forks': 5, 'module_path': '/usr/lib/python2.7/site-packages/ansible/modules', 'listtasks': None,
                    'listtags': None, 'step': None, 'start_at_task': None, 'args': ['fake']}
        self.ops = Values(self.options)

    def playbookrun(self, inventory_path, playbook_path):
        self.loader = DataLoader()
        self.passwords = dict(vault_pass='TangGree')
        self.results_callback = ResultCallback()
        self.inventory = InventoryManager(loader=self.loader, sources= inventory_path)
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)
        # self.variable_manager._extra_vars = {'customer': 'test', 'disabled': 'yes'}
        context._init_global_context(self.ops)
        playbook = PlaybookExecutor(playbooks=playbook_path,
                                    inventory=self.inventory,
                                    variable_manager=self.variable_manager,
                                    loader=self.loader, passwords=self.passwords)
        result = playbook.run()
        return result


if __name__=='__main__':
    a=AnsiblePlayBook()
    a.playbookrun( inventory_path="/etc/ansible/hosts/test",playbook_path=['/etc/ansible/test.yml'])