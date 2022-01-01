window.onload = () => {
    const display = document.createElement("h1");
    display.textContent = "This was added by the javascript file";
    const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];
    document.body.appendChild(display);
    setInterval(
        () => {
            display.style.color = colors[Math.round(Math.random() * colors.length)];
        }, 500
    );
};