// ── Scroll reveal (fallback if base.html script hasn't run yet)
document.addEventListener('DOMContentLoaded', () => {
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(el => {
            if (el.isIntersecting) {
                el.target.classList.add('visible');
                revealObserver.unobserve(el.target);
            }
        });
    }, { threshold: 0.12 });

    document.querySelectorAll('.reveal, .reveal-stagger').forEach(el => revealObserver.observe(el));

    // Navbar scroll shadow
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            navbar.style.boxShadow = '0 4px 30px rgba(0,0,0,0.5)';
        } else {
            navbar.style.boxShadow = 'none';
        }
    });
});