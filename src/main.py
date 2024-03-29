import uvicorn
from fastapi import FastAPI


def get_application() -> FastAPI:
	application = FastAPI()
	return application


app = get_application()


if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0", reload=True)
