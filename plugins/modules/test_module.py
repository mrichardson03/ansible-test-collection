#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: test_module
short_description: A test module
author:
    - Michael Richardson (@mrichardson03)
version_added: 2.9
description:
    - This is a longer description of a test module

options:
    name:
        description:
            - This is the message to send to the test module
        type: str
        required: true
    new:
        description:
            - Control to demo if the result of this module is changed
        type: bool
        required: false
'''

EXAMPLES = '''
# Pass in a message
- name: Test with a message
  test_module:
    name: hello world

- name: Test with a message and changed output
  test_module:
    name: hello world
    new: true

- name: Fail the module
  test_module:
    name: fail me
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    returned: success
    type: str
message:
    description: The output message that the sample module generates
    returned: success
    type: str
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    module_args = dict(
        name=dict(type='str', required=True),
        new=dict(type='bool', required=False, default=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        changed=False,
        original_message='',
        message='',
    )

    if module.check_mode:
        return result

    result['original_message'] = module.params['name']
    result['message'] = 'goodbye'

    if module.params['new']:
        result['changed'] = True

    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail')

    module.exit_json(**result)


if __name__ == '__main__':
    main()
