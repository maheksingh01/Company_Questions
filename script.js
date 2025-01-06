// JavaScript to dynamically set the image in the placeholder
const placeholderImage = document.getElementById("placeholderImage");

// Function to set a new image dynamically
function setImage(src) {
  placeholderImage.src = src;
}

// Example: Dynamically setting an image
setImage("./bg.avif");
