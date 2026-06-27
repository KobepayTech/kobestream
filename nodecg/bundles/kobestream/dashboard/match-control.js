function value(id) {
  return document.getElementById(id).value;
}

function numberValue(id) {
  return Number(document.getElementById(id).value || 0);
}

function updateMatch() {
  nodecg.sendMessage('updateMatch', {
    homeTeam: value('homeTeam'),
    awayTeam: value('awayTeam'),
    homeScore: numberValue('homeScore'),
    awayScore: numberValue('awayScore'),
    timer: value('timer'),
    period: value('period')
  });
}

function updatePlayer() {
  nodecg.sendMessage('updatePlayer', {
    name: value('playerName'),
    number: numberValue('playerNumber'),
    goals: numberValue('goals'),
    assists: numberValue('assists'),
    yellowCards: numberValue('yellowCards'),
    redCards: numberValue('redCards'),
    title: 'Player Stats'
  });
}

function updateLowerThird() {
  nodecg.sendMessage('updateLowerThird', {
    visible: true,
    title: value('lowerTitle'),
    subtitle: value('lowerSubtitle')
  });
}
