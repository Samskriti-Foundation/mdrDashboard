__author__ = 'naras_mg'

# libraries
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import dbmodelMetallurgy, dbmodelYogabibliography, dbmodelHistory, dbmodelPhilosophy, dbmodelScienceTechnology

dbMetallurgy = dbmodelMetallurgy.database
dbMetallurgy.create_tables([dbmodelMetallurgy.OmdsEmployeemaster, dbmodelMetallurgy.OmdsDigitalManuscript], safe=True)
emMetallurgy = dbmodelMetallurgy.OmdsEmployeemaster
dmMetallurgy = dbmodelMetallurgy.OmdsDigitalManuscript
# print({'Users': em.select().where(em.is_deleted == 0).count(), 'Manuscripts': dm.select().where((dm.document_type == 1) & (dm.is_deleted == 0)).count(), 'Books': dm.select().where((dm.document_type == 2) & (dm.is_deleted == 0)).count(), 'Articles':  dm.select().where((dm.document_type == 3) & (dm.is_deleted == 0)).count()})
dbYogabibliography = dbmodelYogabibliography.database
dbYogabibliography.create_tables([dbmodelYogabibliography.OmdsEmployeemaster, dbmodelYogabibliography.OmdsDigitalManuscript], safe=True)
emYogabibliography = dbmodelYogabibliography.OmdsEmployeemaster
dmYogabibliography = dbmodelYogabibliography.OmdsDigitalManuscript

dbHistory = dbmodelHistory.database
dbHistory.create_tables([dbmodelHistory.OmdsEmployeemaster, dbmodelHistory.OmdsDigitalManuscript], safe=True)
emHistory = dbmodelHistory.OmdsEmployeemaster
dmHistory = dbmodelHistory.OmdsDigitalManuscript

dbPhilosophy = dbmodelPhilosophy.database
dbPhilosophy.create_tables([dbmodelPhilosophy.OmdsEmployeemaster, dbmodelPhilosophy.OmdsDigitalManuscript], safe=True)
emPhilosophy = dbmodelPhilosophy.OmdsEmployeemaster
dmPhilosophy = dbmodelPhilosophy.OmdsDigitalManuscript

dbScienceTechnology = dbmodelScienceTechnology.database
dbScienceTechnology.create_tables([dbmodelScienceTechnology.OmdsEmployeemaster, dbmodelScienceTechnology.OmdsDigitalManuscript], safe=True)
emScienceTechnology = dbmodelScienceTechnology.OmdsEmployeemaster
dmScienceTechnology = dbmodelScienceTechnology.OmdsDigitalManuscript
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
      {'Metallurgy':{'Users': emMetallurgy.select().where(emMetallurgy.is_deleted == 0).count(), 'Manuscripts': dmMetallurgy.select().where((dmMetallurgy.document_type == 1) & (dmMetallurgy.is_deleted == 0)).count(), 'Books': dmMetallurgy.select().where((dmMetallurgy.document_type == 2) & (dmMetallurgy.is_deleted == 0)).count(), 'Articles':  dmMetallurgy.select().where((dmMetallurgy.document_type == 3) & (dmMetallurgy.is_deleted == 0)).count()}},
      {'ScienceTechnology':{'Users': emScienceTechnology.select().where(emScienceTechnology.is_deleted == 0).count(), 'Manuscripts': dmScienceTechnology.select().where((dmScienceTechnology.document_type == 1) & (dmScienceTechnology.is_deleted == 0)).count(), 'Books': dmScienceTechnology.select().where((dmScienceTechnology.document_type == 2) & (dmScienceTechnology.is_deleted == 0)).count(), 'Articles':  dmScienceTechnology.select().where((dmScienceTechnology.document_type == 3) & (dmScienceTechnology.is_deleted == 0)).count()}},
      {'Philosophy':{'Users': emPhilosophy.select().where(emPhilosophy.is_deleted == 0).count(), 'Manuscripts': dmPhilosophy.select().where((dmPhilosophy.document_type == 1) & (dmPhilosophy.is_deleted == 0)).count(), 'Books': dmPhilosophy.select().where((dmPhilosophy.document_type == 2) & (dmPhilosophy.is_deleted == 0)).count(), 'Articles':  dmPhilosophy.select().where((dmPhilosophy.document_type == 3) & (dmPhilosophy.is_deleted == 0)).count()}},
      {'History':{'Users': emHistory.select().where(emHistory.is_deleted == 0).count(), 'Manuscripts': dmHistory.select().where((dmHistory.document_type == 1) & (dmHistory.is_deleted == 0)).count(), 'Books': dmHistory.select().where((dmHistory.document_type == 2) & (dmHistory.is_deleted == 0)).count(), 'Articles':  dmHistory.select().where((dmHistory.document_type == 3) & (dmHistory.is_deleted == 0)).count()}},
      {'Yogabibliography':{'Users': emYogabibliography.select().where(emYogabibliography.is_deleted == 0).count(), 'Manuscripts': dmYogabibliography.select().where((dmYogabibliography.document_type == 1) & (dmYogabibliography.is_deleted == 0)).count(), 'Books': dmYogabibliography.select().where((dmYogabibliography.document_type == 2) & (dmYogabibliography.is_deleted == 0)).count(), 'Articles':  dmYogabibliography.select().where((dmYogabibliography.document_type == 3) & (dmYogabibliography.is_deleted == 0)).count()}},
      )
