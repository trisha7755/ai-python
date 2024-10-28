using System.Text;
using System.Threading.Tasks;
using Microsoft.CognitiveServices.Speech;
using Microsoft.CognitiveServices.Speech.Audio;

string azureKey = "ENTER YOUR KEY";
string azureLocation = "ENTER YOUR LOCATION";
string textFile = "Shakespeare.txt";
string waveFile = "Shakespeare.wav";

try
{
    FileInfo fileInfo = new FileInfo(waveFile);
    if (fileInfo.Exists)
    {
        Console.WriteLine("Speech recognition started.");
        var speechConfig = SpeechConfig.FromSubscription(azureKey, azureLocation);
        using var audioConfig = AudioConfig.FromWavFileInput(fileInfo.FullName);
        using var speechRecognizer = new SpeechRecognizer(speechConfig, audioConfig);
        var result = await speechRecognizer.RecognizeOnceAsync();

        FileStream fileStream = File.OpenWrite(textFile);
        StreamWriter streamWriter = new StreamWriter(fileStream, Encoding.UTF8);
        streamWriter.WriteLine(result.Text);
        streamWriter.Close();
        Console.WriteLine("Speech recognition stopped.");
    }
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}
