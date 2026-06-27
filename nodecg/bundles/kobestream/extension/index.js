module.exports = function (nodecg) {
  const match = nodecg.Replicant('match', {
    defaultValue: {
      homeTeam: 'HOME',
      awayTeam: 'AWAY',
      homeScore: 0,
      awayScore: 0,
      timer: '00:00',
      period: '1st Half'
    }
  });

  const player = nodecg.Replicant('player', {
    defaultValue: {
      name: 'Player Name',
      number: 6,
      team: 'HOME',
      goals: 0,
      assists: 0,
      yellowCards: 0,
      redCards: 0,
      title: 'Player Stats'
    }
  });

  const lowerThird = nodecg.Replicant('lowerThird', {
    defaultValue: {
      visible: true,
      title: 'Kobestream Live',
      subtitle: 'Sports broadcast graphics'
    }
  });

  nodecg.listenFor('updateMatch', (value) => {
    match.value = { ...match.value, ...value };
  });

  nodecg.listenFor('updatePlayer', (value) => {
    player.value = { ...player.value, ...value };
  });

  nodecg.listenFor('updateLowerThird', (value) => {
    lowerThird.value = { ...lowerThird.value, ...value };
  });
};
