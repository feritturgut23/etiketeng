<div align="center">
<h1>Miku-MentionAll_Bot Manually Deploy via Heroku Github Actions</h1>
<h3>This page will tell you how to deploy Miku-MentionAll_Bot to heroku on Github Actions</h3><i><b>(This is for Developers.. If You are not, Deploy Bot using Heroku Deploy URL)</b></i>
</div>

#### Steps

🎈1. **Fork this Repo**

🎈2. **Go to Repository `Settings` -> `Secrets`**
    ![Secrets](assets/step-01.jpg)
    
🎈3. **Now set the below Variables in the Github Repository Secrets**
    [Environmental Variables](#environment-variables)![Secrets](assets/step-02.jpg)   
    
🎈4. **After filling the Required vars .... go to Actions and then tap on Run the Workflow**
    ![Actions](assets/step-03.jpg)   

🎉5. **now wait it for it to deployed to heroku and Check app logs and Turn on Workers If OFF** **if everything is OK then send /start to the bot or try other cmds**...


## Environment Variables

### 🔴Required Environmental Variables... MUST BE GIVEN....

| Variable | Value | Example | Required | Description |
| :---: | :---: | :---: | :---: | :---: |
| HEROKU_EMAIL | Heroku email | abc@abc.com | True | Just Give the email you used for Heroku Account|
| HEROKU_API_KEY | Heroku API key | xxxxxxx-xxxx-xxxx-xxxx-xxxxxx | True | Get it from [Heroku](https://dashboard.heroku.com/account/applications/authorizations/new) |
| HEROKU_APP_NAME | Heroku app name | Name Must be unique | True | Heroku app name that needs to be Updated or Created (Should be in lowercase) |
| TOKEN | Telegram Bot Token | your telegram bot api key/token | True | Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the  API token. |
| APP_ID | Telegram API_ID | Your TG account's API_ID | True | Get this value from [TELEGRAM](https://my.telegram.org/apps). |
| API_HASH | Telegram API_HASH | Your TG account's API_HASH | True | Get this value from [TELEGRAM](https://my.telegram.org/apps). |