@app.route('/yogabibliography')
@cross_origin()
def dashboard_yogabibliography():
  return jsonify({'Yogabibliography':{'Users': emYogabibliography.select().where(emYogabibliography.is_deleted == 0).count(), 'Manuscripts': dmYogabibliography.select().where((dmYogabibliography.document_type == 1) & (dmYogabibliography.is_deleted == 0)).count(), 'Books': dmYogabibliography.select().where((dmYogabibliography.document_type == 2) & (dmYogabibliography.is_deleted == 0)).count(), 'Articles':  dmYogabibliography.select().where((dmYogabibliography.document_type == 3) & (dmYogabibliography.is_deleted == 0)).count()}})
@app.route('/history')
@cross_origin()
def dashboard_history():
  return jsonify({'History':{'Users': emHistory.select().where(emHistory.is_deleted == 0).count(), 'Manuscripts': dmHistory.select().where((dmHistory.document_type == 1) & (dmHistory.is_deleted == 0)).count(), 'Books': dmHistory.select().where((dmHistory.document_type == 2) & (dmHistory.is_deleted == 0)).count(), 'Articles':  dmHistory.select().where((dmHistory.document_type == 3) & (dmHistory.is_deleted == 0)).count()}})
@app.route('/metallurgy')
@cross_origin()
def dashboard_metallurgy():
  return jsonify({'Metallurgy':{'Users': emMetallurgy.select().where(emMetallurgy.is_deleted == 0).count(), 'Manuscripts': dmMetallurgy.select().where((dmMetallurgy.document_type == 1) & (dmMetallurgy.is_deleted == 0)).count(), 'Books': dmMetallurgy.select().where((dmMetallurgy.document_type == 2) & (dmMetallurgy.is_deleted == 0)).count(), 'Articles':  dmMetallurgy.select().where((dmMetallurgy.document_type == 3) & (dmMetallurgy.is_deleted == 0)).count()}})
@app.route('/philosophy')
@cross_origin()
def dashboard_philosophy():
    return jsonify({'Philosophy':{'Users': emPhilosophy.select().where(emPhilosophy.is_deleted == 0).count(), 'Manuscripts': dmPhilosophy.select().where((dmPhilosophy.document_type == 1) & (dmPhilosophy.is_deleted == 0)).count(), 'Books': dmPhilosophy.select().where((dmPhilosophy.document_type == 2) & (dmPhilosophy.is_deleted == 0)).count(), 'Articles':  dmPhilosophy.select().where((dmPhilosophy.document_type == 3) & (dmPhilosophy.is_deleted == 0)).count()}})
@app.route('/sciencetechnology')
@cross_origin()
def dashboard_sciencetechnology():
    return jsonify({'ScienceTechnology':{'Users': emScienceTechnology.select().where(emScienceTechnology.is_deleted == 0).count(), 'Manuscripts': dmScienceTechnology.select().where((dmScienceTechnology.document_type == 1) & (dmScienceTechnology.is_deleted == 0)).count(), 'Books': dmScienceTechnology.select().where((dmScienceTechnology.document_type == 2) & (dmScienceTechnology.is_deleted == 0)).count(), 'Articles':  dmScienceTechnology.select().where((dmScienceTechnology.document_type == 3) & (dmScienceTechnology.is_deleted == 0)).count()}})
if __name__ == '__main__':
    app.run(debug=True, port=5000)