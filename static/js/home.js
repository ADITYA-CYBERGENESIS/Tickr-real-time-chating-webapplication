poster=document.querySelector(".poster");
posterImgHolder=document.querySelector(".poster_image_holder");
section3=document.querySelector(".section-3");
if (window.screen.width < 800){
    poster.classList.remove("flex-center");
    posterImgHolder.classList.add("flex-center");
}
if (window.screen.width < 600){
    section3.innerHTML=`<div class="container">
    <div class="section-3_heading">
        <h1>How It Works</h1>
        <p>Get started with Tickr in just 4 easy steps</p>

    </div>

    <div class="steps">
        <div class="step-1">Zip through registration in a flash – fill out your deets in just 60 seconds!
        </div>
        <div class="step-2">Hit the ground running – activate, log in, and let the adventure begin!</div>

    </div>
    
    <div class="steps">
        <div class="step-3">Tailor your space, your way – personalize your account to suit your style and
            needs!</div>
        <div class="step-4">Discover, connect, chat! Find friends with a quick username search and dive into
            conversations!</div>
    </div>
</div>`}