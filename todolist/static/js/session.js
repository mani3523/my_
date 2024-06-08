// Check if the browser is Firefox
const isFirefox = typeof InstallTrigger !== 'undefined';

// Define the words to be animated
const words = "Session Expired";

// Initialize angle and animation duration
let ANGLE = 360;
const ANIMATION_DURATION = 4000;

// Function to handle the animation
const animation = () => {
    // Increment the angle
    ANGLE -= 1;

    // Iterate over each character
    document.querySelectorAll(".spiral *").forEach((el, i) => {
        // Calculate translateY and scale for animation
        const translateY = Math.sin(ANGLE * (Math.PI / 120)) * 100;
        const scale = Math.cos(ANGLE * (Math.PI / 120)) * 0.5 + 0.5;

        // Calculate delay based on character position
        const offset = parseInt(el.dataset.offset);
        const delay = i * (ANIMATION_DURATION / 16) - offset;

        // Apply animation transformation
        setTimeout(() => {
            el.style.transform = `translateY(${translateY}px) scale(${scale})`;
        }, delay);
    });

    // Request next animation frame
    requestAnimationFrame(animation);
};

// Function to create HTML elements for characters
const createCharacterElement = (char, offset) => {
    const div = document.createElement("div");
    div.innerText = char;
    div.classList.add("character");
    div.setAttribute("data-offset", offset);
    div.style.animationDelay = `-${offset}ms`;
    return div;
};

// Initialize animation for each character
words.split("").forEach((char, i) => {
    document.querySelector("#spiral").append(createCharacterElement(char, 0));
    document.querySelector("#spiral2").append(createCharacterElement(char, (isFirefox ? 1 : -1) * (ANIMATION_DURATION / 2)));
});

// Start animation if the browser is Firefox
if (isFirefox) {
    animation();
}

// Create login button
const loginButton = document.createElement("button");
loginButton.innerText = "Login again";
loginButton.style.position = "absolute";
loginButton.style.top = "10px";
loginButton.style.left = "10px";
loginButton.style.zIndex = "9999";
loginButton.style.padding = "10px 20px";
loginButton.style.fontSize = "16px";
loginButton.style.fontWeight = "bold";
loginButton.style.color = "#fff";
loginButton.style.backgroundColor = "#ea12ed";
loginButton.style.border = "none";
loginButton.style.borderRadius = "5px";
loginButton.style.cursor = "pointer";
loginButton.style.boxShadow = "0 2px 4px rgba(0, 0, 0, 0.1)";
loginButton.style.transition = "background-color 30s ease";

// Add hover effect
loginButton.addEventListener("mouseenter", () => {
    loginButton.style.backgroundColor = "#0056b3";
});

loginButton.addEventListener("mouseleave", () => {
    loginButton.style.backgroundColor = "#007bff";
});

// Add event listener to the login button
loginButton.addEventListener("click", () => {
    // Redirect to login page
    window.location.href = "/account/login";
});

// Append login button to the body
document.body.appendChild(loginButton);
