import azure.cognitiveservices.speech as speechsdk

azure_key = "ENTER YOUR KEY"
azure_location = "ENTER YOUR LOCATION"
text_file = "Shakespeare.txt"
wave_file = "Shakespeare.wav"

try:
    # Check if wave file exists
    with open(wave_file, 'rb') as f:
        print("Speech recognition started.")
        
        # Configure speech recognition
        speech_config = speechsdk.SpeechConfig(subscription=azure_key, region=azure_location)
        audio_config = speechsdk.AudioConfig(filename=wave_file)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        
        # Perform recognition
        result = speech_recognizer.recognize_once()
        
        # Write result to text file
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            with open(text_file, 'w', encoding='utf-8') as text_output:
                text_output.write(result.text)
            print("Speech recognition stopped.")
        else:
            print(f"Recognition failed: {result.reason}")
            
except Exception as ex:
    print(str(ex))



#########################
List of Commands
#########################

apt-get update
mkdir application
cd application
apt install python3-pip
python3 -m venv myenv
source myenv/bin/activate
pip install azure-cognitiveservices-speech
nano app.py
curl -L https://aka.ms/ShakespeareWAV -o Shakespeare.wav
ls -l
python app.py
ls -l
cat Shakespeare.txt




