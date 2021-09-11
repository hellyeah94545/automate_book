#! /usr/bin/env python3
# sendReminders.py: scripts to send past due email reminders


import sys
import openpyxl
import smtplib


datafile = 'duesRecords.xlsx'
workbook = openpyxl.load_workbook(datafile)
sheet = workbook['Sheet1']

last_column = sheet.max_column
last_row = sheet.max_row
latest_month = sheet.cell(row=1, column=last_column).value

# TODO: Check each member's payment status
unpaid_members = {}
for user in range(2, last_row + 1):
    payment = sheet.cell(row=user, column=latest_month).value.lower()
    if payment != "paid":
        for month in range(2, last_column):
            if sheet.cell(row=user, column=month).value.lower() != "paid":
                unpaid_members[sheet.cell(row=user, column=1).value] = sheet.cell(row=1, colume=month)




unpaid_members = {}

# TODO: Log in to email account
# TODO: Send out reminder emails
