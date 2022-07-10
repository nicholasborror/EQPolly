# EQPolly
Add voiceovers to NPC's in Everquest using AWS's Polly system.  See ExampleVideo.mp4 for a preview.

This python script uses the free tier of Amazon's Polly TTS (Text To Speech) system to parse the logs of Everquest NPC interactions and play an output as they speak.  Each gender and race have been given a specific Amazon Polly voice as shown in the file voice_table.txt.  

Disclaimer:  This was a trial by fire project and my first relativly useful Python script, and my first time really working with AWS, so I am sure there are many improvements that can be made.  I stopped working to improve the script once it was working reliably.

Requirements:

Only tested on Windows Python 3.10

pipwin (used to install pyaudio precompiled binaries)

pyaudio

pygamer

boto3

AWS account (free tier works just fine)


Setup:

Copy the EQPOLLY folder to C:\EQPOLLY or wherever you want it.

Setup an AWS account and log in.

Go to the IAM service and create an addional user (e.g. polly_user).  

Create a new user group (e.g. polly_group) and then give it the permission "AmazonPollyFullAccess".

Edit the polly_user and add it to the group polly_group.  Now the user polly_user can use the polly service.

You will need security credentials for the script to access your AWS account.  Under the properties of polly_user, select the security credentials tab and create an access key.  

Create a a folder named .aws in %userprofile%
Create a file in %userprofile%\.aws\credentials with your access key information in this format:

[default]

aws_access_key_id = XXXXXXX

aws_secret_access_key = YYYYYYYYYYYYYYY



Install the prerequesites:

pip install boto3, pygamer, pipwin

pipwin install pyaudio (at the time of script creation, pyaudio wasn't in the repositories for Python 3.10, so I used precompiled binaries using pipwin)


Log into Everquest and make sure logging is turned on by using the command /log on

Go into your Everquest folder, and under the logs folder, you should see a file named eqlog_yourcharactername_servername.txt.  Make note of the path of this file, as you will need it to start the script.

Run Python %pathtoEQPolly.py% %pathtoeqpollyvoices.csv% %pathtoeqlog_yourcharactername_servername.txt%

For example--

python C:\EQPOLLY\eqpolly.py C:\GAMES\EVERQUEST\LOGS\eqlog_user_agnarr.txt C:\EQPOLLY\eqpollyvoices.csv

Go to a merchant or hail an NPC that say's text, and you will hear a voiceover for their text, based on their gender and race.  If you want to make any changes to the voices used for a particular NPC, or if want to add a NPC that isn't already defined, edit file eqpollyvoices.csv and add the appropriate fields.  So far, over 14800 NPC's have been designated a voice based on their race and gender.  


