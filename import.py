import requests
import sys

scantype = str(sys.argv[1])
importstatus = str(sys.argv[2])
reportfile = str(sys.argv[3])
projectname = str(sys.argv[4])
authtoken = str(sys.argv[5])

def uploadToDefectDojo(filename, is_new_import):
    multipart_form_data = {
        'file': (filename, open(filename, 'rb')),
        'scan_type': (None, scantype),
        'product_name': (None, 'Konomo'), 
        'engagement_name': (None, projectname)
    }
    defect_dojo_domain = "https://defectdojo.hack.cloudnative.nttdatauk.cloud"
    if is_new_import == "True":
       uri = '/api/v2/import-scan/'
    else:   
       uri = '/api/v2/reimport-scan/'
    response = requests.post(
        defect_dojo_domain + uri,
        files=multipart_form_data,
        headers={
            'Authorization': authtoken
        }
    )
    print(response.text)
    print(response.status_code)

uploadToDefectDojo(reportfile, importstatus)
