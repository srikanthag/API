*** Settings ***

Library  Collections
Library  String
Library  JSONLibrary
Library  RequestsLibrary

*** Variables ***
${url}  https://reqres.in/
${pagepath}  S.page

*** Test Cases ***
TC:001 Get Test Title and Status code from API
    [tags]  Demo
    [Documentation]  Get Test Title and Status code from API
    Create Session    session1   ${url}
    ${endpoint}    set variable     /api/users?page=2
    ${response}=    get on session    session1    ${endpoint}
    Log To Console      ${response.headers}
    Log To Console       ${response.status_code}
    Log To Console       ${response.content}
    log     ${response.content}

    # Validation

    ${status_code}=  convert to string    ${response.status_code}
    Should Be Equal     ${Status_code}    200

    ${jason_response}=  Convert String to Json      ${response.content}
    ${contents}     get value from json     ${jason_response}   ${pagepath}
    ${contents}     convert to string   ${contents}
    ${contents}     Remove String Using Regexp      ${contents}     ['\\[\\],]

    ${hearde_value}     get from dictionary     ${response.headers}     Content-Type
    Should Be Equal     ${hearde_value}    application/json; charset=utf-8






























