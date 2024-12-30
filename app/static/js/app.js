function getCSRFToken() {
    let cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        let [key, value] = cookie.trim().split('=');
        if (key === 'csrftoken') {
            return value;
        }
    }
    return null;
}

document.getElementById('chat-form').addEventListener('submit', function (e) {
    e.preventDefault();

    let userInput = document.getElementById('user-input').value;
    let chatLog = document.getElementById('chat-log');

    fetch('/generate/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken() // Include CSRF token
        },
        body: JSON.stringify({ message: userInput }) // Ensure the body is valid JSON
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            chatLog.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
            chatLog.innerHTML += `<p><strong>AI:</strong> ${data.response}</p>`;
            document.getElementById('user-input').value = '';
        })
        .catch(error => {
            console.error('Error:', error);
            chatLog.innerHTML += `<p><strong>Error:</strong> Unable to process the request.</p>`;
        });
});
