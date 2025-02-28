document.addEventListener('DOMContentLoaded', function() {
    // File upload handling
    const fileInput = document.getElementById('sqlFile');
    const fileInfo = document.querySelector('.file-info');
    const fileName = document.querySelector('.file-name');
    const removeFile = document.querySelector('.remove-file');

    fileInput.addEventListener('change', function(e) {
        if (this.files.length > 0) {
            fileName.textContent = this.files[0].name;
            fileInfo.style.display = 'flex';
        }
    });

    removeFile.addEventListener('click', function() {
        fileInput.value = '';
        fileInfo.style.display = 'none';
        fileName.textContent = '';
    });

    // Chat functionality
    const messagesContainer = document.getElementById('messagesContainer');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');

    function addMessage(type, content) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.textContent = content;
        
        messageDiv.appendChild(contentDiv);
        messagesContainer.appendChild(messageDiv);
        
        // Scroll to bottom
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function handleUserInput() {
        const message = userInput.value.trim();
        if (message) {
            // Add user message
            addMessage('user', message);
            
            // Clear input
            userInput.value = '';
            
            // Simulate assistant response (replace with actual API call later)
            setTimeout(() => {
                addMessage('assistant', 'I understand you want to create a SQL query. Let me help you with that...');
            }, 1000);
        }
    }

    // Send button click
    sendButton.addEventListener('click', handleUserInput);

    // Enter key handling
    userInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleUserInput();
        }
    });
}); 