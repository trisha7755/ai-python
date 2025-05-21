import azure.cognitiveservices.speech as speechsdk
import os

AZURE_KEY = "YOUR_AZURE_SPEECH_KEY"  # Replace with your actual key
AZURE_REGION = "eastus"  # Change region if needed

def text_to_speech(input_file, output_file):
    """
    Converts text from a file to speech and saves as WAV using Azure Speech Service
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found")

        # Read text from file
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Configure speech synthesis
        speech_config = speechsdk.SpeechConfig(
            subscription=AZURE_KEY,
            region=AZURE_REGION
        )
        
        # Set the voice (optional)
        speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"  # Female voice
        
        # Configure audio output
        audio_config = speechsdk.audio.AudioOutputConfig(
            filename=output_file
        )

        # Create synthesizer
        synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=speech_config,
            audio_config=audio_config
        )

        print(f"\nConverting '{input_file}' to speech...")

        # Synthesize the text
        result = synthesizer.speak_text_async(text).get()

        # Check results
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"Successfully saved speech to '{output_file}'")
            return True
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print(f"Speech synthesis canceled: {cancellation.reason}")
            if cancellation.reason == speechsdk.CancellationReason.Error:
                print(f"Error details: {cancellation.error_details}")
            return False

    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("=== Text to Speech Converter ===")
    print("Using Azure Cognitive Services Speech SDK\n")
    
    # Get input file from user
    input_file = input("Enter the path to your text file: ").strip()
    
    # Generate output filename
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = f"{base_name}_output.wav"
    
    print(f"\nInput file: {input_file}")
    print(f"Output will be saved as: {output_file}")
    
    # Run the conversion
    success = text_to_speech(
        input_file=input_file,
        output_file=output_file
    )

    if success:
        print("\nConversion completed successfully!")
    else:
        print("\nConversion failed. Please check the error messages.")
