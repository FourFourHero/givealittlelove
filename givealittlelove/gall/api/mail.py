import logging

from django.core.mail import EmailMultiAlternatives
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

def send_coupon_mail(ambassador, activation, coupon):
    subject = 'GALL TEST A little love from American Greetings!'
    from_email = 'aschulak@gmail.com'
    to = activation.email
    coupon_url = 'http://www.givealittlelove.ag/coupon/' + coupon.code
    text_content = coupon_text_template % (activation.name, coupon_url, ambassador.name)
    html_content = coupon_html_template % (activation.name, coupon_url, ambassador.name)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
