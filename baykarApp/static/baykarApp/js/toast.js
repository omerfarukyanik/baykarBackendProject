document.addEventListener("DOMContentLoaded", function () {
    const messagesElement = document.getElementById('toast-messages');
    if (messagesElement) {
        try {

            const messages = JSON.parse(messagesElement.textContent);
            const container = document.getElementById("toast-container");
            messages.forEach(message => {
                const toast = document.createElement("div");
                toast.className = `toast toast-${message.tags}`;
                toast.innerHTML = `
                <span>${message.message}</span>
                <span class="toast-close" onclick="this.parentElement.remove();">&times;</span>
            `;
                container.appendChild(toast);
                setTimeout(() => toast.remove(), 5000);
            });
        } catch (e) {

        }
    }
});