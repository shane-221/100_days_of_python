import smtplib
import glob
import os



class email:
    def __init__(self):
        self.to_email =""
        self.from_email = ""
        self.password =""
        self.location =""
        self.host =""

    def latest_output_file(self):
        list_of_files = glob.glob('../output_emails/*')
        latest_file = max(list_of_files, key=os.path.getmtime)      # From Stack overflow Pulls the file path of the most recent file
        with open(latest_file,'r') as f:
            contents =f.read()
            return contents


    def send_email(self):
            # Connects the smtplib client session to the host
        connection = smtplib.SMTP(self.host)#
            # message is encrypted
        connection.starttls()
            #Login phase
        connection.login(user=self.from_email, password =self.password)
            # Sending email
        connection.sendmail(from_addr=self.from_email,
                            to_addrs=self.to_email,
                            msg=self.latest_output_file()
                            )
            # Close the connection
        connection.close()





