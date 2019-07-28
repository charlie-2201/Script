import smtplib
import csv
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
cr = csv.reader(open(r".csv file"))
arr = []
a=r'file path leaving filename and end with \\'
for row in cr:
    arr.append(row)
for x in range(1,len(arr)):
    i=arr[x][0]
    j=arr[x][1]
    img = Image.open(r"template file path") #used to select the template file
    draw = ImageDraw.Draw(img)
    selectFont = ImageFont.truetype("font name.ttf", 60)
    #used to do changes on the img where 'i' is used for adding text at particulr coordinates
    draw.text((cordinates(x,y)), i, (r,g,b), font=selectFont) 
    w=a+i+".extesion"
    img.save(w)
    #write the sender's email address
    fromaddr = "sender email address"
    toaddr = j
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    # subject to be written on gmail account
    msg['Subject'] = "Subject to be written"
    body = "body of the email"
    msg.attach(MIMEText(body, 'plain')) 
    filename = i+".extension"
    attachment = open(w, 'rb') 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    # write the password of sender's email address
    s.login(fromaddr, "sender password") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit() 