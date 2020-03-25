import React from "react";
import "antd/dist/antd.css";
import "./index.css";
import {Button, Layout} from "antd";
import logo from './streetcard-logo.png';
import {HomeOutlined, LogoutOutlined} from '@ant-design/icons';

const {Header} = Layout;

export default class HeaderComponent extends React.Component {

    constructor(props) {
        super(props);
        this.logIn = this.logIn.bind(this);
        this.logOut = this.logOut.bind(this);
    }

    logIn() {
        this.props.handleSuccessfulLoginAction();
    }

    logOut() {
        this.props.handleSuccessfulLogoutAction();
    }

    render() {
        if (this.props.loginPageStatus === "LOGIN_HEADER") {
            return (
                <Header className="site-layout-header">
                    <img className="logo" src={logo}/>
                </Header>
            );
        } else if (this.props.loggedInStatus === "NOT_LOGGED_IN") {
            return (
                <Header className="site-layout-header">
                    <img className="logo" src={logo}/>
                    <Button onClick={this.logIn} type="link" className="homebutton" key="2">
                        <HomeOutlined/>
                    </Button>
                </Header>
            );
        } else {
            return (
                <Header className="site-layout-header">
                    <img className="logo" src={logo}/>
                    <Button onClick={this.logOut} type="link" className="homebutton" key="2">
                        <LogoutOutlined/>
                    </Button>
                </Header>
            )
                ;
        }
    }
}