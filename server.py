import socket
import pyaudio

# Audio parameters
CHUNK = 1024  # Buffer size
FORMAT = pyaudio.paInt16  # Audio format (16-bit)
CHANNELS = 1  # Mono channel
RATE = 44100  # Sampling rate (44.1 kHz)

# Create a socket
s = socket.socket()
host = socket.gethostname()  # Get local machine name
port = 5000  # Port to bind to
s.bind((host, port))

# Setup PyAudio to play the audio stream
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

# Listen for incoming connections
s.listen(3)
print(f"Server is listening on {host}:{port}")

while True:
    c, addr = s.accept()  # Accept connection from client
    print(f'Connected to client: {addr}')

    # Receive and play audio data in real-time
    try:
        while True:
            data = c.recv(CHUNK)  # Receive audio data from the client
            if not data:
                break  # Stop when no data is received
            print("Receiving audio data...")  # Indicate that audio is being received
            stream.write(data)  # Play received audio in real-time
            print("Playing audio on server...")  # Indicate that audio is being played
    except:
        break

c.close()
stream.stop_stream()
stream.close()
p.terminate()
