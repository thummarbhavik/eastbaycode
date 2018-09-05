import docker
client = docker.from_env()
#handles=client.containers.run("ubuntu:latest","./bbt train sol.py input.json output.json")
handles=client.images.build(path="/home/bhavik/eastbaycode/runner",tag="latest")
print(handles)
handles=client.containers.run("latest:latest")
print(handles)
input("fdfgbbgfgb")
