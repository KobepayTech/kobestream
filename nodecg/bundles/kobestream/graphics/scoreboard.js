var matchRep = nodecg.Replicant('match');

matchRep.on('change', function (value) {
  if (!value) return;
  document.getElementById('homeTeam').textContent = value.homeTeam;
  document.getElementById('awayTeam').textContent = value.awayTeam;
  document.getElementById('homeScore').textContent = value.homeScore;
  document.getElementById('awayScore').textContent = value.awayScore;
  document.getElementById('timer').textContent = value.timer;
  document.getElementById('period').textContent = value.period;
});
