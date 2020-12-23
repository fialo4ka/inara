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
    }
   



function scrollHorizontally(e) {
    let hjhg = !isInViewport(document.getElementById("scrollAkril"));
    if(hjhg)
    {
        console.log(hjhg);
        return;
    } 
    e = window.event || e;
    var delta = Math.max(-1, Math.min(1, (e.wheelDelta || -e.detail)));
    var scrollSpeed = 60; // Janky jank <<<<<<<<<<<<<<
    document.documentElement.scrollLeft -= (delta * scrollSpeed);
    document.body.scrollLeft -= (delta * scrollSpeed);
    e.preventDefault();
  }

function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    console.log(rect.top+ "  " + window.innerHeight);

    return (
        rect.top >= 0 && 
        rect.top <= window.innerHeight
        
    );
}
