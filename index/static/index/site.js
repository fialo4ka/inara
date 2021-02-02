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
  if(text != "None"){
    document.getElementById("text").innerHTML = text;
  }
  var info = document.getElementById("info");
  info.innerHTML = "";
  if(size != "None"){
    info.innerHTML +="Size: " + size + ". ";
  }
  if(year != "None"){
    info.innerHTML += "Creation year " + year;
  }
  if(price != "None"){
    document.getElementById("price").innerHTML = "Price: " + price + "Eu";
    document.getElementById("order").classList.remove("w3-hide");
  }
  else{
    document.getElementById("order").classList.add("w3-hide");
  }
  var orderMailDetails = document.getElementById("order");
  orderMailDetails.href = orderMailDetails.href.replace("*artwort*",text);
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