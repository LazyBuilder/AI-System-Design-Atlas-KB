/* Read-only presentation control: no requests, cookies, or browser storage. */
(() => {
  const buttons = Array.from(document.querySelectorAll('[data-provider]'));
  const panels = Array.from(document.querySelectorAll('.provider-panel'));
  if (buttons.length !== 3 || panels.length !== 3) return;
  const select = provider => {
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.provider === provider)));
    panels.forEach(panel => { panel.hidden = panel.id !== `panel-${provider}`; });
  };
  buttons.forEach(button => button.addEventListener('click', () => select(button.dataset.provider)));
  select('aws');
})();
