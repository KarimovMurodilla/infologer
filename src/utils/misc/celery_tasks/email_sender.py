from celery import Celery

from utils.misc.sender import Email
from ..redis_instance import redis_cache

from config import REDIS_HOST, REDIS_PORT

celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')


def generate_email_text_part_template(first_name: str, code: int):
    text_part = (
        f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Email Verification Code</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }}

                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #ffffff;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    margin-top: 20px;
                }}

                h2 {{
                    color: #333333;
                }}

                p {{
                    color: #666666;
                }}

                .verification-code {{
                    font-size: 24px;
                    font-weight: bold;
                    color: #007bff;
                    margin-top: 10px;
                    margin-bottom: 20px;
                }}

                .footer {{
                    text-align: center;
                    margin-top: 20px;
                    color: #999999;
                }}
            </style>
        </head>
        <body>

        <div class="container">
            <h2>Email Verification Code</h2>
            <p>Dear {first_name},</p>
            <p>Your verification code is:</p>
            <div class="verification-code">{code}</div>
            <p>This code will expire in 10 minutes.</p>
            <p>If you didn't request this code, please ignore this email.</p>
            <p>Thank you!</p>
            <div class="footer">
                <p>This is an automated email, please do not reply.</p>
            </div>
        </div>

        </body>
        </html>
"""
    )    

    return text_part


@celery.task
def send_verify_code_to_email(first_name: str, email: str, code: int):
    email_obj = Email()

    save_to_cache(email, code)
    text_part = generate_email_text_part_template(first_name, code)

    email_obj.send_mail(
        subject="Email Verification",
        text_part=text_part,
        to_email=email
    )


def save_to_cache(email, code):
    redis_cache.set(name=email, value=code, ex=600)


def email_verification_is_successful(email, code):
    sended_code = int(redis_cache.get(email)) if redis_cache.get(email) else 0

    return code == sended_code



# celery -A utils.misc.celery_tasks.email_sender:celery worker --loglevel=INFO