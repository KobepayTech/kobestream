var lowerRep = nodecg.Replicant('lowerThird');

lowerRep.on('change', function (value) {
  if (!value) return;
  document.getElementById('lower').classList.toggle('hidden', value.visible === false);
  document.getElementById('title').textContent = value.title;
  document.getElementById('subtitle').textContent = value.subtitle;
});
