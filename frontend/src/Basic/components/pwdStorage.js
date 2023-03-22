


function hasToken(){
    return(sessionStorage.getItem('authtoken'))
}

function expireToken(){
    sessionStorage.removeItem('authtoken')
};

function authHeader(){
    let headers = new Headers();
    headers.append('Authorization', hasToken())
    return(
        headers
    )
};

export default {expireToken,hasToken, authHeader}