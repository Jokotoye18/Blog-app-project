const social = document.querySelector('.social').children;
const facebook = document.querySelector('.facebook');
const instagram = document.querySelector('.instagram');
const linkedin = document.querySelector('.linkedin');
const twitter = document.querySelector('.twitter');
const contact = document.querySelector('.contact');
const about = document.querySelector(".about");
const contact_btn = document.querySelector(".contact-btn")
const subscribe = document.querySelector(".subscribe");
const active = document.querySelectorAll('.nav-link');
const contactMessage = document.querySelector('#id_message');

console.log(contactMessage)

console.log(active.length)

for (let i = 0; i < social.length; i++) {
    social[i].addEventListener("mouseover", function(){
        social[i].classList.add("fa-3x");
    })
    social[i].addEventListener("mouseout", function(){
        social[i].classList.remove("fa-3x");
    })
}

facebook.addEventListener("mouseover", () => facebook.classList.add("facebook-color"));
facebook.addEventListener("mouseout", () => facebook.classList.remove("facebook-color"));

instagram.addEventListener("mouseover", () => instagram.classList.add("instagram-color"));
instagram.addEventListener("mouseout", () => instagram.classList.remove("instagram-color"));

linkedin.addEventListener("mouseover", () => linkedin.classList.add("linkedin-color"));
linkedin.addEventListener("mouseout", () => linkedin.classList.remove("linkedin-color"));

twitter.addEventListener("mouseover", () => twitter.classList.add("twitter-color"));
twitter.addEventListener("mouseout", () => twitter.classList.remove("twitter-color"));

contact.addEventListener("mouseover", () => contact.classList.add("contact-color"));
contact.addEventListener("mouseout", () => contact.classList.remove("contact-color"));

about.addEventListener("mouseover", () => about.classList.add("about-img"));
about.addEventListener("mouseout", () => about.classList.remove("about-img"));
contact_btn.addEventListener("mouseover", () => contact_btn.classList.add("btn-lg"));
contact_btn.addEventListener("mouseout", () => contact_btn.classList.remove("btn-lg"));

subscribe.addEventListener("mouseover", () => subscribe.classList.add("btn-lg"));
subscribe.addEventListener("mouseout", () => subscribe.classList.remove("btn-lg"));

