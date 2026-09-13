document.addEventListener('DOMContentLoaded', () => {
  const modal = document.querySelector('[data-wish-modal]');
  const openWishButton = document.querySelector('[data-wish-open]');
  const closeWishButtons = document.querySelectorAll('[data-wish-close]');
  const wishName = modal?.querySelector('#id_name');

  const openModal = () => {
    if (!modal) return;
    modal.hidden = false;
    document.body.classList.add('modal-is-open');
    wishName?.focus();
  };

  const closeModal = () => {
    if (!modal) return;
    modal.hidden = true;
    document.body.classList.remove('modal-is-open');
    openWishButton?.focus();
  };

  openWishButton?.addEventListener('click', openModal);
  closeWishButtons.forEach((button) => button.addEventListener('click', closeModal));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && modal && !modal.hidden) closeModal();
  });
  if (modal?.dataset.open === 'true') openModal();

  const music = document.querySelector('#wedding-music');
  const musicButton = document.querySelector('[data-music-toggle]');
  musicButton?.addEventListener('click', async () => {
    if (!music) return;
    if (music.paused) {
      try {
        await music.play();
        musicButton.classList.add('is-playing');
        musicButton.textContent = '❚❚';
        musicButton.setAttribute('aria-label', 'Музыканы өшіру');
        musicButton.setAttribute('aria-pressed', 'true');
      } catch (_) {
        musicButton.setAttribute('aria-label', 'Музыканы ойнату мүмкін болмады');
      }
    } else {
      music.pause();
      musicButton.classList.remove('is-playing');
      musicButton.textContent = '♫';
      musicButton.setAttribute('aria-label', 'Музыканы қосу');
      musicButton.setAttribute('aria-pressed', 'false');
    }
  });
});
