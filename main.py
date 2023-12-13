from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
import sys
from pdfminer.high_level import extract_text

text = extract_text('media/the_raven_short.pdf')

session = Session(profile_name="adminuser")
polly = session.client("polly")

try:
    # Request speech synthesis
    response = polly.synthesize_speech(Text=text,
                                       OutputFormat="mp3",
                                       VoiceId="Brian")
except (BotoCoreError, ClientError) as error:
    # The service returned an error, exit gracefully
    print(error)
    sys.exit(-1)

file = open('media/the_raven.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()
