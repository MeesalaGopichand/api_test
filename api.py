from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route("/get-status/<service_tag>")
def get_status(service_tag):
    if(service_tag != ""):
        device_data = {}
        status_code = 200
        if(service_tag == "54FZTT2"):
            device_data = {
                "name" : "Latitude 5490",
                "type" : "server",
                "status" : "Expired",
                "exp_date" : "07 FEB 2022",
                "email" : "user@dell.com",
                "service_tag" : service_tag,
                "n_status" : "0",
                "p_url" : "https://www.dell.com/support/home/en-in/product-support/servicetag/"+service_tag,
                "img_url" : "latitude5490.jpg"
            }
        elif(service_tag == "4YXMQN2"):
            device_data = {
                "name" : "Latitude 5480/5488",
                "type" : "server",
                "status" : "Expired",
                "exp_date" : "27 APR 2021",
                "email" : "user@dell.com",
                "service_tag" : service_tag,
                "n_status" : "0",
                "p_url" : "https://www.dell.com/support/home/en-in/product-support/servicetag/"+service_tag,
                "img_url" : "latitude5480.jpg"
            }
        elif(service_tag == "3C1ZTL3"):
            device_data = {
                "name" : "Latitude 5530",
                "type" : "laptop",
                "status" : "Active",
                "exp_date" : "27 AUG 2025",
                "email" : "user@dell.com",
                "service_tag" : service_tag,
                "n_status" : "2",
                "p_url" : "https://www.dell.com/support/home/en-in/product-support/servicetag/"+service_tag,
                "img_url" : "latitude5530.jpg"
            }
        else:
            device_data = {
                "error" : " no device found",
                "service_tag" : service_tag,
                "n_status" : "3"
            }
            status_code = 200

        res = make_response(jsonify(device_data), status_code)
        res.headers['Access-Control-Allow-Origin'] = "*"
        return res
    # except:
    #     device_data = {
    #         "error" : " no device found",
    #         "service_tag" : service_tag,
    #         "n_status" : "3"
    #     }
    #     res = make_response(jsonify(device_data), 200)
    #     res.headers['Access-Control-Allow-Origin'] = "*"
    #     return res


if __name__ == "__main__":
    app.run(debug=True)
