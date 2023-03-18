
function Menu(userName='Macadamia',userBalance='100') {
    return (
        <div className="col-md-3">
            <div className="card card-primary">
                <div className="card-header">
                    <h3 className="card-title">User: {userName}</h3>
                    <div className="card-tools">
                        <button type="button" className="btn btn-tool" data-card-widget="collapse"
                        ><i className="fas fa-minus"></i>
                        </button>
                    </div>
                </div>
                <div className="card-body" style={{ display: 'block' }}>
                   Balance: $ {userBalance}
                </div>

            </div>

        </div>
    )
}
export default Menu;