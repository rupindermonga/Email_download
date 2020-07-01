import imaplib #to install IMAP a standard email protocol that stores email messages on a mail server
import base64 #encoding and decoding of binary data to ASCII characters or vice versa
import os #to manipulate local directories
import email #to read, write and send emails
import getpass #to get password as hidden


target_path = '/media/rupinder/New Volume/Personal/Learning/My Projects/Email Download/'
email_user = input("Email: ")


email_pass = getpass.getpass() #It will help get hidden password

port = 993 #Standard port for IMAP4_SSL
host_address = "imap.gmail.com" #for gmail

mail = imaplib.IMAP4_SSL(host_address,port) #made connection with the host over an SSL encrypted socket

mail.login(email_user,email_pass) #Full access to the said email

mail.select("Inbox") #Select the folder


typ, msgs = mail.search(None, '(UNSEEN SUBJECT "your text")') #search for specific subject

mail_ids = msgs[0]
id_list = mail_ids.split()


for eachid in id_list:
    resp, data = mail.fetch(eachid,  '(RFC822)')
    emailBody = data[0][1]
    new_mail = email.message_from_bytes(emailBody) #for newer version
    # new_mail = email.message_from_string(emailBody) #for older version
    for part in new_mail.walk():
        #not using for this download
        # if part.get_content_maintype() == 'multipart':
        #     # print part.as_string()
        #     continue
        # if part.get('Content-Disposition') is None:
        #     # print part.as_string()
        #     continue
        fileName = part.get_filename()
        if fileName is not None:
            fileName = fileName.split("//")[-1]
        # print(fileName)
        # print(fileName)
        if bool(fileName):
            filePath = os.path.join(target_path, fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
mail.close()
mail.logout()





