from fastapi import FastAPI
import json
import cohere
from schemas import UserInstruction

app = FastAPI()


with open("config.json") as config_file:
    config = json.load(config_file)

co = cohere.Client(config["cohere_api_key"])


@app.get("/")
def read_root():
    response = co.chat(message="hello world!")
    return response.text


@app.post("/generate_openapi")
async def generate_openapi(request: UserInstruction):
    response = co.chat(
        message=f"""Generate OpenAPI specs for the following instruction..
        Just putout the spec in markdown yaml. don't give any other comments: {request.user_instruction}"""
    )

    openapi_spec = response.text
    return {"openapi_specs": openapi_spec}
