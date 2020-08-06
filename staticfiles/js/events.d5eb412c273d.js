const social = document.querySelector('.social').children;
const linkedin = document.querySelector('.linkedin');
const twitter = document.querySelector('.twitter');
const contact = document.querySelector('.contact');
const about = document.querySelector(".about");
const contactBtn = document.querySelector(".contact-btn")
const subscribe = document.querySelector(".subscribe")
const active = document.querySelectorAll('.nav-link')



for (let i = 0; i < social.length; i++) {
    social[i].addEventListener("mouseover", function(){
        social[i].classList.add("fa-2x");
    })
    social[i].addEventListener("mouseout", function(){
        social[i].classList.remove("fa-2x");
    })
}

linkedin.addEventListener("mouseover", () => linkedin.classList.add("linkedin-color"));
linkedin.addEventListener("mouseout", () => linkedin.classList.remove("linkedin-color"));

twitter.addEventListener("mouseover", () => twitter.classList.add("twitter-color"));
twitter.addEventListener("mouseout", () => twitter.classList.remove("twitter-color"));

contact.addEventListener("mouseover", () => contact.classList.add("contact-color"));
contact.addEventListener("mouseout", () => contact.classList.remove("contact-color"));

about.addEventListener("mouseover", () => about.classList.add("about-img"));
about.addEventListener("mouseout", () => about.classList.remove("about-img"));



subscribe.addEventListener("mouseover", () => subscribe.classList.add("btn-lg"));
subscribe.addEventListener("mouseout", () => subscribe.classList.remove("btn-lg"));

function changeNavBtnIcon() {
    let navIcon = document.querySelector('#nav-icon');
    if (navIcon.className === 'fas fa-bars') {
        navIcon.className = 'fas fa-times'
    }else {
        navIcon.className = 'fas fa-bars'
    }
}