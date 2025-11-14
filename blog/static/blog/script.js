const box = document.getElementById('box');

// Mouse enters the box
box.addEventListener('mouseenter', () => {
  box.classList.add('hover');
  box.textContent = 'Mouse Entered!';
});

// Mouse leaves the box
box.addEventListener('mouseleave', () => {
  box.classList.remove('hover');
  box.textContent = 'Mouse Left!';
});

// Mouse clicks the box
box.addEventListener('mousedown', () => {
  box.classList.add('active');
  box.textContent = 'Mouse Down!';
});

box.addEventListener('mouseup', () => {
  box.classList.remove('active');
  box.textContent = 'Mouse Up!';
});

// Mouse moves inside the box
box.addEventListener('mousemove', (event) => {
  const x = event.offsetX;
  const y = event.offsetY;
  box.textContent = `Mouse Move: X=${x}, Y=${y}`;
});
