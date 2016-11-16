#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pexpect
import time
import re


def testNis():
    print("Test ID:       Nis test - NIS")
    print("Purpose:       Check NIS")
    print("SUT:           Client-2")
    print("Preconditions: Network and NIS-server configured")
    print("Procedure:     Run ypwhich to see if we are connected to the NIS server.")
    print("Return statuses: ")
    print("               0: Test passed")
    print("               1: Test failed")
    print("Pass criteria: Our NIS server is running and we are connected")
    child = pexpect.spawn('ypwhich')
    print("Return status:")
    print(child.expect(["130.236.179.82", pexpect.EOF]))
    print("Test done.\n\n")

testNis()

