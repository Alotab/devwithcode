const containerEl = document.querySelector(".form-main-container");
const signinEl = document.getElementById("sign-in");
const wrapperEl = document.querySelector(".wrapper");
const closeIcon = document.querySelector(".close-icon")
const signupForm = document.querySelector(".form")


//  show the login screen when user clicks on the "Login" button
signinEl.addEventListener('click', ()=> {
    containerEl.classList.add("form-main-container-popup");
    document.getElementById("main-page").style.filter = "blur(1px)";
    // document.getElementById("main-page").style.position = "fixed";
});


// Close Sign up page
closeIcon.addEventListener('click', ()=>{
    containerEl.classList.remove("form-main-container-popup");
    document.getElementById("main-page").style.filter = "";
    document.getElementById("main-page").style.position = "";
});




