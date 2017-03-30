# Something in lines of http://stackoverflow.com/questions/348630/how-can-i-download-all-emails-with-attachments-from-gmail
# Make sure you have IMAP enabled in your gmail settings.
# Right now it won't download same file name twice even if their contents are different.
#https://gist.github.com/baali/2633554
import email
import datetime
import getpass, imaplib
import os
import sys

detach_dir = '.'
if 'attachments' not in os.listdir(detach_dir):
    os.mkdir('attachments')

userName = raw_input('Enter your GMail username:')
passwd = getpass.getpass('Enter your password: ')

try:
    imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
    typ, accountDetails = imapSession.login(userName, passwd)
    if typ != 'OK':
        print 'Not able to sign in!'
        raise
    
    imapSession.select('[Gmail]/All Mail')
    typ, data = imapSession.search(None, '(FROM "pranav.silimkhan@gmail.com")')
    if typ != 'OK':
        print 'Error searching Inbox.'
        raise
    
    # Iterating over all emails
    for msgId in data[0].split():
        typ, messageParts = imapSession.fetch(msgId, '(RFC822)')

        if typ != 'OK':
            print 'Error fetching mail.'
            raise
        print('Message %s\n' % (messageParts[0][1]))
        output_file = open('email.txt', 'w')
        output_file.write('Message %s\n' % ( messageParts[0][1]))
        output_file.close()
        emailBody = messageParts[0][1]
        mail = email.message_from_string(emailBody)
        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                # print part.as_string()
                continue
            if part.get('Content-Disposition') is None:
                # print part.as_string()
                continue
            fileName = part.get_filename()

            if bool(fileName):
                filePath = os.path.join(detach_dir, 'attachments', fileName)
                if not os.path.isfile(filePath) :
                    print fileName
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
    """typ, messageParts = M.fetch(msgId, '(RFC822)')
    print('Message %s\n' % (messageParts[0][1]))
    output_file = open('email.txt', 'w')
    output_file.write('Message %s\n' % ( messageParts[0][1]))
    output_file.close()"""
            
except :
    print 'Not able to download all attachments.'