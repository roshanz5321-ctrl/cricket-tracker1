let players = [];

function renderTable(data) {
  const tbody = document.getElementById("tableBody");
  tbody.innerHTML = "";

  data.forEach(player => {
    const row = document.createElement("tr");
    row.innerHTML = `
    <td>${player.name}</td>
    <td>${player.team}</td>
    <td>${player.hundreds}</td>
    <td>${player.fifties}</td>
    <td>${player.runs}</td>
    <td>${player.wickets}</td>
    <td><button onclick="deletePlayer('${player.name}')" style="background:red;color:white;border:none;padding:5px 10px;cursor:pointer;">🗑️ Delete</button></td>
`;
    tbody.appendChild(row);
  });
}

function loadPlayers() {
  fetch(`/api/players/${FORMAT}`)
    .then(response => response.json())
    .then(data => {
      players = data;
      renderTable(players);
    });
}

document.getElementById("searchBox").addEventListener("input", function() {
  const searchTerm = this.value.toLowerCase();
  const filtered = players.filter(player =>
    player.name.toLowerCase().includes(searchTerm)
  );
  renderTable(filtered);
});

document.getElementById("sortRunsBtn").addEventListener("click", function() {
  const sorted = [...players].sort((a, b) => b.runs - a.runs);
  renderTable(sorted);
});

document.getElementById("sortWicketsBtn").addEventListener("click", function() {
  const sorted = [...players].sort((a, b) => b.wickets - a.wickets);
  renderTable(sorted);
});

document.getElementById("addPlayerBtn").addEventListener("click", function() {
  const newPlayer = {
    name: document.getElementById("newName").value,
    team: document.getElementById("newTeam").value,
    format: FORMAT,
    hundreds: document.getElementById("newHundreds").value,
    fifties: document.getElementById("newFifties").value,
    runs: document.getElementById("newRuns").value,
    wickets: document.getElementById("newWickets").value
  };

  fetch("/api/players", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(newPlayer)
  })
    .then(response => response.json())
    .then(() => {
      loadPlayers();
      document.getElementById("newName").value = "";
      document.getElementById("newTeam").value = "";
      document.getElementById("newHundreds").value = "";
      document.getElementById("newFifties").value = "";
      document.getElementById("newRuns").value = "";
      document.getElementById("newWickets").value = "";
    });
});

loadPlayers();
function deletePlayer(playerName) {
    if (!confirm(`Delete ${playerName}?`)) return;
    
    fetch(`/api/players/${FORMAT}/${playerName}`, {
        method: "DELETE"
    })
    .then(response => {
        console.log("Status:", response.status);
        if (response.ok) {
            alert("Player deleted!");
            loadPlayers();
        } else {
            response.text().then(text => console.log("Error:", text));
            alert("Failed to delete player");
        }
    })              // ← NO semicolon here!
    .catch(error => {
        console.error("Network error:", error);
        alert("Network error occurred");
    });
}                   // ← Function closing brace