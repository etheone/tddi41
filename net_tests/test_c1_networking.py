#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pexpect
import time
import re

'''***********
***GW TESTS***
***********'''

def testCheckClient1Ips():
        print("Test ID:       HOSTNAME-1")
        print("Purpose:       Check client-1 IP")
        print("SUT:           Client-1")
        print("Preconditions: Basic configuration")
        print("Procedure:     Check ip's and make sure that they are correct.")
        print("Return statuses: ")
        print("               0: Test passed")
        print("               1: Test failed")
        print("Pass criteria: Successful hostname set.")
        child = pexpect.spawn('hostname --all-ip-addresses')
        print("Return status:")
        print(child.expect(["130.236.179.83", pexpect.EOF]))
        print("Test done.\n\n")

def testHostname():
        print("Test ID:       HOSTNAME-2")
        print("Purpose:       Test client-1 hostname")
        print("SUT:           GW")
        print("Preconditions: Basic configuration")
        print("Procedure:     Cat /etc/hostname to see if it is correctly set.")
        print("Return statuses: ")
        print("               0: Test passed")
        print("               1: Test failed")
        print("Pass criteria: Successful hostname set.")
        child = pexpect.spawn('hostname')
        print("Return status:")
        print(child.expect(["client-1", pexpect.EOF]))
        print("Test done.\n\n")
        
def testInternalHost1():
        print("Test ID:       INTERNAL-1")
        print("Purpose:       Test client-1 connection to gw (no nameserver")
        print("SUT:           Client-1")
        print("Preconditions: eth0 configured correctly")
        print("Procedure:     Calling the following commands")
        print("               1. ping -c 1 130.236.179.83")
        print("Return statuses: ")
        print("               0: Test passed")
        print("               1: 5 second timeout reached")
        print("               2: Test designed poorly and probably failed")
        print("Pass criteria: Successful ping, eg prints 0")
        child = pexpect.spawn('ping -c 1 130.236.179.81')
        print("Return status:")
        print(child.expect(["64 bytes from 130.236.179.81", pexpect.TIMEOUT, pexpect.EOF], 5))
        print("Test done.\n\n")

def testInternalHost2():
        print("Test ID:       INTERNAL-2")
        print("Purpose:       Test client-1 connectivity to client-2 (no nameserver")
        print("SUT:           Client-1")
        print("Preconditions: eth0 configured correctly")
        print("Procedure:     Calling the following commands")
        print("               1. ping -c 1 130.236.179.84")
        print("Return statuses: ")
        print("               0: Test passed")
        print("               1: 5 second timeout reached")
        print("               2: Test designed poorly and probably failed")
        print("Pass criteria: Successful ping, eg prints 0")
        child = pexpect.spawn('ping -c 1 130.236.179.84')
        print("Return status:")
        print(child.expect(["64 bytes from 130.236.179.84", pexpect.TIMEOUT, pexpect.EOF], 5))
        print("Test done.\n\n")
        
def testInternalHost3():
        print("Test ID:       INTERNAL-3")
        print("Purpose:       Test client-1 connectivity to server (internal) (no nameserver")
        print("SUT:           Client-1")
        print("Preconditions: eth0 configured correctly")
        print("Procedure:     Calling the following commands")
        print("               1. ping -c 1 130.236.179.82")
        print("Return statuses: ")
        print("               0: Test passed")
        print("               1: 5 second timeout reached")
        print("               2: Test designed poorly and probably failed")
        print("Pass criteria: Successful ping, eg prints 0")
        child = pexpect.spawn('ping -c 1 130.236.179.82')
        print("Return status:")
        print(child.expect(["64 bytes from 130.236.179.82", pexpect.TIMEOUT, pexpect.EOF], 5))
        print("Test done.\n\n")

def testClient1ToIdaGwCon():
        print("Test ID:       NET-1")
        print("Purpose:       Test client-1 connectivity with ida-gw (no nameserver")
        print("SUT:           Client-1")
        print("Preconditions: eth0 configured correctly and router properly setup")
        print("Procedure:     Calling the following commands")
        print("               1. ping -c 1 130.236.178.1")
        print("Return statuses: ")
        print("               0: Test passed")
        print("               1: 5 second timeout reached")
        print("               2: Test designed poorly and probably failed")
        print("Pass criteria: Successful ping, eg prints 0")
        child = pexpect.spawn('ping -c 1 130.236.178.1')
        print("Return status:")
        print(child.expect(["64 bytes from 130.236.178.1", pexpect.TIMEOUT, pexpect.EOF], 5))
        print("Test done.\n\n")

def testNameServer():
        print("Test ID:       NET-2")
        print("Purpose:       Test client-1 connectivity with ida-gw using nameserver")
        print("SUT:           client-1")
        print("Preconditions: eth0 configured correctly, router and nameserver properly setup")
        print("Procedure:     Calling the following commands")
        print("               1. ping -c 1 ida-gw.sysinst.ida.liu.se")
        print("Return statuses: ")
        print("               0: Test passed")
        print("               1: 30 second timeout reached")
        print("               2: Test designed poorly and probably failed")
        print("Pass criteria: Successful ping, eg prints 0")
        child = pexpect.spawn('ping -c 1 ida-gw.sysinst.ida.liu.se')
        print("Return status:")
        print(child.expect(["64 bytes from ida-gw.sysinst.ida.liu.se \(130.236.178.1\)", pexpect.TIMEOUT, pexpect.EOF], 30))
        print("Test done.\n\n")
       

def testPingOutsideHost():
        print("Test ID:       NET-3")
        print("Purpose:       Test client-1 connectivity to internet")
        print("SUT:           client-1")
        print("Preconditions: eth0 configured correctly, router and nameserver properly setup")
        print("Procedure:     Calling the following commands")
        print("               1. ping -c 1 www.google.com")
        print("Return statuses: ")
        print("               0: Test passed")
        print("               1: 30 second timeout reached")
        print("               2: Test designed poorly and probably failed")
        print("Pass criteria: Successful ping, eg prints 0")
        child = pexpect.spawn('ping -c 1 www.google.com')
        print("Return status:")
        print(child.expect(["64 bytes from", pexpect.TIMEOUT, pexpect.EOF], 30))
        print("Test done.\n\n")
       



testCheckClient1Ips()
time.sleep(2)
testHostname()
time.sleep(2)
testInternalHost1()
time.sleep(2)
testInternalHost2()
time.sleep(2)
testInternalHost3()
time.sleep(2)
testClient1ToIdaGwCon()
time.sleep(2)
testNameServer()
time.sleep(2)
testPingOutsideHost()
time.sleep(2)

