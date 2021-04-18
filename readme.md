# VeeTooTee

## Dependencies

+ ffmpeg
+ sox
+ webrtcvad
+ youtube-dl

## Usage
Suppose we want to process
[試映劇場《寫實的天能》完整版｜試當真](https://www.youtube.com/watch?v=pumhdhv6r2w), please follow the steps listed below:

```
# Make a directory to store the files of this video
mkdir "試映劇場《寫實的天能》完整版｜試當真"
cd "試映劇場《寫實的天能》完整版｜試當真"

# Download the video
youtube-dl https://www.youtube.com/watch\?v\=pumhdhv6r2w -o video


# Extract the audio from the video
ffmpeg -i video.mp4 -q:a 0 -map a audio.wav
# Make the audio mono (and down-sample it)
sox audio.wav -c 1 -r 32000 32k-audio.wav 

# Locate the speech segments          
python ../find-speech.py 3 32k-audio.wav| tee find-speech.log

python ../transcribe.py | tee transcription.txt

```
