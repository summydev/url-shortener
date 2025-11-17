# URL Shortener

Built a URL shortener API with Django today. It's live and working.

**What works:**
- Shorten any URL
- Get a short code 
- Track how many times links are clicked
- Custom short codes
- REST API for frontends

**Live at:** `https://url-shortener-jgh8.onrender.com`

**For frontend:**
- POST to `/api/shorturls/` with `{"original_url": "your-url"}`
- GET from `/api/shorturls/` to see all URLs
- Visit `/{code}` to redirect

Built on Nov 17, 2025. Planning to add more features later.