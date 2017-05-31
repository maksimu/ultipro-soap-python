from zeep import Client as Zeep
from zeep import xsd

endpoint = '/EmployeeAddress?wsdl'

def find_addresses(client, query):
    zeep_client = Zeep(client.base_url + endpoint)
    return zeep_client.service.FindAddresses(
        _soapheaders=[client.session_header],
        query=query)

def get_address_by_employee_identifier(client, employee_identifier):
    zeep_client = Zeep(client.base_url + endpoint)
    if 'EmployeeNumber' in employee_identifier:
        element = zeep_client.get_element('ns6:EmployeeNumberIdentifier')
        obj = element(**employee_identifier)
    elif 'EmailAddress' in employee_identifier:
        element = zeep_client.get_element('ns6:EmailAddressIdentifier')
        obj = element(**employee_identifier)

    return zeep_client.service.GetAddressByEmployeeIdentifier(
        _soapheaders=[client.session_header],
        employeeIdentifier=obj)
