__author__ = 'naras_mg'

import yaml
# libraries
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from yaml import SafeLoader

import dbmodelMetallurgy, dbmodelYogabibliography, dbmodelHistory, dbmodelPhilosophy, dbmodelScienceTechnology
dictYogabibliography, dictHistory, dictMetallurgy, dictPhilosophy, dictScienceTechnology = None, None, None, None, None
dbcredentials = yaml.load(open("db_credentials.yaml"), SafeLoader)
if 'metallurgy' in dbcredentials:
    dbMetallurgy = dbmodelMetallurgy.database
    dbMetallurgy.create_tables([dbmodelMetallurgy.OmdsEmployeemaster, dbmodelMetallurgy.OmdsDigitalManuscript], safe=True)
    emMetallurgy = dbmodelMetallurgy.OmdsEmployeemaster
    dmMetallurgy = dbmodelMetallurgy.OmdsDigitalManuscript
    dictMetallurgy = {'Users': emMetallurgy.select().where(emMetallurgy.is_deleted == 0).count(), 'Manuscripts': dmMetallurgy.select().where((dmMetallurgy.document_type == 1) & (dmMetallurgy.is_deleted == 0)).count(), 'Books': dmMetallurgy.select().where((dmMetallurgy.document_type == 2) & (dmMetallurgy.is_deleted == 0)).count(), 'Articles':  dmMetallurgy.select().where((dmMetallurgy.document_type == 3) & (dmMetallurgy.is_deleted == 0)).count()}
if 'yogabibliography' in dbcredentials:
    dbYogabibliography = dbmodelYogabibliography.database
    dbYogabibliography.create_tables([dbmodelYogabibliography.OmdsEmployeemaster, dbmodelYogabibliography.OmdsDigitalManuscript], safe=True)
    emYogabibliography = dbmodelYogabibliography.OmdsEmployeemaster
    dmYogabibliography = dbmodelYogabibliography.OmdsDigitalManuscript
    dictYogabibliography = {'Users': emYogabibliography.select().where(emYogabibliography.is_deleted == 0).count(), 'Manuscripts': dmYogabibliography.select().where((dmYogabibliography.document_type == 1) & (dmYogabibliography.is_deleted == 0)).count(), 'Books': dmYogabibliography.select().where((dmYogabibliography.document_type == 2) & (dmYogabibliography.is_deleted == 0)).count(), 'Articles':  dmYogabibliography.select().where((dmYogabibliography.document_type == 3) & (dmYogabibliography.is_deleted == 0)).count()}
if 'history' in dbcredentials:
    dbHistory = dbmodelHistory.database
    dbHistory.create_tables([dbmodelHistory.OmdsEmployeemaster, dbmodelHistory.OmdsDigitalManuscript], safe=True)
    emHistory = dbmodelHistory.OmdsEmployeemaster
    dmHistory = dbmodelHistory.OmdsDigitalManuscript
    dictHistory = {'Users': emHistory.select().where(emHistory.is_deleted == 0).count(), 'Manuscripts': dmHistory.select().where((dmHistory.document_type == 1) & (dmHistory.is_deleted == 0)).count(), 'Books': dmHistory.select().where((dmHistory.document_type == 2) & (dmHistory.is_deleted == 0)).count(), 'Articles':  dmHistory.select().where((dmHistory.document_type == 3) & (dmHistory.is_deleted == 0)).count()}
if 'philosophy' in dbcredentials:
    dbPhilosophy = dbmodelPhilosophy.database
    dbPhilosophy.create_tables([dbmodelPhilosophy.OmdsEmployeemaster, dbmodelPhilosophy.OmdsDigitalManuscript], safe=True)
    emPhilosophy = dbmodelPhilosophy.OmdsEmployeemaster
    dmPhilosophy = dbmodelPhilosophy.OmdsDigitalManuscript
    dictPhilosophy = {'Users': emPhilosophy.select().where(emPhilosophy.is_deleted == 0).count(), 'Manuscripts': dmPhilosophy.select().where((dmPhilosophy.document_type == 1) & (dmPhilosophy.is_deleted == 0)).count(), 'Books': dmPhilosophy.select().where((dmPhilosophy.document_type == 2) & (dmPhilosophy.is_deleted == 0)).count(), 'Articles':  dmPhilosophy.select().where((dmPhilosophy.document_type == 3) & (dmPhilosophy.is_deleted == 0)).count()}
if 'sciencetechnology' in dbcredentials:
    dbScienceTechnology = dbmodelScienceTechnology.database
    dbScienceTechnology.create_tables([dbmodelScienceTechnology.OmdsEmployeemaster, dbmodelScienceTechnology.OmdsDigitalManuscript], safe=True)
    emScienceTechnology = dbmodelScienceTechnology.OmdsEmployeemaster
    dmScienceTechnology = dbmodelScienceTechnology.OmdsDigitalManuscript
    dictScienceTechnology = {'Users': emScienceTechnology.select().where(emScienceTechnology.is_deleted == 0).count(), 'Manuscripts': dmScienceTechnology.select().where((dmScienceTechnology.document_type == 1) & (dmScienceTechnology.is_deleted == 0)).count(), 'Books': dmScienceTechnology.select().where((dmScienceTechnology.document_type == 2) & (dmScienceTechnology.is_deleted == 0)).count(), 'Articles':  dmScienceTechnology.select().where((dmScienceTechnology.document_type == 3) & (dmScienceTechnology.is_deleted == 0)).count()}

app = Flask(__name__)

# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)
@app.route('/')
@cross_origin()
def hello():
  return 'Hello from mdr dashboard service!'
@app.route('/all')
@cross_origin()
def dashboard_all():
    return jsonify(
      {'Metallurgy': dictMetallurgy},
      {'ScienceTechnology': dictScienceTechnology},
      {'Philosophy': dictPhilosophy},
      {'History':dictHistory},
      {'Yogabibliography': dictYogabibliography}
      )
@app.route('/yogabibliography')
@cross_origin()
def dashboard_yogabibliography():
  return jsonify({'Yogabibliography':dictYogabibliography})
@app.route('/history')
@cross_origin()
def dashboard_history():
  return jsonify({'History':dictHistory})
@app.route('/metallurgy')
@cross_origin()
def dashboard_metallurgy():
  return jsonify({'Metallurgy':dictMetallurgy})
@app.route('/philosophy')
@cross_origin()
def dashboard_philosophy():
    return jsonify({'Philosophy':dictPhilosophy})
@app.route('/sciencetechnology')
@cross_origin()
def dashboard_sciencetechnology():
    return jsonify({'ScienceTechnology':dictScienceTechnology})
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)