#!/usr/bin/env bash

ansible-galaxy collection build
ansible-galaxy collection publish --api-key ${GALAXY_API_KEY} mrichardson03-test_collection-*