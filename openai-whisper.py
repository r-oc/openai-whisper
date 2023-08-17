import whisper

model = whisper.load_model("base")
result = model.transcribe("harvard.wav/Rathnally_St.m4a")

print(result["text"])

