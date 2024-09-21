from flask import Flask, render_template, redirect, request
from pcpartpicker import API

app = Flask(__name__)
pcpartpickerapi = API()


@app.route("/")
def get_home_page():
    return redirect("/cpu")


@app.route("/cpu", methods=["GET", "POST"])
async def get_amd_page():
    if request.method == "POST":
        if request.form['cpu'] == "" or request.form["brand"] == "":
            return redirect("/cpu")

        cpu_model = request.form["cpu"]
        cpu_brand = request.form["brand"]
        result = await pcpartpickerapi.retrieve("cpu")

        for cpu in result["cpu"]:
            if cpu.brand == cpu_brand and cpu.model == cpu_model:
                return render_template("cpu_result.html", cpu=cpu)

    brands = set()

    cpus = await pcpartpickerapi.retrieve("cpu")

    for cpu in cpus["cpu"]:
        brands.add(cpu.brand)

    return render_template("cpu_find.html", brands=brands)

if __name__ == "__main__":
    app.run()
