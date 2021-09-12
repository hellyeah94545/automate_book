# /usr/bin/env python3
# assignChores.py: Sends emails to participients in a list
# with provided list of chores, randomly selecting chores
import random
import smtplib

'''
# analysis
## Inputs: [] of email address, [] of chores

# 1. Randomly assign chores to email address
# 2. Send out email to participants with assigned chore

to do:

1. Loop through list of email address
2. Assign one chore to each email address with random.choice. save in dictionary
3. Remove chore from chore lists
4. ?Stop is no more chores are left
5. send email to each person

'''

persons = ['hellyeah94545@yahoo.com', 'wife@example.com', 'kid1@example.com', 'kid2@example.com']
chores = ['dishes', 'bathroom', 'vacuum', 'mop']
chore_assignment = {}

for email in persons:
    chore = random.choice(chores)
    chore_assignment[email] = chore
    chores.remove(chore)

# send email
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'hellyeah94545@gmail.com'
sender_password = input("Enter password: ")
e_mailer = smtplib.SMTP(smtp_server, smtp_port)
e_mailer.ehlo()
e_mailer.starttls()
e_mailer.login(sender_email, sender_password)

for email, chore in chore_assignment.items():
    body = "Subject: Your chore for this week is: {0} ." \
           " \n\n Subject: Your chore for this week is: {0}\n\nThank you!".format(chore)
    send_mail_status = e_mailer.sendmail(sender_email, email, body)
    if send_mail_status != {}:
        print('There was a problem send email to {0}: {1}'.format(email, send_mail_status))
    print("sent email to %s" % email)
e_mailer.close()
