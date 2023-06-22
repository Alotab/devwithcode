/*============ SHOW MENU =================== */
const navMenu = document.getElementById('nav-menu')
const navToggle = document.getElementById('nav-toggle');
const navClose = document.getElementById('nav-close');

// const elSearcIcon = document.getElementById('icon')
// document.querySelector('#element').style.display = 'none';  bard
const elSearcIcon = document.querySelector('.search-icon')
const elSearchMenu = document.querySelector('.middle-colume-search')


if (navToggle){
    navToggle.addEventListener('click', () =>{
        navMenu.classList.add('show-menu')
    })
   
}

if(navClose){
    navClose.addEventListener('click', () =>{
        navMenu.classList.remove('show-menu')
    })
}
/*============ middle search bar =================*/

if(elSearcIcon){
    elSearcIcon.addEventListener('click', ()=>{
        elSearchMenu.classList.add('middle-search')
    })
}

// if(elSearcIcon){
//     elSearcIcon.addEventListener('click', ()=>{
//         elSearchMenu.classList.remove('middle-search')
//     })
// }







/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 400
})
sr.reveal(`.home__data, .footer__container, .footer__group`);
sr.reveal(`.portfolio-container, .portfolio-card`, {delay: 700, origin: 'bottom'})
sr.reveal(`.portfolio-container, .portfolio-card`, {interval: 100})
sr.reveal(`.my-profile-introduction`, {origin: 'left'})
sr.reveal(`.my-profile-image`, {origin: 'right'})