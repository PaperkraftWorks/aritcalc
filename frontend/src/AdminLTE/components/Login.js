
function Login() {
    return (
        <div>
            <div className="centerfy">
            <div className="col-md-6">

                <div className="card card-info">
                    <div className="card-header ">
                        <h3 className="card-title">Arithmetic Calculator</h3>
                        <br></br>
                        <h3 className="card-title">Login Access</h3>
                    </div>
                    <form className="form-horizontal">
                        <div className="card-body">
                            <div className="form-group row">
                                <label htmlFor="inputEmail3" className="col-sm-2 col-form-label">Email</label>
                                <div className="col-sm-10">
                                    <input type="email" className="form-control" id="inputEmail3" placeholder="user@domain.com"></input>
                                </div>
                            </div>
                            <div className="form-group row">
                                <label htmlFor="inputPassword3" className="col-sm-2 col-form-label">Password</label>
                                <div className="col-sm-10">
                                    <input type="password" className="form-control" id="inputPassword3" placeholder="******"></input>
                                </div>
                            </div>
                            <div className="form-group row">
                                <div className="offset-sm-2 col-sm-10">
                                    <div className="form-check">
                                        <input type="checkbox" className="form-check-input" id="exampleCheck2"></input>
                                        <label className="form-check-label" htmlFor="exampleCheck2">Remember me</label>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div className="card-footer">
                            <button type="submit" className="btn btn-default ">Cancel</button>
                            <button type="submit" className="btn btn-info float-right">Sign in</button>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </div>
    );
}

export default Login