from peewee import *
import yaml
from yaml.loader import SafeLoader
def get_credentials(user):
    dbcredentials = yaml.load(open("db_credentials.yaml"), SafeLoader)
    if user in dbcredentials and 'db' in dbcredentials[user] and 'user' in dbcredentials[user] and 'password' in dbcredentials[user]:
        return dbcredentials[user]['db'], dbcredentials[user]['user'], dbcredentials[user]['password']
    return None, None, None
def get_dburl():
    dbcredentials = yaml.load(open("db_credentials.yaml"), SafeLoader)
    if "database_url" in dbcredentials: return dbcredentials["database_url"]
    return None
db, db_user, db_password = get_credentials('sciencetechnology')
database_url = get_dburl()
if database_url == None: database = MySQLDatabase(db, **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'port': 3306, 'user': db_user, 'password': db_password})
else: database = MySQLDatabase(db, host=database_url, port=3306, user=db_user, password=db_password)


class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database
class OmdsDigitalManuscript(BaseModel):
    # author_fk = ForeignKeyField(backref='omds_person_author_fk_set', column_name='AuthorFkId', field='id', model=OmdsPerson, null=True)
    contribution_to_ayurveda = CharField(column_name='CONTRIBUTION_TO_AYURVEDA', null=True)
    id = BigAutoField(column_name='Id')
    # material_fk = ForeignKeyField(backref='omds_material_material_fk_set', column_name='MaterialFkId', field='id', model=OmdsMaterial, null=True)
    name = CharField(column_name='NAME')
    # organisation_fk = ForeignKeyField(backref='omds_organisation_organisation_fk_set', column_name='OrganisationFkId', field='id', model=OmdsOrganisation, null=True)
    # publication_fk = ForeignKeyField(backref='omds_publication_publication_fk_set', column_name='PublicationFkId', field='id', model=OmdsPublication, null=True)
    remarks = CharField(column_name='REMARKS', null=True)
    summary = TextField(column_name='SUMMARY', null=True)
    type_of_work = IntegerField(column_name='TYPE_OF_WORK', null=True)
    uniqueness_of_work = TextField(column_name='UNIQUENESS_OF_WORK', null=True)
    acc_no = CharField(null=True)
    any_other_details = TextField(null=True)
    # article_detail_fk = ForeignKeyField(column_name='articleDetailFkId', field='id', model=MdrArticleDetails, null=True)
    article_laguage = IntegerField(column_name='articleLaguage', null=True)
    beginning_line = CharField(null=True)
    bundle_masterfkid = BigIntegerField(column_name='bundleMasterfkid', null=True)
    catalogue_no = CharField(null=True)
    cataloguedetails = CharField(null=True)
    # category_fk = ForeignKeyField(column_name='categoryFkId', field='id', model=OmdsCategory, null=True)
    characters_per_line = CharField(column_name='charactersPerLine', null=True)
    colophon = CharField(null=True)
    # commentatorfkid = ForeignKeyField(backref='omds_person_commentatorfkid_set', column_name='commentatorfkid', field='id', model=OmdsPerson, null=True)
    condition_of_manuscript = CharField(null=True)
    decorated = IntegerField(null=True)
    decorated_remarks = TextField(column_name='decoratedRemarks', null=True)
    diacritical_name = CharField(null=True)
    digitized_by = CharField(null=True)
    digitizerid = BigIntegerField(null=True)
    document_type = BigIntegerField(column_name='documentType', null=True)
    documentation_of_manuscript = IntegerField(null=True)
    edited = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    edited_type = CharField(column_name='editedType', null=True)
    edited_type_remarks = TextField(column_name='editedTypeRemarks', null=True)
    ending_line = CharField(null=True)
    fields_covered = CharField(column_name='fieldsCovered', null=True)
    illustrations = IntegerField(null=True)
    illustrations_others = CharField(column_name='illustrationsOthers', null=True)
    illustrations_type = CharField(column_name='illustrationsType', null=True)
    ink_pigment = CharField(column_name='inkPigment', null=True)
    ink_pigment_others = CharField(column_name='inkPigmentOthers', null=True)
    is_deleted = IntegerField(column_name='isDeleted', null=True)
    isbound = IntegerField(null=True)
    # language_fk = ForeignKeyField(backref='omds_language_language_fk_set', column_name='languageFkId', field='id', model=OmdsLanguage, null=True)
    lines_per_page = CharField(column_name='linesPerPage', null=True)
    manuscript_id = CharField(null=True)
    manuscripttype = IntegerField(null=True)
    miscellaneous_remarks = TextField(column_name='miscellaneousRemarks', null=True)
    nature_of_collection = IntegerField(null=True)
    # nmm_details_fk = ForeignKeyField(column_name='nmmDetailsFkId', field='id', model=OmdsNmmDetails, null=True)
    parentfkid = ForeignKeyField(column_name='parentfkid', field='id', model='self', null=True)
    patha = CharField(null=True)
    recordstatus = IntegerField(null=True)
    red_digits = CharField(column_name='redDigits', null=True)
    red_digits_text = CharField(column_name='redDigitsText', null=True)
    red_letters = CharField(column_name='redLetters', null=True)
    red_letters_text = CharField(column_name='redLettersText', null=True)
    red_lines = CharField(column_name='redLines', null=True)
    red_lines_text = CharField(column_name='redLinesText', null=True)
    red_marked = CharField(column_name='redMarked', null=True)
    red_marked_text = CharField(column_name='redMarkedText', null=True)
    regional_name = CharField(null=True)
    # scribefkid = ForeignKeyField(backref='omds_person_scribefkid_set', column_name='scribefkid', field='id', model=OmdsPerson, null=True)
    # script_fk = ForeignKeyField(column_name='scriptFkId', field='id', model=OmdsScript, null=True)
    source_of_catalogue = IntegerField(null=True)
    # specific_category_fk = ForeignKeyField(column_name='specificCategoryFkId', field='id', model=OmdsSpecificcategory, null=True)
    # sub_commentatorfkid = ForeignKeyField(backref='omds_person_sub_commentatorfkid_set', column_name='subCommentatorfkid', field='id', model=OmdsPerson, null=True)
    subject1 = CharField(null=True)
    table_of_contents = CharField(null=True)
    total_no_of_folios = BigIntegerField(null=True)
    total_no_of_maps = BigIntegerField(null=True)
    trans_language = CharField(column_name='transLanguage', null=True)
    # translatorfkid = ForeignKeyField(backref='omds_person_translatorfkid_set', column_name='translatorfkid', field='id', model=OmdsPerson, null=True)

    class Meta:
        table_name = 'omds_digital_manuscript'
class OmdsEmployeemaster(BaseModel):
    address1 = CharField(column_name='Address1')
    created_by = CharField(column_name='CreatedBy', null=True)
    created_date = DateTimeField(column_name='CreatedDate', null=True)
    dob = DateTimeField(column_name='Dob')
    email = CharField(column_name='Email', null=True)
    first_name = CharField(column_name='FirstName')
    gender = IntegerField(column_name='Gender')
    id = BigAutoField(column_name='Id')
    last_name = CharField(column_name='LastName')
    modified_by = CharField(column_name='ModifiedBy', null=True)
    modified_date = DateTimeField(column_name='ModifiedDate', null=True)
    phone_number = CharField(column_name='PhoneNumber')
    row_version = IntegerField(column_name='RowVersion', null=True)
    type = IntegerField(column_name='Type')
    department_master_fk_id = BigIntegerField(column_name='departmentMasterFkId', null=True)
    is_deleted = IntegerField(column_name='isDeleted', null=True)
    sms_detail_fk_id = BigIntegerField(column_name='smsDetailFkId', null=True)

    class Meta:
        table_name = 'omds_employeemaster'