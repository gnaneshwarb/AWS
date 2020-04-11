#import the boto3  library to connect to the AWS service
import boto3
import playsound
import csv

#aws access key id and secret access key
with open('credential.csv','r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

#Region
region='us-east-2'

#Paste your text to convert it into speech
text='This AWS polly service (Text to speech conversion). text has been converted to speech'

#connect it into aws polly service
client = boto3.client('polly', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)
response = client.synthesize_speech(
    OutputFormat='mp3',
    Text=text,
    TextType='text',
    VoiceId='Matthew',
)

body = response['AudioStream'].read()
#saving audio file to your directory
file_name = 'voice.mp3'
with open(file_name, 'wb') as file:
    file.write(body)
    file.close()
    
playsound.playsound('voice.mp3', True)
