import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useEffect, useState } from 'react';
import './App.css';
import Navbar from './Navbar';
import RadarChart from './RadarChart';

function Dashboard() {
  const [user, setUser] = useState(null);
  const [progress, setProgress] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/users/1')
      .then(res => {
        setUser(res.data);
      })
  }, []);

  useEffect(() => {
    if (user && user.id) {
      axios.get(`http://localhost:8000/progress/${user.id}`)
        .then(res => {
          setProgress(res.data.progress.map(Number));
        })
    }
  }, [user]);

  if (!user) return <div>Loading...</div>;

  const goals = ['Programming', 'Lifting', 'Networing', 'School', 'Money'];

  return (
    <div>
      <Navbar />
      <p>Name: {user.username}</p>
      <RadarChart labels={goals} dataPoints={progress} />
    </div>
  );
}

export default Dashboard;