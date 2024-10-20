// Function to toggle the menu and blur effect
function toggleMenu() {
    const menu = document.getElementById('category-menu');
    const overlay = document.getElementById('overlay');
    const bodyContent = document.querySelectorAll('.news-block'); // Select news-block and footer, exclude header
    const menuIcon = document.getElementById('menuIcon');
    const closeIcon = document.getElementById('closeIcon');

    if (menu.classList.contains('show')) {
        // Close the menu
        menu.classList.remove('show');
        overlay.style.display = "none";
        bodyContent.forEach((element) => {
            element.classList.remove('blur'); // Remove blur effect
        });
        menuIcon.style.display = "block"; // Show menu icon
        closeIcon.style.display = "none"; // Hide close icon
    } else {
        // Open the menu
        menu.classList.add('show');
        overlay.style.display = "block";
        bodyContent.forEach((element) => {
            element.classList.add('blur'); // Apply blur effect to news-block and footer
        });
        menuIcon.style.display = "none"; // Hide menu icon
        closeIcon.style.display = "block"; // Show close icon
    }
}

// Close the menu when clicking outside (on the overlay)
document.getElementById('overlay').onclick = function() {
    toggleMenu();
};

// Highlight the active menu item based on the current URL
const currentPage = window.location.pathname.split("/").pop();
const menuLinks = document.querySelectorAll("#category-menu li a");

menuLinks.forEach(link => {
    if (link.getAttribute("href") === currentPage) {
        link.classList.add("active");
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const menuIcon = document.getElementById("menuIcon");
    const closeIcon = document.getElementById("closeIcon");

    menuIcon.addEventListener("click", toggleMenu);
    closeIcon.addEventListener("click", toggleMenu);
});


document.addEventListener('DOMContentLoaded', function() {
        const menuToggle = document.getElementById('menu-toggle');
        const closeIcon = document.getElementById('closeIcon');
        const menu = document.getElementById('category-menu');
        const currentPageHeader = document.getElementById('current_page');

        // Toggle menu visibility
        menuToggle.addEventListener('click', function() {
            menu.classList.toggle('show'); // Show/hide menu
            closeIcon.style.display = menu.classList.contains('show') ? 'block' : 'none'; // Show close icon
        });

        // Close the menu when the close icon is clicked
        closeIcon.addEventListener('click', function() {
            menu.classList.remove('show');
            closeIcon.style.display = 'none';
        });

        // Update the current page header and highlight active link
        const links = menu.querySelectorAll('a');
        links.forEach(link => {
            // Highlight active link based on current page
            if (link.href === window.location.href) {
                link.classList.add('active'); // Add active class to the current page link
            }
            link.addEventListener('click', function(event) {
                // Update the current page header when a link is clicked
                const title = link.textContent; // Use link text as title
                currentPageHeader.innerText = title; // Update the header
            });
        });
    });