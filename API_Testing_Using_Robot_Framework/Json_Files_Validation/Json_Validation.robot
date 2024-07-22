*** Settings ***

Library  Collections
Library  String
Library  JSONLibrary
Library  RequestsLibrary
Library  OperatingSystem


*** Variables ***
${url}  https://reqres.in/
${pagepath}  S.page
${id_path}  S.id

*** Test Cases ***
TC:001 Load and get Json data
    [tags]  Demo
    [Documentation]  Load and get Json data
    ${filepath}     set variable        ${EXECDIR}\\API_Testing\\Json_Files_Validation\\data.json
    Log To Console       ${filepath}

    ${json_object}=     Get File        ${filepath}
    ${valueof}      Evaluate    json.loads('''${json_object}''')    json
    Log To Console      ${valueof["name"]}
    ${name}     set variable        ${valueof["name"]}
    Should Be Equal     ${name}    srikanth