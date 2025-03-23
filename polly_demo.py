import boto3

# Create a Polly client (ensure the region matches what you set with aws configure)
polly = boto3.client('polly', region_name='us-east-1')

# Synthesize speech using a youthful female voice "Ivy"
response = polly.synthesize_speech(
    Text="Hello, I am Ivy, your SunnyDoll assistant. How's your day going?",
    OutputFormat="mp3",
    VoiceId="Ivy"
)

# Save the synthesized audio to output.mp3
with open("output.mp3", "wb") as file:
    file.write(response['AudioStream'].read())

print("Audio file saved as output.mp3")
