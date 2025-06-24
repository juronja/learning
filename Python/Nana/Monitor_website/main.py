import requests
import smtplib
import os
import paramiko

app_ip = "64.226.72.236"
app_port = "8080"
GMAIL_USER = os.environ.get("GMAIL_USER")
GMAIL_PASS = os.environ.get("GMAIL_PASS")
SSH_KEY_PATH = os.path.expanduser("~/.ssh/id_k8s")


def send_email(email_msg):
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(GMAIL_USER, GMAIL_PASS)  # Google app password
        smtp.sendmail(GMAIL_USER, "jure.repina.work@gmail.com", email_msg)


try:
    response = requests.get(f"http://{app_ip}:{app_port}")
    if response.status_code == 200:
        print("App is accessible the request succeeded")
    else:
        print(f"App is returning status code: {response.status_code}")
        # send email
        send_email(f"Subject: Site problems\nApp is returning status code: {response.status_code}\nPlease investigate.")
except Exception as e:
    print(f"There was an error:\n{e}")
    send_email(f"Subject: Site is DOWN\nThere was an error:\n{e}\n\nFix the issue.")

    # Restart docker container
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=app_ip, username="root", key_filename=SSH_KEY_PATH)
    stdin, stdout, stderr = client.exec_command("docker start my-nginx")
    print(stdout.readlines())
    client.close()



