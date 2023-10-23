function hideshow(elem) {
    var x = document.getElementById(elem);
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

const element = document.querySelector('.color-swap');

function swapColors() {
  const styles = window.getComputedStyle(element);

  const backgroundColor = styles.backgroundColor;
  const color = styles.color;

  element.style.backgroundColor = color;
  element.style.color = backgroundColor;
}

setInterval(swapColors, 250);