import React from 'react';
import "./Login.css"
import logo from '../../img/logo.png';
import GoogleLogin from 'react-google-login';
import API from '../../api/Api.jsx';

export default class Login extends React.Component{
    constructor(props) {
        super(props);
        this.state = { accessCodeEntered: false, accessCodeError: true };
    }
    
    onGoogleLoginSuccess = (response) => {
        const idToken = response.tokenId;
        const data = {
            email: response.profileObj.email,
            first_name: response.profileObj.givenName,
            last_name: response.profileObj.familyName
        };
    
        this.validateTokenAndObtainSession({ data, idToken });
    }

    onGoogleLoginFailure = (response) => {
        console.log("Error: google login failed");
    }

    validateTokenAndObtainSession({data, idToken}) {
        API.login(idToken, data);
    }

    validateAccessToken = () => {
        let notValid = !(document.getElementById("access-code-input").value === "ABC123"); // call api function to validate here
        this.setState({ accessCodeEntered: true, accessCodeError: notValid });
    }


    render() {
        return (
            <div className="page">
                <div className="welcome-banner">
                    <img className="logo-image" alt="logo" src={logo} id="login-img"></img>
                    <p className="welcome-text">Welcome to the BT Mentorship Map!</p>
                </div>

                <div className="login-box">
                    <p className="login-box-header">Log in to your account</p>

                    <GoogleLogin
                        className="login-box-google-button"
                        clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}  // your Google app client ID
                        buttonText="Continue with Google"
                        onSuccess={this.onGoogleLoginSuccess} // perform your user logic here
                        onFailure={this.onGoogleLoginFailure} // handle errors here
                        isSignedIn={true}
                    />
                    
                    <p className="login-box-guidance-text">OR</p>

                    {(this.state.accessCodeError ? 
                        <div>
                            <p className="login-box-header login-box-header--sign-up">Sign up with access code</p>
                            {(!this.state.accessCodeEntered ?
                                <input className="login-box-input" id="access-code-input" type="text" placeholder="Enter access code" onSubmit={this.validateAccessToken}/>
                                :
                                <>
                                    <input className="login-box-input login-box-input--error" id="access-code-input" type="text" placeholder="Enter access code" onSubmit={this.validateAccessToken}/>
                                    <p className="login-box-input-hint">Invalid access code, try again.</p>
                                </>
                            )}
                            <br></br>
                            <button className="login-box-submit" onClick={this.validateAccessToken}>Continue</button>
                        </div>
                        :
                        <div>
                            <p className="login-box-header login-box-header--sign-up">Access code validated</p>
                            <GoogleLogin
                                className="login-box-google-button"
                                clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}  // your Google app client ID
                                buttonText="Sign up with Google"
                                onSuccess={this.onGoogleLoginSuccess} // perform your user logic here
                                onFailure={this.onGoogleLoginFailure} // handle errors here
                                isSignedIn={true}
                            />
                        </div>
                    )}
                </div>  
            </div>
        )
    }  

 
}