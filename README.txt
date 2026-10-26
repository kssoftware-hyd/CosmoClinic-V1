Cosmo International Clinic - plain HTML/CSS/JS site (15 pages)

DEPLOY: upload everything in this folder to public_html (cPanel File Manager). No build step. Open index.html locally to preview.

EDIT: change text directly in the .html files; styles in css/style.css; behaviour in js/script.js. Images: save in an images/ folder and replace each grey placeholder <div class="ph">...</div> with <img src="images/file.webp" alt="describe the image" loading="lazy">.

FORM: no backend is set up. On submit it validates and opens WhatsApp with the enquiry (it never claims a booking is made). To receive emails instead, connect Formspree or a PHP mail script. Never put secret keys in JavaScript.

CLIENT MUST SUPPLY: street address and Google Maps embed (contact.html), clinic hours, logo, clinic/hero/gallery photos, approved before/after images with patient consent, verified testimonials, doctor names/qualifications, about-us text, social media URLs, and doctor review of all treatment text and aftercare details.

TEST: all 15 pages load, mobile menu, form validation, call/email/WhatsApp links, lightbox (Esc closes), keyboard focus, 360/768/1280px widths, 404 page.

NOTE: Logo is in images/logo.png. Navigation and teal theme follow the screenshots of the existing site. WhatsApp/call number: +91 9246119111.
The old site's hero badges ("100% Successful Result", "15+ Years Experience", "100% Patient Comfort") were NOT copied: they are guarantee/experience claims that the clinic must confirm and legally substantiate first.

V3: index.html + css/home.css + js/home.js is the new home page (offer popup, results, stats). Footer on every page has Instagram, YouTube and Facebook icons (edit the three links in each footer if they change).
CONFIRM WITH CLIENT BEFORE LAUNCH: the "up to 30% off" offer and its terms, the stats strip (15+ years, DHI introduced in Hyderabad), the "Affordable Prices" card, and the Rs 40,000 to 2,00,000 price range in the FAQ.

V4 NOTES
- Images in /images (t-*, result-*, gallery-*, hero-*, about) are SAMPLE placeholders. Replace each file with the real photo using the same file name (download originals from the old site's wp-content/uploads).
- Testimonial videos: copy the 3 mp4 files from the old site into /videos as testimonial-1.mp4, testimonial-2.mp4, testimonial-3.mp4. Until then pages fall back to the old cosmoclinic.com video URLs, which stop working once the old WordPress site is removed.
- Counters: edit data-count in index.html (Happy Patients 1000+, Years 15+, Clinic 0, Procedures Everyday 0 are set as requested).
- Contact page address, hours (11:00 AM to 7:00 PM daily) and map come from the old site's business data. Confirm before launch.
- Claims left out of the home text on purpose: "100% safe/efficacy", "no side effects", "100% money back guarantee", "100% customer satisfaction", "highest in the industry", "best clinic". Add back only if the clinic can substantiate them.
