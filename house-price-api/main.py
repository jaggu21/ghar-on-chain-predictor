from flask import Flask, jsonify
import subprocess
import sys

DAPP_ADDRESS = "/home/vijay/Desktop/projects/hackathons/ethindia/rollups-examples/custom-dapps/house/deployments/localhost/dapp.address"
FRONTEND_PATH = "/home/vijay/Desktop/projects/hackathons/ethindia/rollups-examples/frontend-console"


def get_payload(lot, bed):
    return '{"lot": ' + lot + ', "bed" : ' + bed + '}'

def get_transaction_string(lot, bed):
    command = f"cd {FRONTEND_PATH} && yarn start input send --payload '{get_payload(lot, bed)}' --addressFile {DAPP_ADDRESS}"
    return command

def get_api_call():
    return f"cd {FRONTEND_PATH} && yarn start notice list"

app = Flask(__name__)

@app.route("/")
def index():
    return "House price classifier is active"

@app.route("/predict/<string:lot>/<string:bed>")
def show_details(lot, bed):
    print(f"Lot: {lot}, Bed: {bed}")
    command_string = get_transaction_string(lot, bed)
    
    # FuncCall
    result = subprocess.run(
        command_string,
        capture_output = True,
        text = True,
        shell = True
    )

    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
    
    
    # Get the predicted price
    json_output = subprocess.run(
        get_api_call(),
        capture_output = True,
        text = True,
        shell = True
    )

    print("stdout:", json_output.stdout)
    print("stderr:", json_output.stderr)

    return json_output.stdout


if __name__ == "__main__":
    app.run(debug = True, port = 8090)
