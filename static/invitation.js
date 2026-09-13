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
  const setMusicButtonState = (isPlaying) => {
    if (!musicButton) return;
    musicButton.classList.toggle('is-playing', isPlaying);
    musicButton.textContent = isPlaying ? '❚❚' : '♫';
    musicButton.setAttribute('aria-label', isPlaying ? 'Музыканы өшіру' : 'Музыканы қосу');
    musicButton.setAttribute('aria-pressed', String(isPlaying));
  };
  const startMusic = async () => {
    if (!music) return;
    try {
      await music.play();
      setMusicButtonState(true);
    } catch (_) {
      setMusicButtonState(false);
    }
  };

  startMusic();
  // Browsers block unmuted autoplay. Start music on the visitor's first
  // natural interaction anywhere on the page if the initial attempt was blocked.
  const startOnFirstInteraction = () => {
    if (music?.paused) startMusic();
  };
  ['pointerdown', 'touchstart', 'keydown', 'scroll'].forEach((eventName) => {
    window.addEventListener(eventName, startOnFirstInteraction, { once: true, passive: eventName !== 'keydown' });
  });
  musicButton?.addEventListener('click', async () => {
    if (!music) return;
    if (music.paused) {
      await startMusic();
    } else {
      music.pause();
      setMusicButtonState(false);
    }
  });
});
