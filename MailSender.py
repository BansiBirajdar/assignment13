'''This module the send the mail form the user'''
import time
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


#send(filename,sys.argv[2],scannfile_count,D_count,Starting_time)
def Send(filename,toaddr,scannfile_count,D_count,Starting_time):
    try:
        fromaddr = "bansiddha7@gmail.com"
        
        msg = MIMEMultipart()
        
        msg['From'] = fromaddr
        
        msg['To'] = toaddr
        
        body ="""
        Hello %s
        Welcome To Marvellour Infosystems.
        Please find attached document which contains 
        Log of Running Process.
        Log file is Created at :%s
        Stating time of scanning:%s
        Total number of files scanned:%s
        Total numberr of duplicate file fountd:%s
        This is auto Gennerated Mail.
        
        Thanks & Regards,
        Bansiddha Chadrakant Birajdar
        Gmail:%s
        Student of Marvellour Infosystems
        """%(toaddr,time.time(),Starting_time,scannfile_count,D_count,fromaddr)
        
        Subject="""
        Marvellous Infosystem Process log Generated at:%s
        """%(time.time())
        
        msg['Subject'] =Subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        attachment = open(filename, "rb")
        
        p = MIMEBase('application', 'octet-stream')
        
        p.set_payload((attachment).read())
        
        encoders.encode_base64(p)
        
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
        msg.attach(p) 

        s = smtplib.SMTP('smtp.gmail.com', 587) 

        s.starttls() 

        s.login(fromaddr, "9049******") 

        text = msg.as_string() 

        s.sendmail(fromaddr, toaddr, text) 

        s.quit()
        
        print("Log file successfully sent through Mail")
    except Exception as E:
        print("Unable to send mail.",E)