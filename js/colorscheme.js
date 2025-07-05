let schemes = {
  "red": {
    "link-color": "#ee0000",
    "button-text-color": "#ee0000"
  },
  "orange": {
    "link-color": "#ff6010",
    "button-text-color": "#ff6010"
  },
  "blue": {
    "link-color": "#2492d6",
    "button-text-color": "#2492d6"
  },
  "purple": {
    "link-color": "#530fff",
    "button-text-color": "#530fff"
  }
}

function changeColorScheme(name) {
  let scheme = schemes[name];

  if (scheme) {
    Object.entries(scheme).forEach((kv) => {
      document.documentElement.style.setProperty("--" + kv[0], kv[1]);
    })
  }
}
