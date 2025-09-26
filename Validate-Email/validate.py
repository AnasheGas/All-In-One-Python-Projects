#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Aman Kumar
# Version: 1.0.0 

import re

email_conditions = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
user_email = input("Enter your email: ")

isValid = re.search(email_conditions, user_email)

if(isValid):
    print("Valid Email")
    if "@gmail" in user_email:
        print("you dirty googler")
    elif  "@yahoo" in user_email:
        print("you dirty yahooer")
    else:
        print("U got a weird email")

else:
    print("Invalid Email")


