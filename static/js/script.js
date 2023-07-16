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



// CHAT BOT
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


  





//scroll loading
// const postEl = document.querySelector('.post');


//set current page number
// let limit = 10;
// let page = 1;
// let pageNumber = 1;



// async function fetchImage() {
//     //https://jsonplaceholder.typicode.com/posts
//     try {
//          const windows = "{% url 'blog:home' %}";
//         // const postsUrl = `${window.location.origin}/posts`;
//         const response = await fetch(windows, {
//             method: 'GET',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'X-Requested-With': 'XMLHttpRequest',
//             },
//             params: {
//                 page: pageNumber,
//             },
//       });
//       if (!response.ok) {
//         throw new Error("Network response was not OK");
//       }
//       const data = await response.json();
//     //   console.log(data);

//     } catch (error) {
//       console.error("There has been a problem with your fetch operation:", error);
//     }
// }

// fetchImage();

// const dataURL = ''
// $(document).ready(function () {
//     var page = 1;
//     var block_request = false;
//     var end_pagination = false;

//     $(window).scroll(function () {
//         var margin = $(document).height() - $(window).height() - 200;

//         if ($(window).scrollTop() > margin && end_pagination === false && block_request === false) {
//             block_request = true;
//             page += 1;

//             $.ajax({
//                 type: 'GET',
//                 url: window,
//                 data: {
//                     "page": page
//                 },
               
//                 success: function (data) {
//                     if (data.end_pagination === true) {
//                         end_pagination = true;
                   
//                     } else {
//                         block_request = false;
//                     }
//                     $('.post').append(data.content);
//                 }
//             })
//         }
//     });
// })



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

// scroll


const loadBtn = document.querySelector('.load-post');
const loadPostHide = document.querySelector('.load-post');


function loadmorePost(){
    var current_time = $('.post').length;

    const content_add_post = document.getElementById('middle-colume-post');

    $.ajax({
        url:'fetch/',
        type: 'GET',
        data: {
            'total_item': current_time
        },
        beforeSend: function(){
            loadPostHide.classList.add('.hide');

            //spinner appears
        },
        success: function(response){
            const data = response.posts;

            data.map( post=>{
                content_add_post.innerHTML += `
                <div class="post">
                    <div class="author-profile">
                        <div class="author-image">
                        
                        
                        </div>
                        <!-- <div class="post-author-details">
                            {% with author=post.author %}
                                <a href="#"><p>{{ author.first_name}} {{ author.last_name}}</p></a>
                                <p id="time-tag"  class="post-date">{{ post.publish |date:'M d' }} &middot; {{ post.get_readtime }} read</p>
                            
                            {% endwith %}
                    
                        </div> -->
                    
                    </div>
                    <div class="post-header">
                        <a href="${ post.get_absolute_url }">
                        
                            <h4>${ post.title }</h4>
                        </a>
                    </div>
                    <!-- <div class="post-tags">
                        {% for post in post.tags.all %}
                            <a class="post-tag-chrome" href="#"><span></span>${ post }</a>
                        {% endfor %}
                    </div> -->
        
                    <div class="comment-share">
                        <div class="post-comment">
                            <a href="#">
                                <img src="{% static 'images/commentIcon.svg' %}" alt="comment" class="post-comment-icon">
                                <p>Add Comment</p>
                            </a>
                        </div>
                        <div class="post-share">
                            <a href="#"><img src="{% static 'images/share_2.svg' %}"></a>
                        </div>
                    </div> 
                </div>
                `
            });
            loadPostHide.classList.remove('.hide');
            history.replaceState(null, null, ' ');

        },
        error: function(error){

        }
    })

}


// loadBtn.addEventListener('click', (e) =>{
//     e.preventDefault();
//     loadmorePost();
// });