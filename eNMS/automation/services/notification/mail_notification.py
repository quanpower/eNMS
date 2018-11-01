from flask_mail import Message
from netmiko import file_transfer
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String


from eNMS.automation.models import Service
from eNMS.base.models import service_classes


class MailNotificationService(Service):

    __tablename__ = 'MailNotificationService'

    id = Column(Integer, ForeignKey('Service.id'), primary_key=True)
    title = Column(String)
    sender = Column(String)
    recipients = Column(String)
    body = Column(String)
    body_textarea = True
    multiprocessing = False

    __mapper_args__ = {
        'polymorphic_identity': 'mail_notification_service',
    }

    def job(self, payload):
        message = Message(
            self.title,
            sender=self.sender,
            recipients=self.recipients.split(','),
            body=self.body
        )
        mail.send(message)
        return {'success': True, 'result': message}


service_classes['mail_notification_service'] = MailNotificationService