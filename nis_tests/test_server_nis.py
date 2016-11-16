#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pexpect
import time
import re


def testNis1():
    print("Test ID:       Nis test1 - NIS")
    print("Purpose:       Check NIS server is running")
    print("SUT:           Server")
    print("Preconditions: Network and NIS configured")
    print("Procedure:     See if ypserv is running")
    print("Return statuses: ")
    print("               0: Test passed")
    print("               1: Test failed")
    print("Pass criteria: Our NIS server is running")
    child = pexpect.spawn('ps aux | grep ypserv')
    print("Return status:")
    print(child.expect(["/usr/sbin/ypserv", pexpect.EOF]))
    print("Test done.\n\n")

def testNis2():
    print("Test ID:       Nis test2 - NIS")
    print("Purpose:       Check NIS server contains correct information.")
    print("SUT:           Server")
    print("Preconditions: Network and NIS configured")
    print("Procedure:     Check if the map passwd contains the correct information")
    print("Return statuses: ")
    print("               0: Test passed")
    print("               1: Test failed")
    print("Pass criteria: Our NIS server contains the correct information")
    child = pexpect.spawn('ypcat -k passwd')
    print("Return status:")
    print(child.expect(["tomli962", pexpect.EOF]))
    print("Test done.\n\n")


testNis1()
testNis2()


