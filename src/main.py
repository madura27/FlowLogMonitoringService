from flask import Flask, Response, jsonify, request, make_response

from flow_monitoring_service import FlowMonitoringService

app = Flask(__name__)

service = FlowMonitoringService()


@app.route('/flows', methods = ['GET'])
def get_flows():
    query_params = request.args.to_dict() # request.args.get('hour')
    response, error = service.get(query_params)
    if error is not None:
        return make_response(error.error_msg, error.code)
    if response is None:
        return jsonify(list())
    return jsonify(response)

@app.route('/flows', methods = ['POST'])
def put_flows():
    error = service.put(request)
    if error is not None:
        return make_response(error.error_msg, error.code)
    return Response(status=200)


app.run(host='0.0.0.0', port=3000)