# SMS Echo Server with Twilio and Heroku

Once deployed, any SMS message sent to your Twilio number will be echoed right
back to you.

## Setup

0. Clone this repo: `git clone https://github.com/paulfurley/twilio-heroku-sms-echo`
1. [Create a new app](https://dashboard-next.heroku.com/new) on Heroku
2. Follow Heroku instructions to add a new git remote `heroku`
3. Deploy to heroku

    ```
    export APP_NAME=<your-app-name>

    git push heroku master
    heroku ps:scale web=1
    ```
4. Configure Twilio messaging to point to `https://<your-app-name>.herokuapp.com/sms/`
5. Send SMS to your Twilio number.
6. Receive SMS reply!
