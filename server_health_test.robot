*** Settings ***
Library  RequestsLibrary
Library  SeleniumLibrary

*** Variables ***
${BASE_URL}  http://localhost:5000

*** Test Cases ***
Verify Backend Health
    GET  ${BASE_URL}/health
    Should Be Equal As Strings  ${status_code}  200


