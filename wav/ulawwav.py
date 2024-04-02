from scipy.io import wavfile
from pydub import AudioSegment

# Specify the path to the ffmpeg and ffprobe tools
AudioSegment.converter = "/usr/bin/ffmpeg"
AudioSegment.ffmpeg = "/usr/bin/ffmpeg"
AudioSegment.ffprobe = "/usr/bin/ffprobe"

def convert_ulaw_to_wav(ulaw_file, wav_file):
    audio = AudioSegment.from_file(ulaw_file, format="ulaw")
    audio.export(wav_file, format="wav")

convert_ulaw_to_wav('hold.ulaw', 'hold.wav')