import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch('https://organic-giggle-5v65wpxw67x2p7rj-8000.app.github.dev/api/leaderboard/')
      .then(response => response.json())
      .then(data => setLeaderboard(data))
      .catch(error => console.error('Error fetching leaderboard:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-primary">Leaderboard</h1>
      {leaderboard.length > 0 ? (
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Team</th>
              <th>Points</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map(entry => (
              <tr key={entry._id}>
                <td>{entry.team?.name || 'Unknown Team'}</td>
                <td>{entry.points}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p className="text-danger">No leaderboard data available.</p>
      )}
    </div>
  );
}

export default Leaderboard;