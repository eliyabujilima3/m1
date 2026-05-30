const adminLoginForm = document.querySelector('#admin-login-form');
const adminStatus = document.querySelector('#admin-status');

if (adminLoginForm) {
  adminLoginForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    adminStatus.textContent = '';
    const email = adminLoginForm.email.value.trim();
    const password = adminLoginForm.password.value.trim();

    if (!email || !password) {
      adminStatus.textContent = 'Please enter both email and password.';
      adminStatus.className = 'status-error';
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:5000/api/admin/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });
      const result = await response.json();
      if (response.ok && result.success) {
        window.location.href = 'admin.html';
      } else {
        adminStatus.textContent = result.error || 'Login failed. Check your credentials.';
        adminStatus.className = 'status-error';
      }
    } catch (error) {
      adminStatus.textContent = 'Server unreachable. Start the backend and try again.';
      adminStatus.className = 'status-error';
    }
  });
}
