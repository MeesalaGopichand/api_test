from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route("/get-status/<service_tag>")
def get_status(service_tag):
    device_data = {}
    if(service_tag == "asdf"):
        device_data = {
            "name" : "power edge server x40",
            "type" : "server",
            "status" : "expired",
            "exp_date" : "12-02-2022",
            "email" : "user@dell.com",
            "service_tag" : service_tag,
            "r2years" : "8000",
            "r3years" : "11000"
        }
    if(service_tag == "asd"):
        device_data = {
            "name" : "power edge server 123",
            "type" : "server",
            "status" : "active",
            "exp_date" : "10-01-2023",
            "email" : "user@dell.com",
            "service_tag" : service_tag,
        }
    if(service_tag == "asdfg"):
        device_data = {
            "name" : "latitude 5530",
            "type" : "laptop",
            "status" : "active",
            "exp_date" : "15-10-2023",
            "email" : "user@dell.com",
            "service_tag" : service_tag,
            "r2years" : "2000",
            "r3years" : "2500"
         }

    api_key = request.args.get("api_key")
    if api_key:
        device_data['api_key'] = api_key

    res = make_response(jsonify(device_data), 200)
    res.headers['Access-Control-Allow-Origin'] = "*"
    return res

if __name__ == "__main__":
    app.run(debug=True)
