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
        social[i].classList.add("fa-1x");
    })
    social[i].addEventListener("mouseout", function(){
        social[i].classList.remove("fa-1x");
    })
}

function changeNavBtnIcon() {
    let navIcon = document.querySelector('#nav-icon');
    if (navIcon.className === 'fas fa-bars') {
        navIcon.className = 'fas fa-times'
    }else {
        navIcon.className = 'fas fa-bars'
    }
}

// // Get the container element
// const btnContainer = document.querySelector("#activeList");

// // Get all buttons with class="btn" inside the container
// const activeBtns = btnContainer.children;

// // Loop through the buttons and add the active class to the current/clicked button
// for (let i = 0; i < activeBtns.length; i++) {
//   activeBtns[i].addEventListener("click", function() {
//     let current = document.getElementsByClassName("active");
//     this.className += " active";


//     // If there's no active class
//     if (current.length > 0) {
//       current[0].className = current[0].className.replace(" active", "");
//     }

//     // Add the active class to the current/clicked button
//     this.className += " active";
//   });
// }

linkedin.addEventListener("mouseover", () => linkedin.classList.add("linkedin-color"));
linkedin.addEventListener("mouseout", () => linkedin.classList.remove("linkedin-color"));

twitter.addEventListener("mouseover", () => twitter.classList.add("twitter-color"));
twitter.addEventListener("mouseout", () => twitter.classList.remove("twitter-color"));

contact.addEventListener("mouseover", () => contact.classList.add("contact-color"));
contact.addEventListener("mouseout", () => contact.classList.remove("contact-color"));


