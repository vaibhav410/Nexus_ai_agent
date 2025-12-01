let currentMode = 'therapy';
const input = document.getElementById('input');

// Auto-resize input
input.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 120) + 'px';
});

// Enter to send
input.addEventListener('keypress', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

function setMode(el, mode) {
    document.querySelectorAll('.mode-card').forEach(c => c.classList.remove('active'));
    el.classList.add('active');
    currentMode = mode;
}

function sendQuick(text) {
    input.value = text;
    sendMessage();
}

async function sendMessage() {
    const text = input.value.trim();
    if (!text) return;

    // UI Updates
    const welcomeScreen = document.getElementById('welcome');
    if (welcomeScreen) {
        welcomeScreen.style.display = 'none';
    }

    input.value = '';
    input.style.height = 'auto';

    addMessage(text, 'user');
    showTyping();

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text, mode: currentMode })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        hideTyping();
        addMessage(data.reply, 'bot');

    } catch (error) {
        console.error('Error:', error);
        hideTyping();
        addMessage('**Connection Error**: Please check your internet or API key.', 'bot');
    }
}

function addMessage(text, type) {
    const container = document.getElementById('messages');
    const div = document.createElement('div');
    div.className = `message ${type}`;

    const avatar = type === 'user' ? '<i class="fas fa-user"></i>' : '<i class="fas fa-brain"></i>';
    const avatarClass = type === 'user' ? 'user-avatar' : 'bot-avatar';

    // Parse Markdown for bot messages
    const content = type === 'bot' ? marked.parse(text) : text;

    div.innerHTML = `
        <div class="avatar ${avatarClass}">${avatar}</div>
        <div class="message-bubble">${content}</div>
    `;

    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
}

function showTyping() {
    const container = document.getElementById('messages');
    const div = document.createElement('div');
    div.id = 'typing';
    div.className = 'typing-indicator';
    div.innerHTML = '<div class="dot"></div><div class="dot"></div><div class="dot"></div>';
    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
}

function hideTyping() {
    const el = document.getElementById('typing');
    if (el) el.remove();
}

function clearChat() {
    document.getElementById('messages').innerHTML = `
        <div class="welcome-screen" id="welcome">
            <h1 class="welcome-title">Hello, I am Nexus AI.</h1>
            <p class="welcome-subtitle">How can I support your mind today?</p>
            <div class="quick-actions">
                <div class="action-card glass-panel" onclick="sendQuick('I am feeling anxious and need to calm down.')">
                    <i class="fas fa-wind" style="color: var(--accent); font-size: 1.5rem; margin-bottom: 10px;"></i>
                    <h3>Anxiety Relief</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem;">Simple breathing exercises</p>
                </div>
                <div class="action-card glass-panel" onclick="sendQuick('I want to reflect on my day.')">
                    <i class="fas fa-book-open" style="color: var(--secondary); font-size: 1.5rem; margin-bottom: 10px;"></i>
                    <h3>Daily Reflection</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem;">Guided journaling session</p>
                </div>
            </div>
        </div>
    `;
}
