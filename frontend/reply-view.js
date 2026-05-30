const replyForm = document.querySelector('#reply-form');
const replyStatus = document.querySelector('#reply-status');
const messageContainer = document.querySelector('#message-detail');

const getQueryParameter = (name) => {
  return new URLSearchParams(window.location.search).get(name);
};

const loadMessageDetail = async () => {
  const messageId = getQueryParameter('id');
  if (!messageId || !messageContainer) return;

  try {
    const response = await fetch(`http://127.0.0.1:5000/api/admin/message/${messageId}`);
    const payload = await response.json();
    if (response.ok && payload.success) {
      const message = payload.message;
      messageContainer.innerHTML = `
        <div class="message-card">
          <h3>${message.subject}</h3>
          <p><strong>Name:</strong> ${message.name}</p>
          <p><strong>Email:</strong> ${message.email}</p>
          <p>${message.message}</p>
          <p class="meta">Received: ${new Date(message.created_at).toLocaleString()}</p>
        </div>
      `;
    } else {
      messageContainer.innerHTML = '<p>Message details could not be loaded.</p>';
    }
  } catch (error) {
    messageContainer.innerHTML = '<p>Unable to load message detail from the server.</p>';
  }
};

if (replyForm) {
  replyForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    replyStatus.textContent = '';
    const contactId = getQueryParameter('id');
    const replyText = replyForm.reply.value.trim();

    if (!replyText) {
      replyStatus.textContent = 'Please enter a reply before saving.';
      replyStatus.className = 'status-error';
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:5000/api/reply', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ contact_id: Number(contactId), reply: replyText }),
      });
      const payload = await response.json();
      if (response.ok && payload.success) {
        replyStatus.textContent = 'Reply saved successfully.';
        replyStatus.className = 'status-success';
        replyForm.reset();
      } else {
        replyStatus.textContent = payload.error || 'Unable to save reply.';
        replyStatus.className = 'status-error';
      }
    } catch (error) {
      replyStatus.textContent = 'Cannot reach backend server. Please try again later.';
      replyStatus.className = 'status-error';
    }
  });
}

window.addEventListener('DOMContentLoaded', loadMessageDetail);
