// Copyritht © 2022 Marcin Różewski MDSANIMA

// swap logo
function swapLogo(color) {
  var svgPath = "/_static/logo/filled/svg/";
  let logo = document.images[0];
  logo.src = svgPath + "logo_mdsanima_default_" + color + ".svg";
}

// swap favicon
function swapFavicon(color) {
  var pngPath = "/_static/logo/squere/png/";
  let favicon = document.querySelector("link[rel~='icon']");
  favicon.href = pngPath + "logo_mdsanima_default_" + color + "_1x.png";
}

// object method color options
const logo = {
  colorSky: (swapColor = () => {
    color = "02-sky";
    swapLogo(color);
  }),
  colorTeal: (swapColor = () => {
    color = "17-teal";
    swapLogo(color);
  }),
  colorLime: (swapColor = () => {
    color = "14-lime";
    swapLogo(color);
  }),
  colorOrange: (swapColor = () => {
    color = "11-orange";
    swapLogo(color);
  }),
  colorRed: (swapColor = () => {
    color = "10-red";
    swapLogo(color);
  }),
};

// const test = document.getElementById("bdg-info-line");
// const test = document.querySelector("svg[class~='sd-octicon-desktop-download']");
// const test = document.querySelector(".sd-octicon-file-code");
// const test = document.querySelector(".sidebar-tree .current-page>.reference");
// const test = document.querySelector(".sidebar-tree .current>.current-page");
// const test = document.querySelector(".sidebar-tree .toctree-l1> .reference");
// test.onclick = logo.colorOrange;
