/*============ SHOW MENU =================== */
const primaryNav = document.querySelector('.primary-navigation');
const navToggleMobile = document.querySelector('.mobile-nav-toggle');
const navCloseToggle = document.querySelector('.mobile-nav-toggle-close');

const elSearcIcon = document.querySelector('.search-icon');
const elSearchMenu = document.querySelector('.middle-colume-search');

// variables for chatbot 
const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");
const chatbox = document.querySelector(".chatbox");
const chatBotToggler = document.querySelector(".chatbot-toggler");
const chatbotCloseBtn = document.querySelector(".close-btn");





/*============== middle search bar =====================*/
if(elSearcIcon){
    elSearcIcon.addEventListener('click', ()=>{
        elSearchMenu.classList.add('middle-search')
    })
}


/*=============== Hambuger Menu for small devices =================*/

// prevent and enable scrolling when hambuger menu is clicked
function disableScroll() {
    // Get the current page scroll position
    scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
  
        // if any scroll is attempted, set this to the previous value
        window.onscroll = function() {
            window.scrollTo(scrollLeft, scrollTop);
        };
}
function enableScroll() {
    window.onscroll = function() {};
}  

navToggleMobile.addEventListener('click', () => {
    const visibility = primaryNav.getAttribute('data-visible');
    // const hamMenuVisibility = navToggleMobile.getAttribute('data-visible');
    // const closeMenuVisiblity =  navCloseToggle.getAttribute('data-visible');
   
    // Get the window object.
    var window = window;

    disableScroll() 
    if(visibility === "false"){
        primaryNav.setAttribute('data-visible', true);
        navToggleMobile.setAttribute('aria-expanded', true);
        navCloseToggle.setAttribute('aria-expanded', true);
    } 
});
navCloseToggle.addEventListener('click', () => {
    const visibility = primaryNav.getAttribute('data-visible');

    enableScroll()
    if(visibility === 'true'){
        navCloseToggle.setAttribute('aria-expanded', false);
        primaryNav.setAttribute('data-visible', false);  
        navToggleMobile.setAttribute('aria-expanded', false);
    }
});
function preventScrolling() {
    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('mobile-nav-toggle')) {
        event.preventDefault();
        document.body.classList.add('no-scroll');
        } else if (event.target.classList.contains('close-menu')) {
        document.body.classList.remove('no-scroll');
        }
    });
}
window.onload = preventScrolling;



/*==================== CHAT BOT =======================*/
var userMessenger;
var API_KEY = "";
const inputInitHeight = chatInput.scrollHeight;

const createChatLi = (message, className) => {
    // create a chat <li> element with passed message and className
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", className);

    let chatContent = className === "outgoing" ? `<p></p><span class="material-symbols-outlined">
    <img src="images/user.png" alt=""></span>` : ` <span class="material-symbols-outlined">
    <img src="images/chatbot.png" alt=""></span><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi;
}
const generateResponse = (incomingChatLi) => {
    const API_URL = "https://api.openai.com/v1/chat/completions";
    const messageElement = incomingChatLi.querySelector("p");

    const requestOptions = {
        method :"POST",
        Headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${API_KEY}`
        },
        body: JSON.stringify({
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": userMessenger}]
        })
    }  
    
    fetch(API_URL, requestOptions).then(res => res.json()).then(data => {
        // console.log(data);
        messageElement.textContent = data.choices[0].message.content;
    }).catch((error) => {
        // console.log(error);

       
        messageElement.classList.add("error");   //add to style the error
        messageElement.textContent = "Oops! Something went wrong. Please try again.";
    }).finally(() => chatbox.scrollTo(0, chatbox.scrollHeight));
}

