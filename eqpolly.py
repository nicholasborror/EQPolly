
########################## YOU NEED THESE TO RUN EQPOLLY ##########################
#pip install boto3, pygamer

#Turn off pygame hello
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
import time 
from pygame import mixer  # Load the popular external library
import csv #we are going to try to import voice rules via CSV

# Set the region
os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'


# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (%userprofile%\.aws\credentials).
#EXAMPLE
#[default]
#aws_access_key_id = XXXXXXX
#aws_secret_access_key = YYYYYYYYYYYYYYY

session = Session(profile_name="default")
polly = session.client("polly")

#Define the function we call with the voice name, text to say, and where to save it.
def speaktome(speaker, say, output):
    
    args = [speaker,say,output]
    print(args)
    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Text=say, OutputFormat="mp3", VoiceId=speaker)
        #debug nb
        print("the response is %s" % response)
        
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    # Access the audio stream from the response
    if "AudioStream" in response:
        # Note: Closing the stream is important because the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
            with closing(response['AudioStream']) as stream, open(output, 'wb') as file:
                while data := stream.read():
                    file.write(data)


    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

    # Play the audio using pygame
    mixer.init()
    mixer.music.load(output)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)
    mixer.music.stop()
    mixer.stop()
    mixer.quit()

#File parser function
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def convert_row( row ): #convert the rows of the speakers into ASCII as UTF, notepad++, and Excel give issues.
    row_dict = {}
    for key, value in row.items():
        keyAscii = key.encode('ascii', 'ignore' ).decode()
        valueAscii = value.encode('ascii','ignore').decode()
        row_dict[ keyAscii ] = valueAscii
    return row_dict

#Main
if __name__ == '__main__':
    logfilepath = (sys.argv[1])
    speechlist = (sys.argv[2])

    logfile = open(logfilepath,"r")
    loglines = follow(logfile)
    for line in loglines:
        print (line)
        #if ("test123" in line):
        with open(speechlist) as c: #This CSV should contain the speakers name to recognize in the file, along with the cooresponding voice
            r = csv.DictReader(c)
            for row in r:
                #print(row['VOICE'], row['NAME'])
                #time.sleep(1)
                
                if (row['NAME'] in line):
                    print(row['NAME'])
                    if ("says" in line):
                        #spl_word = '2021] ' #Says the speakers name
                        spl_word = "says, '"
                        leftover = line.partition(spl_word)[2]
                        speaktome(row['VOICE'], leftover, "voice.mp3")
                        #print(row['NAME'], row['VOICE'])
                        break
                        

