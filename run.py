import uvicorn
import os

inside = os.environ.get('IN_DOCKER', False)

print("Launching Dungeons And Dungeons Distribution")
h = "127.0.0.1"
if inside:
    print('I am running in a Docker container')
    h = "0.0.0.0"
if __name__ == '__main__':
    uvicorn.run("main:app", host=h, port=8080)
