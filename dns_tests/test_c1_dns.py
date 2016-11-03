#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pexpect
import time
import re


def testPingInternalHost():
    print("Test ID:       PING INTERNAL - DNS")
    print("Purpose:       Check DNS")
    print("SUT:           Client-1")
    print("Preconditions: Network and DNS configured")
    print("Procedure:     Check if internal host is reachable through (name)server")
    print("Return statuses: ")
    print("               0: Test passed")
    print("               1: Test failed")
    print("Pass criteria: Internal network reachable through own nameserver.")
    child = pexpect.spawn('ping client-2.d3.sysinst.ida.liu.se')
    print("Return status:")
    print(child.expect(["130.236.179.84", pexpect.EOF]))
    print("Test done.\n\n")
        
def testDigInternalHost():
    print("Test ID:       DIG INTERNAL - DNS")
    print("Purpose:       Check DNS")
    print("SUT:           Client-1")
    print("Preconditions: Network and DNS configured")
    print("Procedure:     Dig internal host, verify (name)server")
    print("Return statuses: ")
    print("               0: Test passed")
    print("               1: Test failed")
    print("Pass criteria: Internal network reachable through own nameserver.")
    child = pexpect.spawn('dig client-2.d3.sysinst.ida.liu.se')
    print("Return status:")
    print(child.expect(["server.d3.sysinst.ida.liu.se.", pexpect.EOF]))
    print("Test done.\n\n")

def testDigXInternalHost():
    print("Test ID:       DIG -X INTERNAL - DNS")
    print("Purpose:       Check DNS")
    print("SUT:           Client-1")
    print("Preconditions: Network and DNS configured")
    print("Procedure:     Dig internal host, verify (name)server")
    print("Return statuses: ")
    print("               0: Test passed")
    print("               1: Test failed")
    print("Pass criteria: Reverse DNS lookup through own nameserver.")
    child = pexpect.spawn('dig -x 130.236.179.84')
    print("Return status:")
    print(child.expect(["client-2.d3.sysinst.ida.liu.se", pexpect.EOF]))
    print(child.expect(["server.d3.sysinst.ida.liu.se", pexpect.EOF]))
    print("Test done.\n\n")


testPingInternalHost()
testDigInternalHost()
testDigXInternalHost()
