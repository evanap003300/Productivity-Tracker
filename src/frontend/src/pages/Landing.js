import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './App.css';

function Landing() {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://localhost:8000/login/', {
        username: username,
        password: password
      });

      if (response.data.message === "Login successful") {
        navigate('/Dashboard');
      } else {
        alert('Incorrect username or password');
      }
    } catch (error) {
      alert("Something went wrong. Please try again.");
    }
  };

  return (
    <div>
      <p>Username: </p>
      <input type="text" onChange={e => setUsername(e.target.value)} />
      <p>Password: </p>
      <input type="password" onChange={e => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
      <button>Make Account</button>
    </div>
  );
}

export default Landing;