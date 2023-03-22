import {LoginURL} from './constants'
import storageToken from '../storage/storagetoken';
let base64 = require('base64')

function performLogin(username, pwd){
    let headers = new Headers();
    headers.append('Authorization', 'Basic' + base64.encode(username+":"+pwd))
    debugger
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

export default performLogin;