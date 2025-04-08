import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://organic-giggle-5v65wpxw67x2p7rj-8000.app.github.dev/api/workouts/')
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div>
      <h1>Workouts</h1>
      {workouts.length > 0 ? (
        <ul>
          {workouts.map(workout => (
            <li key={workout._id}>{workout.name || 'Unnamed Workout'} - {workout.description || 'No Description'}</li>
          ))}
        </ul>
      ) : (
        <p>No workouts available.</p>
      )}
    </div>
  );
}

export default Workouts;