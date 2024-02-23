import imaplib
import email

EMAIL_ADDRESS = input("What is your email address?: ")
PASSWORD = input("What is your password?: ")
IMAP = input("What is your IMAP server? (if unsure, google your email host + imap to find out): ")
LIMITER = int(input("Enter the number of last recieved emails you would like to check. This is optional. If nothing is entered, every email in your inbox will be checked. This could take some time.: ")) 
PHRASES = ['unfortunately', 'move forward with other candidates', 'not to move forward', 'will not be moving forward']

mail = imaplib.IMAP4_SSL(IMAP)
mail.login(EMAIL_ADDRESS, PASSWORD)

status, messages = mail.select("inbox") # connect to inbox.
result, data = mail.search(None, "ALL")
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
if LIMITER: 
        id_list = id_list[-LIMITER:]
counter = 0
 

print('counting your rejections...')
print('#################################')
for ids in id_list:
    result, data = mail.fetch(ids, "(RFC822)")
    if result == 'OK': 
        email_message = email.message_from_bytes(data[0][1])
        b = email_message 
        body = ""

        if b.is_multipart():
            for part in b.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))

                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    body = part.get_payload(decode=True)  # decode
                    break
        else:
            body = b.get_payload(decode=True)

        for phrase in PHRASES:
            if phrase in str(body).lower():
                counter += 1
                break
print(f"Heres how many times a job has rejected you: {counter}")
                