let toggled = false;

function toggleAllDetails() {
  toggled = !toggled;

  document.body.querySelectorAll('details').forEach((e) => {
    if (e.hasAttribute("open") && !toggled) {
      e.removeAttribute("open")
    } else {
      e.setAttribute("open", true)
    }
  })
}
