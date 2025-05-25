function swapColors() {
  const element = document.querySelector('.colorswap');

  if (element !== null) {
    const styles = window.getComputedStyle(element);

    const backgroundColor = styles.backgroundColor;
    const color = styles.color;

    element.style.backgroundColor = color;
    element.style.color = backgroundColor;
  }
}

setInterval(swapColors, 250);
