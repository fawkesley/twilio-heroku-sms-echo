import logging

from flask import Flask, request


app = Flask(__name__)


@app.route('/sms/')
def sms_echo():
    # https://github.com/twilio/twilio-python#api-credentials

    sms_body = request.args.get('Body')
    app.logger.info('body: `{}`'.format(sms_body))

    if sms_body is None:
        app.logger.warning('Null SMS body.')
        return 'Bad request from Twilio client.'
    else:
        return ('<?xml version="1.0" encoding="UTF-8" ?>'
                '<Response>'
                '<Message>{}</Message>'
                '</Response>'.format(sms_body))


if __name__ == "__main__":  # Running eg `python server.py`
    app.run(debug=True)

else:  # Running in Foreman / heroku
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)
