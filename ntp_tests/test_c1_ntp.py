#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pexpect
import time
import re


def testNtp():
    print("Test ID:       Ntp test - NTP")
    print("Purpose:       Check NTP")
    print("SUT:           Client-1")
    print("Preconditions: Network and NTP configured")
    print("Procedure:     Run ntpq -p and check to see if our NTP server exists in response")
    print("Return statuses: ")
    print("               0: Test passed")
    print("               1: Test failed")
    print("Pass criteria: Our NTP server exists")
    child = pexpect.spawn('ntpq -p')
    print("Return status:")
    print(child.expect(["130.236.179.81", pexpect.EOF]))
    print("Test done.\n\n")

testNtp()


