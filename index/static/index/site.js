// Toggle between showing and hiding the sidebar when clicking the menu icon
var mySidebar = document.getElementById("mySidebar");

function w3_open() {
  if (mySidebar.style.display === 'block') {
    mySidebar.style.display = 'none';
  } else {
    mySidebar.style.display = 'block';
  }
}

// Close the sidebar with the close button
function w3_close() {
    mySidebar.style.display = "none";
}

var modal = document.getElementById("artModal");

// When the user clicks the button, open the modal 
function OpenArtModal(photo, price, size, year, text) {
  modal.style.display = "block";
  document.getElementById("photo").src = "/artWorks/" + photo;
  let info = document.getElementById("info"),
  priceEl = document.getElementById("price"),
  textEl = document.getElementById("text");
  info.innerHTML = "";
  priceEl.innerHTML = "";
  textEl.innerHTML = "";
  if(text != "None"){
    textEl.innerHTML = text;
  }  
  if(size != "None"){
    info.innerHTML +="Size: " + size + ". ";
  }
  if(year != "None"){
    info.innerHTML += "Creation year " + year;
  }
  if(price != "None"){
    priceEl.innerHTML = "Price: " + price + " Eur";
    document.getElementById("order").classList.remove("w3-hide");
  }
  else{
    document.getElementById("order").classList.add("w3-hide");
  }
  var orderMailDetails = document.getElementById("order");
  orderMailDetails.href = `mailto:lamachenno108@gmail.com?subject=Ortder artwork&body=Hello%20I'm%20interested%20in%20ordering%20artwork%20'`+text+"'";
}

// When the user clicks on <span> (x), close the modal
function CloseArtModal() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}