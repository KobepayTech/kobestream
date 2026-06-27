var playerRep = nodecg.Replicant('player');

playerRep.on('change', function (value) {
  if (!value) return;
  document.getElementById('title').textContent = value.title || 'Player Stats';
  document.getElementById('number').textContent = value.number;
  document.getElementById('name').textContent = value.name;
  document.getElementById('goals').textContent = value.goals;
  document.getElementById('assists').textContent = value.assists;
  document.getElementById('yellowCards').textContent = value.yellowCards;
  document.getElementById('redCards').textContent = value.redCards;
});
