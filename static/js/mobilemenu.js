loginBtn = document.querySelector("#login_btn-homepage");
getStartedBtn = document.querySelector("#get_started_btn-homepage");
mobileNav = document.querySelector(".mobile_nav");
hamburgerMenu = document.querySelector(".hamburger_menu");
hamburgerBar1 = document.querySelector(".hamburger_bar-1");
hamburgerBar2 = document.querySelector(".hamburger_bar-2");
hamburgerBar3 = document.querySelector(".hamburger_bar-3");

var state = 'closed';
hamburgerMenu.addEventListener("click", () => {
    screenWidth = window.screen.width;
    loginBtn.classList.toggle("dis-none");
    getStartedBtn.classList.toggle("dis-none");
    if (screenWidth < 451) {
        if (state == 'closed') {
            mobileNav.classList.toggle("dis-none");
            mobileNav.classList.toggle("slidein-top");
        }
        else {
            mobileNav.classList.toggle("slideout-top");
            mobileNav.classList.toggle("slidein-top");
            setTimeout(() => {
                mobileNav.classList.add("dis-none");
                mobileNav.classList.toggle("slideout-top");

            }, 400)
        }
    }
    else {
        if (state == 'closed') {
            mobileNav.classList.toggle("dis-none");
            mobileNav.classList.toggle("slidein-right");
        }
        else {
            mobileNav.classList.toggle("slideout-right");
            mobileNav.classList.toggle("slidein-right");
            setTimeout(() => {
                mobileNav.classList.toggle("slideout-right");
                mobileNav.classList.add("dis-none");
            }, 400)

        }
    }
    // 
    // hamburgerBar3.style.bottom='10px';
    // hamburgerBar3.style.rotate='-45deg';
    
    
    if (state == 'closed') {
        hamburgerBar1.style.animation='hamburgerbar1-open 0.5s';
        hamburgerBar3.style.animation='hamburgerbar3-open 0.5s';
        hamburgerBar2.style.visibility='hidden';
        setTimeout(() => {
            hamburgerBar1.style.top='10px';
            hamburgerBar1.style.rotate='45deg';
            hamburgerBar3.style.bottom='10px';
            hamburgerBar3.style.rotate='-45deg';
        },450)
        state = 'open';
    }
    else {
        hamburgerBar1.style.animation='hamburgerbar1-close 0.5s';
        hamburgerBar3.style.animation='hamburgerbar3-close 0.5s';
     
        setTimeout(() => {
            hamburgerBar2.style.visibility='visible';
            hamburgerBar1.style.top='0px';
            hamburgerBar1.style.rotate='0deg';
            hamburgerBar3.style.bottom='0px';
            hamburgerBar3.style.rotate='0deg';
        },450)
        state = 'closed';
    }
    console.log(state)
})

let a = document.addEventListener('click', function (event) {
    if (event.target !== mobileNav && !mobileNav.contains(event.target)&&event.target !== hamburgerMenu && !hamburgerMenu.contains(event.target)&&!mobileNav.classList.contains('dis-none')) {
        loginBtn.classList.toggle("dis-none");
        getStartedBtn.classList.toggle("dis-none");
            mobileNav.classList.add("dis-none");
            mobileNav.classList.remove("slidein-top");
            mobileNav.classList.remove("slidein-right");
            state = 'closed';
            console.log(state)
            hamburgerBar1.style.animation='hamburgerbar1-close 0.5s';
            hamburgerBar3.style.animation='hamburgerbar3-close 0.5s';
            
            setTimeout(() => {
                hamburgerBar2.style.visibility='visible';
                hamburgerBar1.style.top='0px';
                hamburgerBar1.style.rotate='0deg';
                hamburgerBar3.style.bottom='0px';
                hamburgerBar3.style.rotate='0deg';
            },450)
  }});
let b = document.addEventListener('scroll', function (event) {
    if (!mobileNav.classList.contains('dis-none')){
        loginBtn.classList.toggle("dis-none");
    getStartedBtn.classList.toggle("dis-none");
    }
    mobileNav.classList.add("dis-none");
    mobileNav.classList.remove("slidein-top");
    mobileNav.classList.remove("slidein-right");
    state = 'closed';
    console.log(state);
    hamburgerBar1.style.animation = 'hamburgerbar1-close 0.5s';
    hamburgerBar3.style.animation = 'hamburgerbar3-close 0.5s';

    setTimeout(() => {
        hamburgerBar2.style.visibility='visible';
        hamburgerBar1.style.top='0px';
        hamburgerBar1.style.rotate='0deg';
        hamburgerBar3.style.bottom='0px';
        hamburgerBar3.style.rotate='0deg';
    }, 450);
});

if (state=='open'){
    a()
    b()
}
