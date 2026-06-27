async function loadCameraStats() {
  try {
    var res = await fetch('../shared/ai_stats.json?ts=' + Date.now());
    if (!res.ok) throw new Error('No stats yet');
    var data = await res.json();
    document.getElementById('players').textContent = data.players_detected || 0;
    document.getElementById('ball').textContent = data.ball_detected || 0;
    document.getElementById('frame').textContent = data.frame || 0;
    document.getElementById('updated').textContent = data.updated_at || 'running';
  } catch (err) {
    document.getElementById('updated').textContent = 'Waiting...';
  }
}

setInterval(loadCameraStats, 500);
loadCameraStats();
