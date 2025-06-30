function toggleAllDetails() {
  let oneIsOpen = false;

  let allDetails = document.body.querySelectorAll("details");

  allDetails.forEach((e) => {
    if (e.hasAttribute("open")) {
      oneIsOpen = true;
      return;
    }
  }) 

  if (oneIsOpen) {
    allDetails.forEach((e) => {
      if (e.hasAttribute("open")) {
        e.removeAttribute("open")
      }
    })
  } else {
    allDetails.forEach((e) => {
      if (!e.hasAttribute("open")) {
        e.setAttribute("open", true)
      }
    })
  }
}
