import './main.css'

// Cicero bust easter egg
const bust = document.querySelector('.cicero-bust');
if (bust) {
  bust.addEventListener('click', () => {
    bust.classList.add('animate-pulse');
    setTimeout(() => bust.classList.remove('animate-pulse'), 1000);
  });
}
