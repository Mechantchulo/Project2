// NAVBAR START
document.querySelector('.hamburger').addEventListener('click', function() {
    const navLinks = document.querySelector('.nav-links');
    if (navLinks.style.display === 'none') {
        navLinks.style.display = 'block';
    } else {
        navLinks.style.display = 'none';
    }
});

// SCROLL
const myDiv = document.getElementById('myDiv');
const logo = document.getElementById('logo');
const scrolledLogo = document.getElementById('scrolledLogo');

window.addEventListener('scroll', function() {
    if (window.scrollY >= 90) {
        myDiv.className = 'header header-bg';
        logo.style.display = 'none';
        scrolledLogo.style.display = 'block';
    } else {
        myDiv.className = 'header';
        logo.style.display = 'block';
        scrolledLogo.style.display = 'none';
    }
});


// NAVBAR END

// faq items
const faqData = [
    {
        question: 'What is Ranqiify?',
        answer: 'Next.js is a React framework that enables functionality such as server-side rendering and generating static websites.'
    },
    {
        question: 'Can I use Ranqiify for free?',
        answer: 'Yes!, Next.js is a React framework that enables functionality such as server-side rendering and generating static websites.'
    },
    {
        question: 'Can I use Ranqiify for free?',
        answer: 'Yes!, Next.js is a React framework that enables functionality such as server-side rendering and generating static websites.'
    },
    {
        question: 'Can I use Ranqiify for free?',
        answer: 'Yes!, Next.js is a React framework that enables functionality such as server-side rendering and generating static websites.'
    },
    {
        question: 'Can I use Ranqiify for free?',
        answer: 'Yes!, Next.js is a React framework that enables functionality such as server-side rendering and generating static websites.'
    },
    
];

$(document).ready(function() {
    faqData.forEach(function(faq, index) {
        const faqItem = `
            <div class="faq-item">
                <div class="faq-question" id="faq-question-${index}">
                    <h3>${faq.question}</h3>
                    <div id="icon-${index}" style="font-size: 1.8rem;">+</div>

                </div>
                <div class="faq-answer" id="faq-answer-${index}" style="display: none;">${faq.answer}</div>
                <hr class="faq-line" />
            </div>
        `;
        $('#faq-container-wrap').append(faqItem);

        $(`#faq-question-${index}`).click(function() {
            const answer = $(`#faq-answer-${index}`);
            const icon = $(`#icon-${index}`);
            if (answer.is(":visible")) {
                answer.hide();
                icon.text('+');
            } else {
                // Close all FAQ items
                $('.faq-answer').hide();
                $('.faq-question div').text('+');

                // Open the clicked FAQ item
                answer.show();
                icon.text('-');
            }
        });
    });
});

// FAQ END

// YEAR

function getNewYear() {
    const today = new Date();
    const year = today.getFullYear();
    return year;
}

document.getElementById("year").textContent = getNewYear();
// END

// SCROLL TO TOP
 // When the user scrolls down 20px from the top of the document, show the button
 window.onscroll = function() {scrollFunction()};

 function scrollFunction() {
     var myBtn = document.getElementById("myBtn");
     if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
         myBtn.style.display = "block";
     } else {
         myBtn.style.display = "none";
     }
 }

 // When the user clicks on the button, scroll to the top of the document smoothly
 function topFunction() {
     window.scrollTo({ top: 0, behavior: 'smooth' });
 }
// END