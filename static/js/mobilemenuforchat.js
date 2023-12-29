
mobileNav = document.querySelector(".chat_nav");
hamburgerMenu = document.querySelector(".mobilemenubtn");

var state = 'closed';
hamburgerMenu.addEventListener("click", () => {
    screenWidth = window.screen.width;
    if (screenWidth < 500) {
        if (state == 'closed') {
            mobileNav.classList.toggle("nav-disnone");
        }
        else {
                mobileNav.classList.add("nav-disnone");
        }
    }
    else {
        if (state == 'closed') {
            mobileNav.classList.toggle("nav-disnone");
        }
        else {
                mobileNav.classList.add("nav-disnone");
        }
    }
})

let a = document.addEventListener('click', function (event) {
    if (event.target !== mobileNav && !mobileNav.contains(event.target)&&event.target !== hamburgerMenu && !hamburgerMenu.contains(event.target)&&!mobileNav.classList.contains('dis-none')) {
            mobileNav.classList.add("nav-disnone");
            state = 'closed';
  }});
let b = document.addEventListener('scroll', function (event) {
    if (!mobileNav.classList.contains('nav-disnone')){
    }
    mobileNav.classList.add("nav-disnone");
    state = 'closed';
});

if (state=='open'){
    a()
    b()
}
