/* ========================= */
/* SECURITY FIX */
/* ========================= */

history.replaceState(null, '', `#${tabId}`);

/* ========================= */
/* BLOG RENDER */
/* ========================= */

const blogGrid = document.getElementById('blogGrid');

if(blogGrid){

    blogGrid.innerHTML = blogs.map(b => `
        <div class="blog-card">

            <img
                loading="lazy"
                decoding="async"
                src="${b.img}"
                alt="${b.title}"
            >

            <div class="blog-card-content">

                <h3>${b.title}</h3>

                <span class="filter-btn" style="background:#1e293b;">
                    ${b.topic}
                </span>

                <p>
                    Explore modern ${b.topic} strategies,
                    scalable architectures,
                    and enterprise engineering insights.
                </p>

            </div>
        </div>
    `).join('');
}

/* ========================= */
/* CONTACT FORM */
/* ========================= */

const contactForm = document.getElementById('secureContactForm');
const fb = document.getElementById('formFeedback');

contactForm?.addEventListener('submit', async (e) => {

    e.preventDefault();

    const name = document.getElementById('fullname').value.trim();
    const email = document.getElementById('email').value.trim();
    const msg = document.getElementById('message').value.trim();

    if (!name || !email || !msg) {

        fb.textContent = 'All fields required.';
        fb.style.color = '#ffb7b2';

        return;
    }

    const validEmail = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

    if (!validEmail.test(email)) {

        fb.textContent = 'Valid email required.';
        fb.style.color = '#ffb7b2';

        return;
    }

    fb.textContent = 'Sending message...';
    fb.style.color = '#60a5fa';

    try {

        await emailjs.send(
            'YOUR_SERVICE_ID',
            'YOUR_TEMPLATE_ID',
            {
                from_name: name,
                from_email: email,
                message: msg,
                to_email: 'mutethiaantony715@gmail.com'
            }
        );

        fb.textContent =
            '✅ Message sent successfully. Fortuna Labs will contact you shortly.';

        fb.style.color = '#8ef7a9';

        contactForm.reset();

    } catch (error) {

        console.error(error);

        fb.textContent =
            '❌ Failed to send message. Please try again later.';

        fb.style.color = '#ffb7b2';
    }

    setTimeout(() => {
        fb.textContent = '';
    }, 6000);
});

/* ========================= */
/* NEWSLETTER */
/* ========================= */

async function newsletterSubscribe(){

    const emailInput =
        document.getElementById('footerNewsEmail');

    const email = emailInput.value.trim();

    const validEmail =
        /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

    if(!validEmail.test(email)){

        document.getElementById(
            'newsletterFeedback'
        ).textContent =
            '❌ Please enter a valid email address.';

        return;
    }

    const btn =
        document.getElementById('footerNewsBtn');

    btn.disabled = true;
    btn.textContent = 'Subscribing...';

    try{

        await emailjs.send(
            'YOUR_SERVICE_ID',
            'YOUR_TEMPLATE_ID',
            {
                subscriber_email: email,
                to_email: 'mutethiaantony715@gmail.com'
            }
        );

        document.getElementById(
            'newsletterFeedback'
        ).textContent =
            '✅ Successfully subscribed to Fortuna updates.';

        btn.textContent = 'Subscribed ✓';

        emailInput.value = '';

        setTimeout(() => {

            btn.disabled = false;
            btn.textContent = 'Subscribe →';

            document.getElementById(
                'newsletterFeedback'
            ).textContent = '';

        }, 3000);

    }catch(error){

        console.error(error);

        document.getElementById(
            'newsletterFeedback'
        ).textContent =
            '❌ Subscription failed. Please try again.';

        btn.disabled = false;
        btn.textContent = 'Try Again';
    }
}

document.getElementById('footerNewsBtn')
?.addEventListener('click', newsletterSubscribe);

/* ========================= */
/* PERFORMANCE */
/* ========================= */

document.addEventListener('visibilitychange', () => {

    if(document.hidden){

        clearInterval(autoInterval);

    } else {

        startAutoSlide();
    }
});