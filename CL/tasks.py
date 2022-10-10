# from django.contrib.auth import get_user_model
# from celery.utils.log import get_task_logger
from __future__ import print_function
from celery import shared_task
from sendgrid.helpers.mail import *


@shared_task (bind=True)
def test(self):
    for i in range(5):
        print('he')
    return "done"

@shared_task(bind=True)
def send_mail(self):
    
    import sendgrid

    sg = sendgrid.SendGridAPIClient(api_key='API TOKEN')
    from_email = Email("ankur.thakur1020@gmail.com")
    to_email = To("ankur.thakur1020@gmail.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

@shared_task(bind=True)
def api_mail(self):
    import requests
    import sendgrid

    url = "	https://api.coindesk.com/v1/bpi/currentprice.json"

    response = requests.get(url)

    # print(response.status_code)
    data = response.json()
    # print(type(data))
    time = data["time"]
    chart = data["bpi"]
    usd = chart["USD"]
    gbp = chart["GBP"]
    eur = chart["EUR"]
    output = f'{time} \n{usd} \n{gbp} \n{eur}'

    sg = sendgrid.SendGridAPIClient(api_key='API TOKEN')
    from_email = Email("ankur.thakur1020@gmail.com")
    to_email = To("ankur.thakur1020@gmail.com")
    subject = "Bit coin"
    content = Content("text/plain",output)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


