document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function (e) {
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        this.classList.add('active');
    })
})


let currentOpenPopup = null;

function togglePopup(event, taskId) {
    event.stopPropagation();
    const popup = document.getElementById('popup-' + taskId);

    // Close other popups
    if (currentOpenPopup && currentOpenPopup !== popup) {
        currentOpenPopup.classList.remove('active');
    }

    // Toggle current popup
    popup.classList.toggle('active');
    currentOpenPopup = popup.classList.contains('active') ? popup : null;
}

// Close popup when clicking outside
document.addEventListener('click', function(event) {
    if (currentOpenPopup && !event.target.closest('.popup-menu') && !event.target.closest('.task-id')) {
        currentOpenPopup.classList.remove('active');
        currentOpenPopup = null;
    }
});


// Set today's date as default for start_date
document.getElementById('start_date').valueAsDate = new Date();

// Validate due date is not before start date
document.getElementById('due_date').addEventListener('change', function() {
    const startDate = document.getElementById('start_date').value;
    const dueDate = this.value;

    if (startDate && dueDate && new Date(dueDate) < new Date(startDate)) {
        alert('Due date cannot be before start date');
        this.value = '';
    }
});
