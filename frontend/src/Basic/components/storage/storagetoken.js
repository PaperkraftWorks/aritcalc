function storageToken(token){
    sessionStorage.setItem('authtoken', `Token ${token}`)
};

export default storageToken;