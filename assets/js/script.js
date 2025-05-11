document.addEventListener('DOMContentLoaded', function() {
    // منوی همبرگر برای نسخه موبایل
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    
    hamburger.addEventListener('click', function() {
        this.classList.toggle('active');
        navLinks.classList.toggle('active');
    });
    
    // بستن منو هنگام کلیک روی لینک
    const navItems = document.querySelectorAll('.nav-links a');
    navItems.forEach(item => {
        item.addEventListener('click', function() {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });
    
    // اسکرول نرم برای لینک‌ها
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // افکت اسکرول برای عناصر
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.slide-up, .fade-in');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 100) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
        
        // شمارنده آمار
        const stats = document.querySelectorAll('.stat-number');
        const statsSection = document.querySelector('.stats-section');
        const statsPosition = statsSection.getBoundingClientRect().top;
        
        if (statsPosition < windowHeight - 100 && !stats[0].classList.contains('animated')) {
            stats.forEach(stat => {
                const target = +stat.getAttribute('data-count');
                const count = +stat.innerText;
                const increment = target / 50;
                
                if (count < target) {
                    stat.innerText = Math.ceil(count + increment);
                    setTimeout(updateCount, 20);
                } else {
                    stat.innerText = target;
                    stat.classList.add('animated');
                }
                
                function updateCount() {
                    const current = +stat.innerText;
                    if (current < target) {
                        stat.innerText = Math.ceil(current + increment);
                        setTimeout(updateCount, 20);
                    } else {
                        stat.innerText = target;
                        stat.classList.add('animated');
                    }
                }
            });
        }
    };
    
    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll(); // برای عناصری که در ابتدا در viewport هستند
    
    // فیلتر محصولات
    const filterBtns = document.querySelectorAll('.filter-btn');
    const productItems = document.querySelectorAll('.product-card');
    
    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // حذف کلاس active از همه دکمه‌ها
            filterBtns.forEach(btn => btn.classList.remove('active'));
            // اضافه کردن کلاس active به دکمه کلیک شده
            this.classList.add('active');
            
            const filter = this.getAttribute('data-filter');
            
            productItems.forEach(item => {
                if (filter === 'all' || item.getAttribute('data-category') === filter) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
    
    // اکوردئون سوالات متداول
    const accordionBtns = document.querySelectorAll('.accordion-btn');
    
    accordionBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            this.classList.toggle('active');
            const content = this.nextElementSibling;
            
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + 'px';
            }
        });
    });
    
    // فرم تماس
    const contactForm = document.querySelector('.modern-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // اعتبارسنجی ساده
            const name = this.querySelector('#name');
            const email = this.querySelector('#email');
            const message = this.querySelector('#message');
            
            if (!name.value.trim()) {
                alert('لطفا نام خود را وارد کنید');
                name.focus();
                return;
            }
            
            if (!email.value.trim() || !validateEmail(email.value)) {
                alert('لطفا یک ایمیل معتبر وارد کنید');
                email.focus();
                return;
            }
            
            if (!message.value.trim()) {
                alert('لطفا پیام خود را وارد کنید');
                message.focus();
                return;
            }
            
            // ارسال فرم (شبیه‌سازی)
            alert('پیام شما با موفقیت ارسال شد. به زودی با شما تماس خواهیم گرفت.');
            this.reset();
        });
    }
    
    // تابع اعتبارسنجی ایمیل
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
});