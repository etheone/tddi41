#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pexpect
import time
import re


def testNfs1():
    print("Test ID:       Nfs test - NFS")
    print("Purpose:       Check NFS")
    print("SUT:           Client-2")
    print("Preconditions: Network, nis nfs and autofs configured properly")
    print("Procedure:     Run ls -l /home} to see if we have mounted a users homedir")
    print("Return statuses: ")
    print("               0: Test passed")
    print("               1: Test failed")
    print("Pass criteria: We have mounted the users home dir from the nfs server and have the proper rights")
    child = pexpect.spawn('ls -l /home')
    print("Return status:")
    print(child.expect(["drwx------ 2 test1 test1", pexpect.EOF]))
    print("Test done.\n\n")


testNfs1()

