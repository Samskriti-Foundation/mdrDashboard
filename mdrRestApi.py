__author__ = 'naras_mg'

# libraries
from flask import Flask, jsonify
from flask_cors import cross_origin
import yaml
from yaml import SafeLoader
import sqlDashboardCountsQuery

yamlFile = yaml.load(open("db_credentials.yaml"), SafeLoader)

app = Flask(__name__)

# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)
@app.route('/')
@cross_origin()
def hello():
  return 'Hello from mdr dashboard service!'
@app.route('/app/<string:prefix>')
@cross_origin()
def dashboard(prefix):
  return jsonify(sqlDashboardCountsQuery.getDataQryResults(yamlFile[prefix]['db']))
@app.route('/allcounts')
@cross_origin()
def dashboard_sqlQuery():
    return jsonify(sqlDashboardCountsQuery.getDataQryResultsAll())
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)