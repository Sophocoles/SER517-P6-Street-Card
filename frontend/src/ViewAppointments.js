import React from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import './index.css';
import {Form, Button, Icon} from 'antd';
import Header from './Header'
import StreetCardFooter from './StreetCardFooter'
import WrappedSetAppointments from "./SetAppointments";

class ViewAppointments extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            items: [],
            isLoaded: false,
        }
      this.handleSuccessfulLogoutAction = this.handleSuccessfulLogoutAction.bind(this);
    }

  handleSubmit = e => {
    e.preventDefault();

    this.props.form.validateFields((err, fieldsValue) => {
      if (err) {
        return;
      }

    });
  };


  componentDidMount() {
    /* fetch('http://127.0.0.1:8000/homeless/' + this.props.homelessPersonId + '/appointment/' , {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('token')}`
          },
        })
        .then(res => {
          if (res.status == 200) {
            console.log("STATUS", res.status)
            res.json().then(json=>{
              this.setState({
                isLoaded: true,
                items: json
              })
            })
              
          }
          else{
            console.log("STATUS", res.status)
            if(window.confirm("Error, invalid id: "+(res.status).toString())){
              this.props.history.push('/socialWorkerRegister');
            }else{
              res.json().then(json=>{
                this.setState({
                  isLoaded: true,
                  items: json
                })
            })
              
          } 
          }
         
          
      });*/

  }


  handleSuccessfulLogoutAction() {
    this.props.handleLogout();
    this.props.history.push('/login');
  }
  
  render() {
      const {isLoaded, items} = this.state;
      const { getFieldDecorator } = this.props.form;
        const formItemLayout = {
          labelCol: {
            xs: { span: 24 },
            sm: { span: 8 },
          },
          wrapperCol: {
            xs: { span: 24 },
            sm: { span: 16 },
          },
        };
    const config = {
      rules: [{ type: 'object', required: true, message: 'Please select time!' }],
    };
    return (
        <div>
          <Header 
                  handleSuccessfulLogoutAction={this.handleSuccessfulLogoutAction}
                  loggedInStatus={this.props.loggedInStatus}
          />
      <Form {...formItemLayout} onSubmit={this.handleSubmit} className="view-appointment">
          <h1>Appointment Details:</h1>
          <Form.Item >
        <div>{items.map(item => (<li key={item.PersonalId}>Personal-Id : {item.personalId} | Appointment-Id :
            {item.appointmentId} | Venue : {item.venue} | ServiceProvider : {item.serviceProvider} |
            DateTime : {item.DateTime}</li>))}</div>
       </Form.Item>
        <Form.Item
          wrapperCol={{
            xs: { span: 24, offset: 0 },
            sm: { span: 16, offset: 8 },
          }}
        >
          <Button type="primary" htmlType="Edit Appointment">
            Edit Appointment
          </Button>
        </Form.Item>
          <Form.Item
          wrapperCol={{
            xs: { span: 24, offset: 0 },
            sm: { span: 16, offset: 8 },
          }}
        >
          <Button type="primary" htmlType="back">
              <Icon type="left" />
            Back
          </Button>
        </Form.Item>
      </Form>
              <StreetCardFooter/>
          </div>
    );
  }
}

const WrappedViewAppointments = Form.create({ name: 'time_related_controls' })(ViewAppointments);


export default WrappedViewAppointments;
