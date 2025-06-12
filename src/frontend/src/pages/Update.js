import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';
import './App.css';
import Navbar from './Navbar';

function Update() {
  const [followerValue, setFollowerValue] = useState('');
  const [connectionsValue, setConnections] = useState('');
  const [programmingHours, setProgrammingHours] = useState('');
  const [bodyWeight, setBodyWeight] = useState('');
  const [benchMax, setBenchMax] = useState('');
  const [squatReps, setSquatReps] = useState('');
  const [gpa, setGPA] = useState('');
  const [money, setMoney] = useState('');

  const userId = 1;

  const handlePut = async (url, data, fieldName) => {
    try {
      const response = await axios.put(`http://localhost:8000${url}`, data);
      alert(`${fieldName} updated successfully!`);
    } catch (error) {
      alert(`Failed to update ${fieldName}`);
    }
  };

  return (
    <div>
      <Navbar />

      <p>Instagram Followers:</p>
      <input type="number" onChange={e => setFollowerValue(e.target.value)} />
      <button onClick={() => handlePut(`/users/update-followers/${userId}`, { ig_followers: parseInt(followerValue) }, "Instagram Followers")}>Update Followers</button>

      <p>LinkedIn Connections:</p>
      <input type="number" onChange={e => setConnections(e.target.value)} />
      <button onClick={() => handlePut(`/users/update-connections/${userId}`, { linkedin_connections: parseInt(connectionsValue) }, "LinkedIn Connections")}>Update Connections</button>

      <p>Programming Hours:</p>
      <input type="number" onChange={e => setProgrammingHours(e.target.value)} />
      <button onClick={() => handlePut(`/users/update-programming/${userId}`, { programming_hours: parseInt(programmingHours) }, "Programming Hours")}>Update Programming</button>

      <p>Body Weight:</p>
      <input type="number" onChange={e => setBodyWeight(e.target.value)} />

      <p>Bench Press Max:</p>
      <input type="number" onChange={e => setBenchMax(e.target.value)} />

      <p>Squat Reps:</p>
      <input type="number" onChange={e => setSquatReps(e.target.value)} />

      <button onClick={() => handlePut(
        `/users/update-lifting/${userId}`,
        {
          body_weight: parseInt(bodyWeight),
          bench_max: parseInt(benchMax),
          squat_max: parseInt(squatReps)
        },
        "Lifting Stats"
      )}>Update Lifting</button>

      <p>GPA:</p>
      <input type="number" step="0.01" onChange={e => setGPA(e.target.value)} />
      <button onClick={() => handlePut(`/users/update-gpa/${userId}`, { gpa: parseFloat(gpa) }, "GPA")}>Update GPA</button>

      <p>Money:</p>
      <input type="number" onChange={e => setMoney(e.target.value)} />
      <button onClick={() => handlePut(`/users/update-money/${userId}`, { money: parseInt(money) }, "Money")}>Update Money</button>
    </div>
  );
}

export default Update;