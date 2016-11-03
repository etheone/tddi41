#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pexpect
import time
import re


def testNtp():
    print("Test ID:       Ntp test - NTP")
    print("Purpose:       Check NTP")
    print("SUT:           GW")
    print("Preconditions: Network and NTP configured")
    print("Procedure:     Run ntpq -p")
    print("Return statuses: ")
    print("               0: Test passed")
    print("               1: Test failed")
    print("Pass criteria: OUR Ntp server connected to IDA GW and broadcasting on our subnet")
    child = pexpect.spawn('ntpq -p')
    print("Return status:")
    print(child.expect(["\*ida-gw.sysinst", pexpect.EOF]))
    print(child.expect(["130.236.179.87", pexpect.EOF]))
    print(child.expect([".BCST.", pexpect.EOF]))
    print("Test done.\n\n")

testNtp()


