__author__ = 'naras_mg'

# libraries
from flask import Flask, jsonify, request
from flask_cors import cross_origin
import yaml
from yaml import SafeLoader

import sqlDashboardQry

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
    if prefix in yamlFile: return jsonify(sqlDashboardQry.getDataQryResults(yamlFile[prefix]['db']))
    else: return jsonify({})
@app.route('/sub/<string:prefix>', methods=['GET'])
@cross_origin()
def dashboard_subject(prefix):
    app = request.args.get('app', 'sciencetechnology')
    appdb = yamlFile[app]['db']
    key = {'sciencetechnology':'ScienceTechnology', 'philosophy':'Philosophy'}[app]
    # return jsonify({'app':app, 'key':key, 'appdb':appdb})
    prefix = prefix.capitalize()
    dicResult =  sqlDashboardQry.getDataQryResults(appdb)[key]['Subjects']
    if prefix in dicResult: return jsonify({prefix: dicResult[prefix]})
    else: return jsonify({prefix: {'Subject':'missing'}})
@app.route('/allcounts')
@cross_origin()
def dashboard_sqlQuery():
    return jsonify(sqlDashboardQry.getDataQryResultsAll())
@app.route('/subs/<string:prefix>', methods=['GET'])
@cross_origin()
def dashboard_subjects_csv_list_totals(prefix):
    app = request.args.get('subs', '')
    appdb = yamlFile[prefix]['db']
    key = {'sciencetechnology': 'ScienceTechnology', 'philosophy': 'Philosophy', 'yogabibliography': 'Yogabibliography',
           'history': 'History', 'metallurgy': 'Metallurgy'}[prefix]
    res = sqlDashboardQry.getDataQryResults(appdb)
    totals = {'Articles':0, 'Books':0, 'Manuscripts':0}
    reskey = res[key]['Subjects']
    for sub in app.split(','):
        for lbl in ['Articles', 'Books', 'Manuscripts']:
            if sub in reskey: totals[lbl] += reskey[sub][lbl]
    return jsonify({prefix:totals})
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)