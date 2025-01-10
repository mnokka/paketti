*** Settings ***
Library  RequestsLibrary
Library  SeleniumLibrary

*** Variables ***
${BASE_URL}  http://${SUT_IP_ADDRESS}

*** Test Cases ***
Verify Backend Health
    GET  ${BASE_URL}/health
    Should Be Equal As Strings  ${status_code}  200

Verify User Login
    Open Browser  ${BASE_URL}/login  chrome
    Input Text  id:username  test_user
    Input Text  id:password  securepassword
    Click Button  id:login
    Page Should Contain  Welcome, test_user