//chatbot
const handleChat = () =>  {
    userMessenger = chatInput.value.trim();
    if(!userMessenger) return;
    chatInput.value = "";

    //reset the textarea height to its default height once a message is sent
    chatInput.style.height = `${chatInput.scrollHeight}px`;


    // append user's message to the chatbox
    chatbox.appendChild(createChatLi(userMessenger, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);


    setTimeout(() => {
        // chatbox.appendChild(createChatLi("...", "incoming"));

        const incomingChatLi = createChatLi("...", "incoming");
        chatbox.appendChild(incomingChatLi);
        chatbox.scrollTo(0, chatbox.scrollHeight);
        generateResponse(incomingChatLi);
    }, 600);
};

// adjust the height of the input textarea based on it's content
chatInput.addEventListener("input", () => {
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

// if Enter key is press without shift key and the window with is greater than 800px, handle the chat
chatInput.addEventListener("keydown", (e) => {
    if(e.key === 'Enter' && !e.shiftkey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
    }
});
sendChatBtn.addEventListener("click", handleChat);
chatbotCloseBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
chatBotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));


  
/*=============== EXTERNAL LINK SCREEN  ===============*/
const detailImage = document.querySelector(".post-image");
const sharelinkOne = document.querySelector(".share-link");
const postdetailOne = document.querySelector(".post-main-detail");
const externalOne = document.querySelector(".external-share-container");


// Create a function to check if the share container is reached
function isDivReached() {
  // Get the current scroll position
  const scrollPosition = window.scrollY;

  // Check if the scroll position is greater than or equal to the top of the div
  return scrollPosition >= externalOne.offsetTop - 750;
}

// Add an event listener to the window scroll event
// window.addEventListener('scroll', function (e) {
//     e.preventDefault();
//   // Check if the div is reached//
//   if (isDivReached()) {
//     sharelinkOne.classList.add('share-java');
//   }
//   else {
//     sharelinkOne.classList.remove('share-java');
//   }
// });

// function Reached() {
//     // Get the current scroll position
//     const scrollPosition = window.scrollY;

//     // Check if the scroll position is greater than or equal to the top of the div
//     return scrollPosition <= externalOne.offsetTop;
// }

// prevent scroll event
// window.addEventListener('scroll', function (e) {
//     if(Reached){
//         sharelinkOne.classList.add("share-scroll");
//     }
// });
// window.addEventListener('scroll', function (e) {
//     const scrollPosition = window.pageYOffset;
    
//     if (scrollPosition <= externalOne.offsetTop - 655) {
//         sharelinkOne.classList.add('share-scroll');
//     } else {
//         sharelinkOne.classList.remove('share-scroll');
//     }
// });



/*=============== POPUP SHARE LIKE SCREEN ===============*/
const shareEl = document.querySelector('.share-share');
const socialContainerEl = document.querySelector('.social-scroll-wrapper');
const hidePopupWidget = document.querySelector('.kat');


let showMes = false;
// var showWidget = true;

function popShareScreen(){
    if(shareEl){
        shareEl.addEventListener('click', () => {
            socialContainerEl.classList.add('show-social-links');
            likePop.classList.remove('alert-active');
            
            showMes = true;
            if(showMes){
                document.body.style.overflow = 'hidden';
                
            }
        
            document.addEventListener('click', (e) => {
                if (!socialContainerEl.contains(e.target) && !shareEl.contains(e.target)) {
                    socialContainerEl.classList.remove('show-social-links');
                    document.body.style.overflow = 'auto';
                  
                }
            });    
        });
    }
};
popShareScreen();






const likeMouseOver = document.querySelector('.share-like');
const commentMouseOver = document.querySelector('.share-comment');
const bookmarkMouseOver = document.querySelector('.share-bookmark');
const shareMouseOver = document.querySelector('.share-share');
const likePop = document.querySelector('.pop-like');
const commentPop = document.querySelector('.pop-comment');
const bookmarkPop = document.querySelector('.pop-bookmark');
const sharePop = document.querySelector('.pop-share');

function showWidget() {
    if(likeMouseOver) {
        likeMouseOver.addEventListener('mouseover', () =>{

            setTimeout(() => {
                likePop.classList.add('alert-active');
            }, 10);
            likeMouseOver.addEventListener('mouseout', () =>{
                likePop.classList.remove('alert-active');
            })
        });
    }

    if(commentMouseOver){
        commentMouseOver.addEventListener('mouseover', () =>{
            setTimeout(() => {
                commentPop.classList.add('alert-active');
            }, 10);
            commentMouseOver.addEventListener('mouseout', () =>{
                commentPop.classList.remove('alert-active');
            })
        });
    }
    if(bookmarkMouseOver){
        bookmarkMouseOver.addEventListener('mouseover', () =>{
            setTimeout(() => {
                bookmarkPop.classList.add('alert-active');
            }, 10);
            bookmarkMouseOver.addEventListener('mouseout', () =>{
                bookmarkPop.classList.remove('alert-active');
            })
        });
    }
    if(shareMouseOver){
        shareMouseOver.addEventListener('mouseover', () =>{
            setTimeout(() => {
                sharePop.classList.add('alert-active');
            }, 10);
            shareMouseOver.addEventListener('mouseout', () =>{
                sharePop.classList.remove('alert-active');
            })
        });
    }
};
showWidget();







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






/*================= REDIRECT TO EXTERNAL SOCIAL APP ===================*/
// Get all share buttons
const shareButtons = document.querySelectorAll('.share-button');

// Add click event listener to each button
shareButtons.forEach(button => {
   button.addEventListener('click', (e) => {
      e.preventDefault();

      // Get the URL of the current page
      const url = window.location.href;

      // Get the social media platform from the button's class name
      const platform = button.classList[1];

      // Set the URL to share based on the social media platform
      let shareUrl;
      switch (platform) {
         case 'facebook':
         shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`;
         break;
         case 'twitter':
         shareUrl = `https://twitter.com/share?url=${encodeURIComponent(url)}`;
         break;
         case 'linkedin':
         shareUrl = `https://www.linkedin.com/shareArticle?url=${encodeURIComponent(url)}`;
         break;
         case 'reddit':
         shareUrl = `https://reddit.com/submit?url=${encodeURIComponent(url)}`;
         break;
         case 'whatsapp':
         shareUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(url)}`;
         break;
      }

      // Open a new window to share the URL
      window.open(shareUrl, '_blank');
   });
});

// copy permalink/url when user click permalink button
const button = document.querySelector('.permalink');
const copyArticl = document.querySelector('.permalink-message');

function permalinkShare(){
    if(button){
        button.addEventListener('click', (e) => {

            e.preventDefault()
            const url = window.location.href;
            const copied = navigator.clipboard.writeText(url);
        
            if (copied) {
                copyArticl.classList.add('show-permalink-message');
                e.preventDefault();
        
                setTimeout(()=>{
                    copyArticl.classList.remove('show-permalink-message');
                }, 1500);
            } 
        });
    };
}
permalinkShare();




/*========================= DARK MODE =======================   activate-mode */
const setDarkEl = document.querySelector('.darkmode-setup');
const setSunsetEl = document.querySelector('.sunset-setup');
// const darkModeToggler = document.querySelector('.darkmode-set');

setDarkEl.addEventListener('click', () => {
    if(setDarkEl){
        setDarkEl.setAttribute('aria-expanded', true);
        setSunsetEl.setAttribute('aria-expanded', true);
        document.body.classList.toggle("dark-mode-theme");


        //update the local storage when user click on the button
        if(localStorage.getItem("theme") == "light"){
            localStorage.setItem("theme", "dark");
        } else{
            localStorage.setItem("theme", "light")
        }
    }
   
     
   
  
})

setSunsetEl.addEventListener('click', () => {
    if(setSunsetEl){
        setSunsetEl.setAttribute('aria-expanded', false);
        setDarkEl.setAttribute('aria-expanded', false);
        document.body.classList.remove("dark-mode-theme");

        //update the local storage when user click on the button
        if(localStorage.getItem("theme") == "dark"){
            localStorage.setItem("theme", "light");
        } else {
            localStorage.setItem("theme", "light");
        }
    }
});


if(localStorage.getItem("theme") == "light"){
    document.body.classList.remove("dark-mode-theme");
} else if(localStorage.getItem("theme") == "dark"){
    document.body.classList.add("dark-mode-theme");
} else {
    // execute when a user first the website for the first time
    localStorage.setItem("theme", "light");
}


// localStorage.clear();
// if(localStorage.getItem("theme") == "light"){
//     document.body.classList.remove("dark-mode-theme");
//     setDarkEl.classList.remove('activate-mode');

// } else if(localStorage.getItem("theme") == "dark"){
//     document.body.classList.add("dark-mode-theme");
//     setDarkEl.classList.add('activate-mode');

// } else{
//     // execute when a user first the website for the first time
//     localStorage.setItem("theme", "light")
// }










// const icon1 = document.querySelector('.dark-set');
// const icon2 = document.querySelector('.sun-set');

// function toggleIcons() {
//   const currentIcon = icon1.classList.contains('active') ? icon2 : icon1;
//   currentIcon.classList.add('activate-mode');
//   currentIcon.classList.remove('activate-mode');
// }

// icon1.addEventListener('click', toggleIcons);
// icon2.addEventListener('click', toggleIcons);