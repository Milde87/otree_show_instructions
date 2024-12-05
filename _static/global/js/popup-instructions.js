// Event listener for clicks on the overlay area
document.querySelector(".overlay").addEventListener("click", function(event) {
    if (event.target === this) {
        window.location.href = "#";
    }
});