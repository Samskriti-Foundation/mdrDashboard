from peewee import *
import yaml
from yaml.loader import SafeLoader
def get_credentials(user):
    dbcredentials = yaml.load(open("db_credentials.yaml"), SafeLoader)
    if user in dbcredentials and 'db' in dbcredentials[user] and 'user' in dbcredentials[user] and 'password' in dbcredentials[user]:
        return dbcredentials[user]['db'], dbcredentials[user]['user'], dbcredentials[user]['password']
    return None
# def get_db():
#     db = yaml.load(open('db.yaml'), SafeLoader)
#     return db['History']
db, db_user, db_password = get_credentials('sciencetechnology')
database = MySQLDatabase(db, **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'port': 3306, 'user': db_user, 'password': db_password})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Epmcomboentityvo(BaseModel):
    label = CharField(column_name='Label')
    value = CharField(column_name='Value', null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'epmcomboentityvo'

class MdrArticleDetails(BaseModel):
    abstract_of_article = CharField(column_name='abstractOfArticle', null=True)
    abstract_of_magazine = CharField(column_name='abstractOfMagazine', null=True)
    address = CharField(null=True)
    id = BigAutoField()
    is_printed = IntegerField(column_name='isPrinted', null=True)
    issn_no = CharField(column_name='issnNo', null=True)
    journal_othr_dtls = CharField(column_name='journalOthrDtls', null=True)
    magazine_issn_no = CharField(column_name='magazineIssnNo', null=True)
    name_of_editor = CharField(column_name='nameOfEditor', null=True)
    name_of_magazine = CharField(column_name='nameOfMagazine', null=True)
    no_of_pages = CharField(column_name='noOfPages', null=True)
    price = CharField(null=True)
    type = IntegerField(null=True)
    website = CharField(null=True)
    year_of_publication = CharField(column_name='yearOfPublication', null=True)

    class Meta:
        table_name = 'mdr_article_details'

class OmdsAccesscontrol(BaseModel):
    id = BigAutoField(column_name='Id')
    menu_master_fk_id = BigIntegerField(column_name='MenuMasterFkId', null=True)
    role_master_fk_id = BigIntegerField(column_name='RoleMasterFkId', null=True)

    class Meta:
        table_name = 'omds_accesscontrol'

class OmdsBundle(BaseModel):
    bundle_number = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()
    isdeleted = IntegerField(null=True)
    name = CharField()

    class Meta:
        table_name = 'omds_bundle'

class OmdsCategory(BaseModel):
    id = BigAutoField()
    isdeleted = IntegerField(null=True)
    name = CharField(null=True)
    parentfkid = ForeignKeyField(column_name='parentfkid', field='id', model='self', null=True)

    class Meta:
        table_name = 'omds_category'

class OmdsCommoncodesmetadata(BaseModel):
    id = BigAutoField(column_name='Id')
    name = CharField(column_name='Name', null=True)

    class Meta:
        table_name = 'omds_commoncodesmetadata'

class OmdsCommoncodes(BaseModel):
    common_codes_metadata_fk = ForeignKeyField(backref='omds_commoncodesmetadata_common_codes_metadata_fk_set', column_name='CommonCodesMetadataFkId', field='id', model=OmdsCommoncodesmetadata, null=True)
    id = BigAutoField(column_name='Id')
    name = CharField(column_name='Name', null=True)

    class Meta:
        table_name = 'omds_commoncodes'

class OmdsConditionofmanuscript(BaseModel):
    id = BigAutoField()
    isdeleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    name = CharField(null=True)

    class Meta:
        table_name = 'omds_conditionofmanuscript'

class OmdsPublisher(BaseModel):
    address = CharField(column_name='ADDRESS')
    id = BigAutoField(column_name='Id')
    name = CharField(column_name='NAME')

    class Meta:
        table_name = 'omds_publisher'

class OmdsPerson(BaseModel):
    id = BigAutoField(column_name='Id')
    life_history = CharField(column_name='LIFE_HISTORY', null=True)
    name = CharField(column_name='NAME')
    period = CharField(column_name='PERIOD', null=True)
    diacritical_name = CharField(null=True)
    regional_name = CharField(null=True)
    type = IntegerField(null=True)

    class Meta:
        table_name = 'omds_person'

class OmdsPublication(BaseModel):
    author_fk = ForeignKeyField(backref='omds_person_author_fk_set', column_name='AuthorFkId', field='id', model=OmdsPerson, null=True)
    isavailable = IntegerField(column_name='ISAVAILABLE', null=True)
    id = BigAutoField(column_name='Id')
    no_of_pages = CharField(column_name='NO_OF_PAGES', null=True)
    price = CharField(column_name='PRICE', null=True)
    publisher_fk = ForeignKeyField(backref='omds_publisher_publisher_fk_set', column_name='PublisherFkId', field='id', model=OmdsPublisher, null=True)
    remark = CharField(column_name='REMARK', null=True)
    year_of_publication = CharField(column_name='YEAR_OF_PUBLICATION', null=True)
    editorfkid = ForeignKeyField(backref='omds_person_editorfkid_set', column_name='editorfkid', field='id', model=OmdsPerson, null=True)
    is_deleted = IntegerField(column_name='isDeleted', null=True)

    class Meta:
        table_name = 'omds_publication'

class OmdsMaterial(BaseModel):
    id = BigAutoField(column_name='Id')
    name = IntegerField(column_name='NAME', null=True)

    class Meta:
        table_name = 'omds_material'

class OmdsLanguage(BaseModel):
    id = BigAutoField(column_name='Id')
    name = CharField(column_name='NAME')
    unicode_point = CharField(column_name='UNICODE_POINT', null=True)
    isdeleted = IntegerField(null=True)

    class Meta:
        table_name = 'omds_language'

class OmdsNmmDetails(BaseModel):
    camera_make = CharField(column_name='cameraMake', null=True)
    camera_model = CharField(column_name='cameraModel', null=True)
    created_date = CharField(column_name='createdDate', null=True)
    digitised_date = CharField(column_name='digitisedDate', null=True)
    height = CharField(null=True)
    id = BigAutoField()
    width = CharField(null=True)
    x_resolution = CharField(column_name='xResolution', null=True)
    y_resolution = CharField(column_name='yResolution', null=True)

    class Meta:
        table_name = 'omds_nmm_details'

class OmdsOrganisation(BaseModel):
    address = CharField(column_name='ADDRESS', null=True)
    id = BigAutoField(column_name='Id')
    name = CharField(column_name='NAME')
    acronym = CharField(null=True)
    email = CharField(null=True)
    phone_number = CharField(column_name='phoneNumber', null=True)
    type = IntegerField(null=True)
    website = CharField(null=True)

    class Meta:
        table_name = 'omds_organisation'

class OmdsScript(BaseModel):
    id = BigAutoField(column_name='Id')
    name = CharField(column_name='NAME')
    unicode_point = CharField(column_name='UNICODE_POINT', null=True)
    isdeleted = IntegerField(null=True)

    class Meta:
        table_name = 'omds_script'

class OmdsSpecificcategory(BaseModel):
    id = BigAutoField()
    isdeleted = UnknownField(null=True)  # bit
    name = CharField(null=True)

    class Meta:
        table_name = 'omds_specificcategory'

class OmdsDigitalManuscript(BaseModel):
    author_fk = ForeignKeyField(backref='omds_person_author_fk_set', column_name='AuthorFkId', field='id', model=OmdsPerson, null=True)
    contribution_to_ayurveda = CharField(column_name='CONTRIBUTION_TO_AYURVEDA', null=True)
    id = BigAutoField(column_name='Id')
    material_fk = ForeignKeyField(backref='omds_material_material_fk_set', column_name='MaterialFkId', field='id', model=OmdsMaterial, null=True)
    name = CharField(column_name='NAME')
    organisation_fk = ForeignKeyField(backref='omds_organisation_organisation_fk_set', column_name='OrganisationFkId', field='id', model=OmdsOrganisation, null=True)
    publication_fk = ForeignKeyField(backref='omds_publication_publication_fk_set', column_name='PublicationFkId', field='id', model=OmdsPublication, null=True)
    remarks = CharField(column_name='REMARKS', null=True)
    summary = TextField(column_name='SUMMARY', null=True)
    type_of_work = IntegerField(column_name='TYPE_OF_WORK', null=True)
    uniqueness_of_work = TextField(column_name='UNIQUENESS_OF_WORK', null=True)
    acc_no = CharField(null=True)
    any_other_details = TextField(null=True)
    article_detail_fk = ForeignKeyField(column_name='articleDetailFkId', field='id', model=MdrArticleDetails, null=True)
    article_laguage = IntegerField(column_name='articleLaguage', null=True)
    beginning_line = CharField(null=True)
    bundle_masterfkid = BigIntegerField(column_name='bundleMasterfkid', null=True)
    catalogue_no = CharField(null=True)
    cataloguedetails = CharField(null=True)
    category_fk = ForeignKeyField(column_name='categoryFkId', field='id', model=OmdsCategory, null=True)
    characters_per_line = CharField(column_name='charactersPerLine', null=True)
    colophon = CharField(null=True)
    commentatorfkid = ForeignKeyField(backref='omds_person_commentatorfkid_set', column_name='commentatorfkid', field='id', model=OmdsPerson, null=True)
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
    language_fk = ForeignKeyField(backref='omds_language_language_fk_set', column_name='languageFkId', field='id', model=OmdsLanguage, null=True)
    lines_per_page = CharField(column_name='linesPerPage', null=True)
    manuscript_id = CharField(null=True)
    manuscripttype = IntegerField(null=True)
    miscellaneous_remarks = TextField(column_name='miscellaneousRemarks', null=True)
    nature_of_collection = IntegerField(null=True)
    nmm_details_fk = ForeignKeyField(column_name='nmmDetailsFkId', field='id', model=OmdsNmmDetails, null=True)
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
    scribefkid = ForeignKeyField(backref='omds_person_scribefkid_set', column_name='scribefkid', field='id', model=OmdsPerson, null=True)
    script_fk = ForeignKeyField(column_name='scriptFkId', field='id', model=OmdsScript, null=True)
    source_of_catalogue = IntegerField(null=True)
    specific_category_fk = ForeignKeyField(column_name='specificCategoryFkId', field='id', model=OmdsSpecificcategory, null=True)
    sub_commentatorfkid = ForeignKeyField(backref='omds_person_sub_commentatorfkid_set', column_name='subCommentatorfkid', field='id', model=OmdsPerson, null=True)
    subject1 = CharField(null=True)
    table_of_contents = CharField(null=True)
    total_no_of_folios = BigIntegerField(null=True)
    total_no_of_maps = BigIntegerField(null=True)
    trans_language = CharField(column_name='transLanguage', null=True)
    translatorfkid = ForeignKeyField(backref='omds_person_translatorfkid_set', column_name='translatorfkid', field='id', model=OmdsPerson, null=True)

    class Meta:
        table_name = 'omds_digital_manuscript'

class OmdsDigitalManuscriptFrame(BaseModel):
    digital_document_bean = TextField(column_name='digitalDocumentBean', null=True)
    digital_manuscript_fk = ForeignKeyField(column_name='digitalManuscriptFkId', field='id', model=OmdsDigitalManuscript)
    file_path = CharField(column_name='filePath')
    frame_order = IntegerField(null=True)
    id = BigAutoField()
    islast = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'omds_digital_manuscript_frame'

class OmdsDigitaldocument(BaseModel):
    digital_manuscript_fk = ForeignKeyField(column_name='digitalManuscriptFkId', field='id', model=OmdsDigitalManuscript, null=True)
    digital_manuscript_frame_fk = ForeignKeyField(column_name='digitalManuscriptFrameFkId', field='id', model=OmdsDigitalManuscriptFrame, null=True)
    id = BigAutoField()
    language = CharField(null=True)
    language_fk = ForeignKeyField(column_name='languageFkId', field='id', model=OmdsLanguage, null=True)
    recordtype = IntegerField(null=True)
    script = CharField(null=True)
    script_fk = ForeignKeyField(column_name='scriptFkId', field='id', model=OmdsScript, null=True)
    work_type = IntegerField(column_name='workType', null=True)

    class Meta:
        table_name = 'omds_digitaldocument'

class OmdsRolemaster(BaseModel):
    created_by = CharField(column_name='CreatedBy', null=True)
    created_date = DateTimeField(column_name='CreatedDate', null=True)
    description = CharField(column_name='Description', null=True)
    id = BigAutoField(column_name='Id')
    is_deleted = IntegerField(column_name='IsDeleted', null=True)
    modified_by = CharField(column_name='ModifiedBy', null=True)
    modified_date = DateTimeField(column_name='ModifiedDate', null=True)
    name = CharField(column_name='Name')
    row_version = IntegerField(column_name='RowVersion', null=True)

    class Meta:
        table_name = 'omds_rolemaster'

class WflLocationuserroledetails(BaseModel):
    user_info_fk_id = BigIntegerField(column_name='UserInfoFkId')
    valid_from_date = DateTimeField(column_name='ValidFromDate', constraints=[SQL("DEFAULT 1900-01-01 00:00:00")], null=True)
    valid_to_date = DateTimeField(column_name='ValidToDate', constraints=[SQL("DEFAULT 2199-12-12 00:00:00")], null=True)
    id = BigAutoField()
    locationmasterfkid = BigIntegerField()
    rolemasterfkid = ForeignKeyField(column_name='rolemasterfkid', field='id', model=OmdsRolemaster, null=True)
    userlogindetailsfkid = BigIntegerField(null=True)

    class Meta:
        table_name = 'wfl_locationuserroledetails'

class OmdsDigitaldocumentDetails(BaseModel):
    text = TextField(column_name='TEXT', null=True)
    attachment_file_path = CharField(column_name='attachmentFilePath', null=True)
    createdby = CharField(null=True)
    createddate = DateTimeField(null=True)
    digital_document_fk = ForeignKeyField(column_name='digitalDocumentFkId', field='id', model=OmdsDigitaldocument)
    id = BigAutoField()
    ismax = IntegerField(null=True)
    modifiedby = CharField(null=True)
    modifieddate = DateTimeField(null=True)
    rowversion = IntegerField(null=True)
    user_role_details_fk = ForeignKeyField(column_name='userRoleDetailsFkId', field='id', model=WflLocationuserroledetails, null=True)
    version = BigIntegerField(null=True)

    class Meta:
        table_name = 'omds_digitaldocument_details'

class OmdsDocumentComment(BaseModel):
    comment = TextField(null=True)
    commentedby = CharField(null=True)
    commentedon = CharField(null=True)
    digitalmanuscriptid = BigIntegerField(null=True)
    framefkid = ForeignKeyField(column_name='framefkid', field='id', model=OmdsDigitalManuscriptFrame, null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'omds_document_comment'

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

class OmdsManuscriptAuthormapper(BaseModel):
    authorfkid = ForeignKeyField(column_name='authorfkid', field='id', model=OmdsPerson, null=True)
    id = BigAutoField()
    manuscriptfkid = ForeignKeyField(column_name='manuscriptfkid', field='id', model=OmdsDigitalManuscript, null=True)

    class Meta:
        table_name = 'omds_manuscript_authormapper'

class OmdsManuscriptSpecificcategorymapper(BaseModel):
    id = BigAutoField()
    manuscriptfkid = BigIntegerField(null=True)
    specificcategoryfkid = BigIntegerField(null=True)

    class Meta:
        table_name = 'omds_manuscript_specificcategorymapper'

class OmdsTags(BaseModel):
    id = BigAutoField()
    isdeleted = UnknownField(null=True)  # bit
    name = CharField()

    class Meta:
        table_name = 'omds_tags'

class OmdsManuscriptTagmapper(BaseModel):
    id = BigAutoField()
    manuscriptfkid = BigIntegerField(null=True)
    tagsfkid = ForeignKeyField(column_name='tagsfkid', field='id', model=OmdsTags, null=True)

    class Meta:
        table_name = 'omds_manuscript_tagmapper'

class OmdsMenumaster(BaseModel):
    default_status = CharField(column_name='DefaultStatus', null=True)
    id = BigAutoField(column_name='Id')
    left_panel_link = CharField(column_name='LeftPanelLink', null=True)
    menu_level = IntegerField(column_name='MenuLevel', null=True)
    menu_link = CharField(column_name='MenuLink', null=True)
    menu_name = CharField(column_name='MenuName', null=True)
    menu_order = IntegerField(column_name='MenuOrder', null=True)
    parent_id = BigIntegerField(column_name='ParentId', null=True)
    request_id = CharField(column_name='RequestId', null=True)
    short_key = CharField(column_name='ShortKey', null=True)
    status_msg = CharField(column_name='StatusMsg', null=True)

    class Meta:
        table_name = 'omds_menumaster'

class OmdsPatha(BaseModel):
    id = BigAutoField()
    isdeleted = UnknownField(null=True)  # bit
    name = CharField()
    unicode_point = CharField(null=True)

    class Meta:
        table_name = 'omds_patha'

class OmdsSubject1(BaseModel):
    id = BigAutoField()
    isdeleted = UnknownField(null=True)  # bit
    name = CharField()
    unicode_point = CharField(null=True)

    class Meta:
        table_name = 'omds_subject1'

class OmdsUserlogindetails(BaseModel):
    created_by = CharField(column_name='CreatedBy', null=True)
    created_date = DateTimeField(column_name='CreatedDate', null=True)
    genrated_reset_password_date = DateTimeField(column_name='GenratedResetPasswordDate', null=True)
    id = BigAutoField(column_name='Id')
    login_id = CharField(column_name='LoginId')
    modified_by = CharField(column_name='ModifiedBy', null=True)
    modified_date = DateTimeField(column_name='ModifiedDate', null=True)
    password = CharField(column_name='Password', null=True)
    refrence_fk_id = BigIntegerField(column_name='RefrenceFkId', null=True)
    reset_password_id = CharField(column_name='ResetPasswordId', null=True)
    row_version = IntegerField(column_name='RowVersion', null=True)
    status = IntegerField(column_name='Status')
    type = IntegerField(column_name='Type')
    is_deleted = IntegerField(column_name='isDeleted', null=True)

    class Meta:
        table_name = 'omds_userlogindetails'

class OmdsUserroledetails(BaseModel):
    id = BigAutoField(column_name='Id')
    role_master_fk_id = BigIntegerField(column_name='RoleMasterFkId', null=True)
    user_login_details_fk_id = BigIntegerField(column_name='UserLoginDetailsFkId', null=True)

    class Meta:
        table_name = 'omds_userroledetails'

class RegistrationCode(BaseModel):
    date_created = DateTimeField()
    id = BigAutoField()
    token = CharField()
    username = CharField()

    class Meta:
        table_name = 'registration_code'

class Roles(BaseModel):
    authority = CharField(index=True)
    created_by = CharField(index=True, null=True)
    date_created = DateTimeField(index=True, null=True)
    id = BigAutoField()
    is_deleted = UnknownField(null=True)  # bit
    is_enabled = UnknownField(null=True)  # bit
    last_updated = DateTimeField(index=True, null=True)
    last_updated_by = CharField(null=True)
    role_description = CharField(null=True)
    role_name = CharField(index=True, null=True)
    version = BigIntegerField()

    class Meta:
        table_name = 'roles'

class Users(BaseModel):
    account_expired = UnknownField()  # bit
    account_locked = UnknownField()  # bit
    address = CharField(null=True)
    created_by = CharField(null=True)
    date_created = DateTimeField(null=True)
    email_address = CharField(null=True)
    enabled = UnknownField()  # bit
    first_name = CharField(null=True)
    id = BigAutoField()
    last_name = CharField(null=True)
    last_updated = DateTimeField(null=True)
    last_updated_by = CharField(null=True)
    mobile_number = CharField(null=True)
    password = CharField()
    password_expired = UnknownField()  # bit
    phone_number = CharField(null=True)
    prev_login_date = BigIntegerField(null=True)
    username = CharField(unique=True)
    version = BigIntegerField()

    class Meta:
        table_name = 'users'

class UsersRoles(BaseModel):
    roles = ForeignKeyField(column_name='roles_id', field='id', model=Roles)
    users = ForeignKeyField(column_name='users_id', field='id', model=Users)

    class Meta:
        table_name = 'users_roles'
        indexes = (
            (('users', 'roles'), True),
        )
        primary_key = CompositeKey('roles', 'users')

class WflCurrentprocessbranchdetails(BaseModel):
    current_process_details_fk_id = IntegerField(column_name='CurrentProcessDetailsFkId')
    id = AutoField(column_name='Id')
    next_fk_id = IntegerField(column_name='NextFkId', null=True)
    previous_fk_id = IntegerField(column_name='PreviousFkId', null=True)

    class Meta:
        table_name = 'wfl_currentprocessbranchdetails'

class WflCurrentprocessccdetails(BaseModel):
    current_process_details_fk_id = IntegerField(column_name='CurrentProcessDetailsFkId')
    id = AutoField(column_name='Id')
    status = IntegerField(column_name='Status')
    user_info_fk_id = IntegerField(column_name='UserInfoFkId')

    class Meta:
        table_name = 'wfl_currentprocessccdetails'

class WflCurrentprocesschecklistanswer(BaseModel):
    checklist_item_fk_id = IntegerField(column_name='ChecklistItemFkId')
    checklist_item_type_details_fk_id = IntegerField(column_name='ChecklistItemTypeDetailsFkId')
    created_by = CharField(column_name='CreatedBy')
    created_date = DateTimeField(column_name='CreatedDate')
    current_process_details_fk_id = IntegerField(column_name='CurrentProcessDetailsFkId')
    high_value = IntegerField(column_name='HighValue')
    id = AutoField(column_name='Id')
    low_value = IntegerField(column_name='LowValue', null=True)
    modified_by = CharField(column_name='ModifiedBy')
    modified_date = DateTimeField(column_name='ModifiedDate')
    row_version = IntegerField(column_name='RowVersion')

    class Meta:
        table_name = 'wfl_currentprocesschecklistanswer'

class WflCurrentprocesschecklistdetails(BaseModel):
    check_list_master_fk_id = IntegerField(column_name='CheckListMasterFkId')
    current_process_details_fk_id = IntegerField(column_name='CurrentProcessDetailsFkId')
    id = AutoField(column_name='Id')

    class Meta:
        table_name = 'wfl_currentprocesschecklistdetails'

class WflCurrentprocessdetails(BaseModel):
    completed_on = DateTimeField(column_name='CompletedOn', null=True)
    current_process_master_fk_id = IntegerField(column_name='CurrentProcessMasterFkId')
    is_authorize_button = IntegerField(column_name='IsAuthorizeButton')
    is_return_button = IntegerField(column_name='IsReturnButton')
    is_save_button = IntegerField(column_name='IsSaveButton')
    is_terminate_button = IntegerField(column_name='IsTerminateButton')
    is_user_role_id = IntegerField(column_name='IsUserRoleId')
    level = IntegerField(column_name='Level')
    location_user_role_fk_id = IntegerField(column_name='LocationUserRoleFkId')
    process_time_out = IntegerField(column_name='ProcessTimeOut')
    screen_name = CharField(column_name='ScreenName')
    started_on = DateTimeField(column_name='StartedOn', null=True)
    status = IntegerField(column_name='Status')
    url = CharField(column_name='Url')
    id = BigAutoField()

    class Meta:
        table_name = 'wfl_currentprocessdetails'

class WflCurrentprocessmaster(BaseModel):
    description = CharField(column_name='Description', null=True)
    location_master_fk_id = IntegerField(column_name='LocationMasterFkId')
    name = CharField(column_name='Name')
    process_master_fk_id = IntegerField(column_name='ProcessMasterFkId')
    reference_fk_id = IntegerField(column_name='ReferenceFkId')
    id = BigAutoField()

    class Meta:
        table_name = 'wfl_currentprocessmaster'

class WflHistoryprocessbranchdetails(BaseModel):
    history_process_details_fk_id = IntegerField(column_name='HistoryProcessDetailsFkId')
    id = AutoField(column_name='Id')
    next_fk_id = IntegerField(column_name='NextFkId', null=True)
    previous_fk_id = IntegerField(column_name='PreviousFkId', null=True)

    class Meta:
        table_name = 'wfl_historyprocessbranchdetails'

class WflHistoryprocessccdetails(BaseModel):
    history_process_details_fk_id = IntegerField(column_name='HistoryProcessDetailsFkId')
    id = AutoField(column_name='Id')
    status = IntegerField(column_name='Status')
    user_info_fk_id = IntegerField(column_name='UserInfoFkId')

    class Meta:
        table_name = 'wfl_historyprocessccdetails'

class WflHistoryprocesschecklistanswer(BaseModel):
    checklist_item_fk_id = IntegerField(column_name='ChecklistItemFkId')
    checklist_item_type_details_fk_id = IntegerField(column_name='ChecklistItemTypeDetailsFkId')
    created_by = CharField(column_name='CreatedBy')
    created_date = DateTimeField(column_name='CreatedDate')
    high_value = IntegerField(column_name='HighValue')
    history_process_details_fk_id = IntegerField(column_name='HistoryProcessDetailsFkId')
    id = AutoField(column_name='Id')
    low_value = IntegerField(column_name='LowValue', null=True)
    modified_by = CharField(column_name='ModifiedBy')
    modified_date = DateTimeField(column_name='ModifiedDate')
    row_version = IntegerField(column_name='RowVersion')

    class Meta:
        table_name = 'wfl_historyprocesschecklistanswer'

class WflHistoryprocesschecklistdetails(BaseModel):
    check_list_master_fk_id = IntegerField(column_name='CheckListMasterFkId')
    history_process_details_fk_id = IntegerField(column_name='HistoryProcessDetailsFkId')
    id = AutoField(column_name='Id')

    class Meta:
        table_name = 'wfl_historyprocesschecklistdetails'

class WflHistoryprocessdetails(BaseModel):
    history_process_master_fk_id = IntegerField(column_name='HistoryProcessMasterFkId')
    id = AutoField(column_name='Id')
    is_authorize_button = IntegerField(column_name='IsAuthorizeButton')
    is_return_button = IntegerField(column_name='IsReturnButton')
    is_save_button = IntegerField(column_name='IsSaveButton')
    is_terminate_button = IntegerField(column_name='IsTerminateButton')
    is_user_role_id = IntegerField(column_name='IsUserRoleId')
    level = IntegerField(column_name='Level')
    location_user_role_fk_id = IntegerField(column_name='LocationUserRoleFkId')
    process_time_out = IntegerField(column_name='ProcessTimeOut')
    screen_name = CharField(column_name='ScreenName')
    status = IntegerField(column_name='Status')
    url = CharField(column_name='Url')

    class Meta:
        table_name = 'wfl_historyprocessdetails'

class WflHistoryprocessmaster(BaseModel):
    description = CharField(column_name='Description', null=True)
    id = AutoField(column_name='Id')
    location_master_fk_id = IntegerField(column_name='LocationMasterFkId')
    name = CharField(column_name='Name')
    process_master_fk_id = IntegerField(column_name='ProcessMasterFkId')

    class Meta:
        table_name = 'wfl_historyprocessmaster'

class WflLocationlevelmaster(BaseModel):
    description = CharField(column_name='Description', null=True)
    icon_image_name = CharField(column_name='IconImageName', null=True)
    id = BigAutoField(column_name='Id')
    level_number = BigIntegerField(column_name='LevelNumber')
    name = CharField(column_name='Name')

    class Meta:
        table_name = 'wfl_locationlevelmaster'

class WflLocationmaster(BaseModel):
    description = CharField(column_name='Description')
    is_deleted = IntegerField(column_name='IsDeleted')
    is_workflow_enabled = IntegerField(column_name='IsWorkflowEnabled', null=True)
    level_fk = ForeignKeyField(column_name='LevelFkId', field='id', model=WflLocationlevelmaster, null=True)
    name = CharField(column_name='Name')
    parent_fk = ForeignKeyField(column_name='ParentFkId', field='id', model='self', null=True)
    createdby = CharField(null=True)
    createddate = DateTimeField(null=True)
    id = BigAutoField()
    modifiedby = CharField(null=True)
    modifieddate = DateTimeField(null=True)
    rowversion = IntegerField(null=True)

    class Meta:
        table_name = 'wfl_locationmaster'

class WflLocationprocessbranchdetails(BaseModel):
    id = AutoField(column_name='Id')
    location_process_details_fk_id = IntegerField(column_name='LocationProcessDetailsFkId')
    next_fk_id = IntegerField(column_name='NextFkId', null=True)
    previous_fk_id = IntegerField(column_name='PreviousFkId', null=True)

    class Meta:
        table_name = 'wfl_locationprocessbranchdetails'

class WflLocationprocesschecklistdetails(BaseModel):
    check_list_master_fk_id = IntegerField(column_name='CheckListMasterFkId')
    id = AutoField(column_name='Id')
    location_process_details_fk_id = IntegerField(column_name='LocationProcessDetailsFkId')

    class Meta:
        table_name = 'wfl_locationprocesschecklistdetails'

class WflLocationprocessdetails(BaseModel):
    id = AutoField(column_name='Id')
    is_authorize_button = IntegerField(column_name='IsAuthorizeButton')
    is_return_button = IntegerField(column_name='IsReturnButton')
    is_save_button = IntegerField(column_name='IsSaveButton')
    is_terminate_button = IntegerField(column_name='IsTerminateButton')
    level = IntegerField(column_name='Level')
    location_process_master_fk_id = IntegerField(column_name='LocationProcessMasterFkId')
    process_time_out = IntegerField(column_name='ProcessTimeOut')
    role_master_fk_id = IntegerField(column_name='RoleMasterFkId')
    screen_name = CharField(column_name='ScreenName')
    status = IntegerField(column_name='Status')
    url = CharField(column_name='Url')

    class Meta:
        table_name = 'wfl_locationprocessdetails'

class WflLocationprocessmaster(BaseModel):
    description = CharField(column_name='Description', null=True)
    id = AutoField(column_name='Id')
    location_master_fk_id = IntegerField(column_name='LocationMasterFkId')
    name = CharField(column_name='Name')
    process_master_fk_id = IntegerField(column_name='ProcessMasterFkId')

    class Meta:
        table_name = 'wfl_locationprocessmaster'

class WflProcessbranchdetails(BaseModel):
    id = AutoField(column_name='Id')
    next_fk_id = IntegerField(column_name='NextFkId', null=True)
    previous_fk_id = IntegerField(column_name='PreviousFkId', null=True)
    process_details_fk_id = IntegerField(column_name='ProcessDetailsFkId')

    class Meta:
        table_name = 'wfl_processbranchdetails'

class WflProcesschecklistdetails(BaseModel):
    check_list_master_fk_id = IntegerField(column_name='CheckListMasterFkId')
    id = AutoField(column_name='Id')
    process_details_fk_id = IntegerField(column_name='ProcessDetailsFkId')

    class Meta:
        table_name = 'wfl_processchecklistdetails'

class WflProcessdetails(BaseModel):
    id = AutoField(column_name='Id')
    is_authorize_button = IntegerField(column_name='IsAuthorizeButton')
    is_return_button = IntegerField(column_name='IsReturnButton')
    is_save_button = IntegerField(column_name='IsSaveButton')
    is_terminate_button = IntegerField(column_name='IsTerminateButton')
    level = IntegerField(column_name='Level')
    process_master_fk_id = IntegerField(column_name='ProcessMasterFkId')
    process_time_out = IntegerField(column_name='ProcessTimeOut')
    role_master_fk_id = IntegerField(column_name='RoleMasterFkId')
    screen_name = CharField(column_name='ScreenName')
    status = IntegerField(column_name='Status')
    url = CharField(column_name='Url')

    class Meta:
        table_name = 'wfl_processdetails'

class WflProcessmaster(BaseModel):
    description = CharField(column_name='Description', null=True)
    id = AutoField(column_name='Id')
    name = CharField(column_name='Name')

    class Meta:
        table_name = 'wfl_processmaster'

class Workflowcountentityvo(BaseModel):
    cnt_direct = BigIntegerField(column_name='cntDirect', null=True)
    cnt_role = BigIntegerField(column_name='cntRole')
    id = BigAutoField()
    process_description = CharField(column_name='processDescription')
    process_id = BigIntegerField(column_name='processId', null=True)

    class Meta:
        table_name = 'workflowcountentityvo'

