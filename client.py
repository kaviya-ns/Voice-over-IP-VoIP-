import socket
import pyaudio

# Audio parameters
CHUNK = 1024  # Buffer size
FORMAT = pyaudio.paInt16  # Audio format (16-bit)
CHANNELS = 1  # Mono channel
RATE = 44100  # Sampling rate (44.1 kHz)

# Create a socket
c = socket.socket()
host = socket.gethostname()  # Get local machine name
port = 5000  # Port to connect to
c.connect((host, port))
print("Connected to the server at", host)

# Setup PyAudio to capture microphone input
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Capture and send audio data in real-time
try:
    while True:
        data = stream.read(CHUNK)  # Capture audio data from the microphone
        print("Transmitting audio to the server...")  # Indicate that audio is being transmitted
        c.sendall(data)  # Send the audio data to the server
except:
    pass

c.close()
stream.stop_stream()
stream.close()
p.terminate()
