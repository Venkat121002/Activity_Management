document.querySelectorAll('nav-link').forEach(link => {
    link.addEventListener('click', function (e) {
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        this.classList.add('active');
    })
})


let currentOpenPopup = null;

function togglePopup(event, taskId) {
    event.stopPropagation();
    
    const popup = document.getElementById('popup-' + taskId);
    
    // Close currently open popup if it's different
    if (currentOpenPopup && currentOpenPopup !== popup) {
        currentOpenPopup.classList.remove('active');
    }
    
    // Toggle the clicked popup
    popup.classList.toggle('active');
    
    // Position the popup near the cursor
    const rect = event.currentTarget.getBoundingClientRect();
    popup.style.left = (event.clientX - rect.left) + 'px';
    popup.style.top = (event.clientY - rect.top + 10) + 'px';
    
    // Update current open popup
    currentOpenPopup = popup.classList.contains('active') ? popup : null;
}

// Close popup when clicking outside
document.addEventListener('click', function(event) {
    if (currentOpenPopup && !event.target.closest('.popup-menu')) {
        currentOpenPopup.classList.remove('active');
        currentOpenPopup = null;
    }
});

// Prevent popup close when clicking inside it
document.querySelectorAll('.popup-menu').forEach(popup => {
    popup.addEventListener('click', function(event) {
        event.stopPropagation();
    });
});