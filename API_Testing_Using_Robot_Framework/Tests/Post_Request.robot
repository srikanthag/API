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
TC:001 Post request Test
    [tags]  Demo
    [Documentation]  Post request Test
    Create Session    session1   ${url}     disable_warnings=1
    ${endpoint}    set variable     /api/users
    ${body}=    create dictionary    name=srikanth1238     job=SW engineer1238
    ${response}=     Post On Session     session1        ${endpoint}     data=${body}
    Log To Console       ${response.status_code}
    Log To Console       ${response.content}

    # Validation

    ${status_code}=  convert to string    ${response.status_code}
    Should Be Equal     ${Status_code}    201

    ${json_response}=      Convert String to Json      ${response.content}
    ${contents}=        get value from json     ${json_response}     ${id_path}
    ${contents}     convert to string   ${contents}
    Should Not Be Empty      ${contents}
    log     ${contents}






