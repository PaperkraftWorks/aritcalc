import { LogoutURL, LoginURL, PerformOperationURL, LastRecordURL } from './constants'
import storageToken from './pwdStorage';
import authHeader from './pwdStorage';
import expireToken from './pwdStorage';
import hasToken from './pwdStorage';
let base64 = require('base-64');


function performLogin(username, pwd){
    let headers = new Headers();
    headers.append('Authorization', 'Basic' + base64.encode(username+":"+pwd))
    fetch(
        LoginURL,
        {
            method: 'POST',
            headers: headers,
        }
    )
    .then(response => response.json() )
    .then (json =>storageToken(json.get('token')))
}

function performLogout(){
    fetch(
        LogoutURL,
        {
            method: 'POST',
            headers: authHeader()
        }
    )
    .then(expireToken())
}

function performOperation(operation){

    fetch(
        PerformOperationURL,
        {
            method: 'POST',
            headers: authHeader(),
            data: operation
        }

    ).then(response => response.json())
    .then(json => console.log(json))

}

function performLastRecord(){
    fetch(
        LastRecordURL,
        {
            method: 'GET',
            headers: authHeader()
        }
    ).then(response => response.json())
    .then(json => console.log(json))
    
}

export default {performLastRecord, performOperation, performLogin, performLogout}