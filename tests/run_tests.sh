#!/bin/sh

py.test --connection=docker --hosts=tests_server1_1,tests_server2_1 tests
