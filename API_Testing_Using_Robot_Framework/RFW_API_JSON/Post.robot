*** Settings ***
Library           RequestsLibrary

*** Variables ***
${BASE_URL}       https://api.example.com
${ENDPOINT}       /create
${TOKEN}          Bearer your_access_token_here
${HEADERS}        Content-Type=application/json    Authorization=${TOKEN}

*** Test Cases ***
Create Request With JSON And Bearer Token
    [Documentation]    Sends a POST request with JSON body using Bearer token authentication.
    Create Session     myapi    ${BASE_URL}
    ${body}=           Create Dictionary    name=Test Name    email=test@example.com    role=admin
    ${response}=       Post Request    myapi    ${ENDPOINT}    json=${body}    headers=${HEADERS}
    Should Be Equal As Integers    ${response.status_code}    201
    Log To Console     Response: ${response.json()}
