# Twitter Bot (no Developer API)

Run your own Twitter bot without any programming knowledge or API keys

## Getting Started

These instructions are for non-developers. If you want to build on top of this bot, continue down to 'Extending'.

### Computer Requirements
Any machine running Python can execute run.py via command line. Compiled versions are available for the following operating systems:

* OSX
  * 64 bit
* x86_64
  * Ubuntu Bionic Beaver

### Initial Setup

* First, make an account on [IFTT](https://ifttt.com/applets/KhYNACJF-emailtotweet)

* Once signed up, go to [my app](https://ifttt.com/applets/KhYNACJF-emailtotweet) and turn it on.
  * You will be asked to connect a Twitter and email. Be sure to use your 'bot' accounts. I would suggest making a new email..
  * There is no need to alter the IFTTT applet settings once turned on.

* Next click the green 'Clone or download' button above and unzip the contents.

* Open the folder for your machine ('OS', 'WINDOWS', ect) and move the run file to the main directory
  * If there is not a distribution for your machine, check below for command line instructions

* Be sure to scroll down to the 'Troubleshooting' section if you experience issues, it is likely your Gmail security settings

* After setting up the config (explained below), simply double click the 'run' file to start the bot

If an executable distribution is not available for your machine run:
```
python run.py
```


### Configuration

To configure the bot, open the resources folder and open 'properties.ini' with a text editor. Below is an explanation for each of the properties.

[main]

You will need to put your email and password in the config for the bot to work
* Email : the email address you registered with the IFTTT applet
* EmailPassword : your email password

These properties are safe to alter, however, setting the frequency too low will get your Twitter account banned
* FreqMins : the amount of time between each Tweet 
* Loop : set to False if you want the bot to stop after iterating tweet list
* Debug : when True, no Tweets will be sent

If you are using gmail and kept the default IFTTT fields you will not need to alter these properties
* TriggerHashtag : should be the same as 'hashtag' field on IFTTT applet
* TriggerEmail : the email address that triggers the IFTTT applet (I don't think this can change)
* EmailServer : the smtp server to send mail (default is Google)
* EmailServerPort : the smtp server port (default is Gmail)

[txt]
* file : name or directory of text file containing tweets in resources

[dev]

Changing the 'dev' properties will break the bot unless you have altered the code to support the change
* RequiredProps : the properties BotConfig.py will look for on startup
* Zone : the properties section to use

### Schedule Tweets

In the resources directory, there is an example 'tweets.txt' demonstrating how to format Tweets. The import thing to keep 
in mind is that you need to end each Tweet with aa semi-colon. You can make multiple text files of tweets just be sure to 
pass the correct file to the bot on startup.

Here are a few examples of 'tweets.txt' sytanx...

* The following two examples will produce the same results
```
I love Twitter; You love Twitter; We love Twitter;
```
```
I love Twitter;
You love Twitter;
We love Twitter;
```

* Tweets can contain newline characters
```
This is 

one Tweet

still;
```

## Troubleshooting
If your bot's console is not reporting errors but Tweets are not sending, it is likely a Google security issue. You can confirm this by going to the IFTTT applet, clicking configure, and viewing the activity log. The steps below should fix this.

* Visit Google's [security settings](https://myaccount.google.com/security?pli=1#connectedapps) and turn on 'Less secure app access'

* Go to Gmail's settings, navigate to the 'Forwarding/IMAP' tab and turn on enable IMAP Access

If you are getting errors in the console, make sure your properties file is setup correctly. If problems persist please contact me with your error message.

## Extending
I did my best to make it easy to build your own bot on top of this application. To see an example of how I have extended this bot, checkout my [Wikipedia Twitter Bot.](https://github.com/JackPhallen/WikiTwitterBot)

### Creating Modules

The program uses what I am calling 'modules' to fetch content to tweet. This bot uses a module called 'txt' located in 'BotModules/txt/txt' to pull tweets from a text file. To create your own module the pattern is simple. 

* Create a py file for your module in 'BotModules/txt/txt' 
* Each module is required to have two functions, init and get
  * init takes a parserconfig object as an argument and should set important global variables for the module
  * get returns a list of tweets
* Next open 'mods.py' and put refrences to your init and get functions inside the respected dictionary

### Configuring Modules

In order for the bot to run your custom module, you need add it to the configuration. First, open your properties file and add your module name under the dev section. Do not put spaces between module names!
```
[dev]
Modules = txt,module1,module2
```
Next create a new config section with your module name and add any properties you want to be passed to your init function. You must create a new section even if your module does not require properties to run
```
[module1]
Database = /resources/db
DatabasePass = mypassword
.
.
```
That's it! Your bot will now fetch tweets from your custom module! If you no longer want a module to run, simply remove it from the 'Modules' property under '[dev]'

  



# Changelog

Notable commits to master branch will be logged here

### 2019-07-09
- Enable debug from properties

### 2019-06-25
- Implemented 'module' system so new Tweet sources can be easily added
- Removed command line prompts and replaced with properties for each 'module'

### 2019-06-24
- OSX executable
