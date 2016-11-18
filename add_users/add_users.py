#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#import pexpect
#import time
#import re


def generateUsername(name):
    """Generates a unique username"""
    name = name.lower()
    namelist = name.split()
    firstPart = namelist[0][:3] + namelist[-1][:2]
    print(firstPart)

def addUser(fullname):
    username = generateUsername(fullname)

def createUsers():
    f = open('users.txt', 'r')
    lines = [line.strip('\n') for line in open('users.txt', 'r')]

    for line in lines:
        addUser(line)


createUsers();
    





