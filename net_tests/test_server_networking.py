#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pexpect
import time
import re

'''***********
***GW TESTS***
***********'''

def testCheckServerIps():
        print("Test ID:       HOSTNAME-1")
        print("Purpose:       Check server IP")
        print("SUT:           Server")
        print("Preconditions: Basic configuration")
        print("Procedure:     Check ip's and make sure that they are correct.")
        print("Return statuses: ")
        print("               0: Test passed")
        print("               1: Test failed")
        print("Pass criteria: Successful hostname set.")
        child = pexpect.spawn('hostname --all-ip-addresses')
        print("Return status:")
        print(child.expect(["130.236.179.82", pexpect.EOF]))
        print("Test done.\n\n")

def testHostname():
        print("Test ID:       HOSTNAME-2")
        print("Purpose:       Test server hostname")
        print("SUT:           server")
        print("Preconditions: Basic configuration")
        print("Procedure:     Cat /etc/hostname to see if it is correctly set.")
        print("Return statuses: ")
        print("               0: Test passed")
        print("               1: Test failed")
        print("Pass criteria: Successful hostname set.")
        child = pexpect.spawn('hostname')
        print("Return status:")
        print(child.expect(["server", pexpect.EOF]))
        print("Test done.\n\n")
        
def testInternalHost1():
        print("Test ID:       INTERNAL-1")
        print("Purpose:       Test server connection to gw (no nameserver")
        print("SUT:           server")
        print("Preconditions: eth0 configured correctly")
        print("Procedure:     Calling the following commands")
        print("               1. ping -c 1 130.236.179.81")
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
        print("Purpose:       Test server connectivity to client-2 (no nameserver")
        print("SUT:           server")
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
        print("Purpose:       Test server connectivity to gw (internal) (no nameserver")
        print("SUT:           server")
        print("Preconditions: eth0 configured correctly")
        print("Procedure:     Calling the following commands")
        print("               1. ping -c 1 130.236.179.81")
        print("Return statuses: ")
        print("               0: Test passed")
        print("               1: 5 second timeout reached")
        print("               2: Test designed poorly and probably failed")
        print("Pass criteria: Successful ping, eg prints 0")
        child = pexpect.spawn('ping -c 1 130.236.179.81')
        print("Return status:")
        print(child.expect(["64 bytes from 130.236.179.81", pexpect.TIMEOUT, pexpect.EOF], 5))
        print("Test done.\n\n")

def testServerToIdaGwCon():
        print("Test ID:       NET-1")
        print("Purpose:       Test server connectivity with ida-gw (no nameserver")
        print("SUT:           server")
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
        print("Purpose:       Test server connectivity with ida-gw using nameserver")
        print("SUT:           server")
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
        print(child.expect(["64 bytes from ida-gw.sysinst.ida.liu.se \(130.236.178.1\)", pexpect.TIMEOUT, pexpect.EOF],30))
        print("Test done.\n\n")
       

def pingOutsideHost():
        print("Test ID:       NET-3")
        print("Purpose:       Test server connectivity to internet")
        print("SUT:           server")
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
       



testCheckServerIps()
time.sleep(2)
testHostname()
time.sleep(2)
testInternalHost1()
time.sleep(2)
testInternalHost2()
time.sleep(2)
testInternalhost3()
time.sleep(2)
testServerToIdaGwCon()
time.sleep(2)
testNameServer()
time.sleep(2)
pingOutsideHost()
time.sleep(2)

