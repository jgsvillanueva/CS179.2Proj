// Get the nav toggle
var navButton = document.querySelector('nav button');

navButton.addEventListener('click', function() {
  // Set the ARIA value
  let expanded = this.getAttribute('aria-expanded') === 'true' || false;
  this.setAttribute('aria-expanded', !expanded);

  // DOM Traversal
  let menu = this.nextElementSibling;
  // Toggle the class
  menu.classList.toggle('open');
});
