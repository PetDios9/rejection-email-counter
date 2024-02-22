import imaplib
import email
from dotenv import load_dotenv

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('email', 'password')

status, messages = mail.select("inbox") # connect to inbox.
result, data = mail.search(None, "ALL")
 
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest
 
result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
raw_email = data[0][1] # here's the body, which is raw text of the whole email
search = mail.search(None, '(BODY "with other candidates")')
decoded_search = search[1][0].decode("utf-8")
print(len(decoded_search.split(' ')))
