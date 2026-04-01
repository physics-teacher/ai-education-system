from fastapi import FastAPI

app =FastAPI()

@app.get("/")
def home():
	return {"message": "AI Education API running"}


@app.get("/generate_question")
def generate_question():
	return {"question": "Example physics question"}

