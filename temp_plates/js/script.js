/*============ SHOW MENU =================== */
// const navMenu = document.getElementById('nav-menu')
// const navToggle = document.getElementById('nav-toggle');
// const navClose = document.getElementById('nav-close');

const primaryNav = document.querySelector('.primary-navigation');
const navToggleMobile = document.querySelector('.mobile-nav-toggle');
const navCloseToggle = document.querySelector('.mobile-nav-toggle-close');


// document.querySelector('#element').style.display = 'none';  bard
const elSearcIcon = document.querySelector('.search-icon')
const elSearchMenu = document.querySelector('.middle-colume-search')






/*============ middle search bar =================*/

if(elSearcIcon){
    elSearcIcon.addEventListener('click', ()=>{
        elSearchMenu.classList.add('middle-search')
    })
}


/*========== Hambuger Menu for small devices =============*/

navToggleMobile.addEventListener('click', () => {
    const visibility = primaryNav.getAttribute('data-visible');
    // const hamMenuVisibility = navToggleMobile.getAttribute('data-visible');
    // const closeMenuVisiblity =  navCloseToggle.getAttribute('data-visible');

    if(visibility === "false"){
        primaryNav.setAttribute('data-visible', true);
        navToggleMobile.setAttribute('aria-expanded', true);
        navCloseToggle.setAttribute('aria-expanded', true);
    } 
});


navCloseToggle.addEventListener('click', () => {
    const visibility = primaryNav.getAttribute('data-visible');

    if(visibility === 'true'){
        navCloseToggle.setAttribute('aria-expanded', false);
        primaryNav.setAttribute('data-visible', false);  
        navToggleMobile.setAttribute('aria-expanded', false);
    }
});



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