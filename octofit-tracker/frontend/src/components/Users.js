import React, { useEffect, useState } from 'react';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('https://organic-giggle-5v65wpxw67x2p7rj-8000.app.github.dev/api/users/')
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-primary">Users</h1>
      {users.length > 0 ? (
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
            </tr>
          </thead>
          <tbody>
            {users.map(user => (
              <tr key={user._id}>
                <td>{user.name || 'Unknown User'}</td>
                <td>{user.email || 'No Email'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p className="text-danger">No users available.</p>
      )}
    </div>
  );
}

export default Users;