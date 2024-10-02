document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById('search');
    const resultHolder = document.getElementById('result-holder');

    searchInput.addEventListener('input', function () {
        const query = searchInput.value;

        fetch('http://localhost:8000/posts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()  // Ensure you have CSRF token in Django if needed
            },
            body: JSON.stringify({
                query: query,
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.success && data.data.length > 0) {
                    let result = '';
                    data.data.forEach(post => {
                        result += ` <div class="m-auto w-100">
                                        <p>POST TEXT: ${post.text}</p> 
                                        <p>USER: ${post.user.username}</p>
                                        <p>TOPIC: ${post.topic}</p>
                                        <p>CREATED: ${post.created}</p>
                                        <p>UPDATED: ${post.updated}</p>
                                        <a class="btn btn-secondary w-100" href="/post/${post.id}/">Open Post</a> 
                                    </div>`;
                    });
                    resultHolder.innerHTML = result;
                } else {
                    resultHolder.innerHTML = '<p class="text-danger">Post Not Found</p>';
                }
            })
            .catch(error => {
                console.error('Error fetching posts:', error);
            });
    });

    function getCsrfToken() {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [name, value] = cookie.split('=');
            if (name.trim() === 'csrftoken') {
                return value;
            }
        }
        return '';
    }
});
