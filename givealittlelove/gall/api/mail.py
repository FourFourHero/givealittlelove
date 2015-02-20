import logging

from django.core.mail import EmailMultiAlternatives
from givealittlelove.gall.mail.ambassador import text_template as ambassador_welcome_text_template
from givealittlelove.gall.mail.ambassador import html_template as ambassador_welcome_html_template
from givealittlelove.gall.mail.coupon import text_template as coupon_text_template
from givealittlelove.gall.mail.coupon import html_template as coupon_html_template

logger = logging.getLogger(__name__)

def send_test_mail():
    subject, from_email, to = 'GALL Test', 'aschulak@ag.com', 'aschulak@gmail.com'
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_ambassador_welcome_mail(ambassador):
    subject = 'Welcome to the Happiness, Laughter and Love Ambassador Program!'
    from_email = 'welcome@givealittlelove.ag'
    to = ambassador.email
    text_content = ambassador_welcome_text_template % (ambassador.name, ambassador.code)
    html_content = ambassador_welcome_html_template % (ambassador.name, ambassador.code)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_coupon_mail(ambassador, last_activation, activation, coupon):
    subject = "A little love for paying it forward"
    from_email = 'thankyou@givealittlelove.ag'
    to = activation.email
    text_content = coupon_text_template % (last_activation.name, activation.name, coupon.code, ambassador.name)
    html_content = coupon_html_template % (last_activation.name, activation.name, coupon.code, ambassador.name)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    #msg.send()
