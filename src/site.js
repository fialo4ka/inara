if (window.addEventListener) {
    let passiveSupported = false;
    try {
        const options = {
            get passive() { 
                passiveSupported = true;
                return false;
            }
        };
        // IE9, Chrome, Safari, Opera
        window.addEventListener("mousewheel", scrollHorizontally, options);
        // Firefox
        window.addEventListener("DOMMouseScroll", scrollHorizontally, options);
    } 
    catch(err) {
        passiveSupported = false;
    }
  } else {
    // IE 6/7/8
    window.attachEvent("onmousewheel", scrollHorizontally);
  }





function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

function scrollHorizontally(e) {
    e = window.event || e;
    var delta = Math.max(-1, Math.min(1, (e.wheelDelta || -e.detail)));
    var scrollSpeed = 60; // Janky jank <<<<<<<<<<<<<<
    document.documentElement.scrollLeft -= (delta * scrollSpeed);
    document.body.scrollLeft -= (delta * scrollSpeed);
    e.preventDefault();
  }

