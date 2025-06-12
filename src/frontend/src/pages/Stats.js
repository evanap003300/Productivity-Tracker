import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useEffect, useState } from 'react';
import './App.css';
import Navbar from './Navbar';

function Dashboard() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/users/1')
      .then(res => {
        setUser(res.data);
      })
  }, []);

  if (!user) return <div>Loading...</div>;


  return (
    <div>
      <Navbar />
      <p>Username: {user.username}</p>
      <p>Programming Hours Done: {user.programming_hours_done}</p>
      <p>Body Weight: {user.body_weight}</p>
      <p>Bench Press Max: {user.bench_press_max}</p>
      <p>Squat Reps: {user.squat_reps}</p>
      <p>Instagram Followers: {user.ig_followers}</p>
      <p>LinkedIn Connections: {user.linkedin_connections}</p>
      <p>GPA: {user.gpa}</p>
      <p>Money: ${user.money}</p>
    </div>
  );
}

export default Dashboard;