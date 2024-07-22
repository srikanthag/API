*** Settings ***

Library  Collections
Library  String
Library  JSONLibrary
Library  RequestsLibrary

*** Variables ***
${url}  https://reqres.in/
${pagepath}  S.page
${id_path}  S.id

*** Test Cases ***
TC:001 Delete request Test
    [tags]  Demo
    [Documentation]  Delete request Test
    Create Session    session1   ${url}     disable_warnings=1
    ${endpoint}    set variable     /api/users/2
    ${response}=     Delete On Session     session1        ${endpoint}
    Log To Console       ${response.status_code}
    Log To Console       ${response.content}

    # Validation

    ${status_code}=  convert to string    ${response.status_code}
    Should Be Equal     ${Status_code}    204

