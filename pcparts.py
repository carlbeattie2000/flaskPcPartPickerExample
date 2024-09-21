from flask import Flask, render_template
from pcpartpicker import API
import json

app = Flask(__name__)
pcpartpickerapi = API()

@app.route("/")
def get_home_page():
    return render_template("./index.html")

@app.route("/amd/<string:offset1>")
async def get_amd_cpu(offset1=""):
    result = await pcpartpickerapi.retrieve("cpu")
    resultJson = json.loads(result.to_json())
    for cpu in resultJson["cpu"]:
        if cpu["brand"] == "AMD" and cpu["model"] == offset1:
            return cpu
    return json.dumps({ "error": "not found" })

if __name__ == "__main__":
    app.run()

