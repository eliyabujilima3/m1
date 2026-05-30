const loadFragment = async (selector, url) => {
  const container = document.querySelector(selector);
  if (!container) return;
  try {
    const response = await fetch(url);
    if (!response.ok) return;
    container.innerHTML = await response.text();
  } catch (error) {
    console.warn(`Unable to load ${url}:`, error);
  }
};

const highlightNav = () => {
  const links = document.querySelectorAll('.nav-links a');
  const current = window.location.pathname.split('/').pop() || 'index.html';
  links.forEach((link) => {
    if (link.getAttribute('href') === current) {
      link.classList.add('active');
    }
  });
};

const toggleMenu = () => {
  document.querySelector('.menu-toggle')?.addEventListener('click', () => {
    document.querySelector('.nav-links')?.classList.toggle('open');
  });
};

const submitContactForm = () => {
  const form = document.querySelector('#contact-form');
  if (!form) return;

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const submitButton = form.querySelector('button[type="submit"]');
    const status = document.querySelector('#contact-status');
    const formData = {
      name: form.name.value.trim(),
      email: form.email.value.trim(),
      subject: form.subject.value.trim(),
      message: form.message.value.trim(),
    };

    if (!formData.name || !formData.email || !formData.subject || !formData.message) {
      status.textContent = 'Please fill in every field before sending your message.';
      status.className = 'status-error';
      return;
    }

    submitButton.disabled = true;
    submitButton.textContent = 'Sending...';

    try {
      const response = await fetch('http://127.0.0.1:5000/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      const payload = await response.json();
      if (response.ok && payload.success) {
        status.textContent = 'Message sent successfully. I will respond shortly.';
        status.className = 'status-success';
        form.reset();
      } else {
        status.textContent = payload.error || 'Unable to send message. Please try again later.';
        status.className = 'status-error';
      }
    } catch (error) {
      status.textContent = 'Unable to connect to the server. Please start the backend or try again later.';
      status.className = 'status-error';
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = 'Send Message';
    }
  });
};

window.addEventListener('DOMContentLoaded', async () => {
  await loadFragment('#header-placeholder', 'header.html');
  await loadFragment('#footer-placeholder', 'footer.html');
  highlightNav();
  toggleMenu();
  submitContactForm();
});
