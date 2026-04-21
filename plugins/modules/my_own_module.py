#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module
short_description: Creates a text file on a remote host
version_added: "1.0.0"
description:
  - This module creates a text file on the remote host with specified content.
options:
  path:
    description: Absolute path to the file to be created.
    required: true
    type: str
  content:
    description: Content to write into the file.
    required: true
    type: str
author:
  - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a file with content
  my_namespace.my_collection.my_own_module:
    path: /tmp/example.txt
    content: "Hello, world!"
'''

RETURN = r'''
path:
  description: Path to the file that was created or updated.
  type: str
  returned: always
content:
  description: Content that was written.
  type: str
  returned: always
changed:
  description: Whether the file was changed.
  type: bool
  returned: always
'''

import os
from ansible.module_utils.basic import AnsibleModule

def write_file(module, path, content):
    changed = False
    existing_content = None
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                existing_content = f.read()
        except Exception as e:
            module.fail_json(msg="Failed to read existing file: %s" % str(e))
    if existing_content != content:
        try:
            with open(path, 'w') as f:
                f.write(content)
            changed = True
        except Exception as e:
            module.fail_json(msg="Failed to write file: %s" % str(e))
    return changed

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )
    result = dict(changed=False, path='', content='')
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    path = module.params['path']
    content = module.params['content']
    result['path'] = path
    result['content'] = content
    if module.check_mode:
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    existing = f.read()
                result['changed'] = (existing != content)
            except:
                result['changed'] = True
        else:
            result['changed'] = True
        module.exit_json(**result)
    changed = write_file(module, path, content)
    result['changed'] = changed
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
