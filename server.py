from flask import Flask,request,jsonify
import util
app=Flask(__name__)



@app.route("/hello",methods=["GET"])
def hello():
    response= jsonify("hello")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/image', methods=['POST'])
def classify_image():
    # image_data = request.get("image_data")
    image_data=request.form["image_data"]
    response = jsonify(util.prediction_class(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route("/")
def home():
    response=jsonify(util.prediction_class())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__=="__main__":
    util.load_artifact()
    app.run(port=5000)
