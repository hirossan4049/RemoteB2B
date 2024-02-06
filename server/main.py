from fastapi import FastAPI
import uvicorn

from simplecoremidi import send_midi

app = FastAPI()

@app.get("/")
async def root():
  return "unko"

@app.post('/midi')
async def midi(mididata: str):
  midiarray = [int(num) for num in mididata.split(',')]
  if len(midiarray) != 3:
    return "invalid midi data"
  print("midiarray", midiarray)
  send_midi((midiarray[0], midiarray[1], midiarray[2]))

  return f"midi {mididata}"


if __name__ == "__main__":
  uvicorn.run("main:app", port=8000, reload=True)