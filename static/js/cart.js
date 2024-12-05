document.addEventListener("DOMContentLoaded", () => {
    const loginPage = document.querySelector(".login-form");
    const form = document.querySelector("form");
    const account = document.querySelector(".account");
    const account1 = document.querySelector(".logprofile");
    const logprofile = document.querySelector(".logprofile");

    // Check login status
    const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

    //  login status
    if (isLoggedIn) {
        if (loginPage) loginPage.style.display = "none";
        if (account) account.style.display = "none";
        if (account1) account1.style.display = "block";

        // Load profile  localStorage
        const userProfilePic = localStorage.getItem("isProfileDp");
        if (userProfilePic && logprofile) {
            logprofile.src = userProfilePic;
        }
    } else {
        if (loginPage) loginPage.style.display = "block";
        if (account) account.style.display = "block";
        if (account1) account1.style.display = "none";
    }

    //  submission
    form?.addEventListener("submit", (e) => {
        e.preventDefault();

        const username = form.username.value.trim();
        const password = form.password.value.trim();

        if (authenticate(username, password)) {
            localStorage.setItem("isLoggedIn", "true");

            if (account1?.src) {
                localStorage.setItem("isProfileDp", account1.src);
            }

            alert("Login successful!");
            if (loginPage) loginPage.style.display = "none";
            if (account) account.style.display = "none";
            if (account1) account1.style.display = "block";
        } else {
            alert("Error: Invalid credentials");
        }
    });

    // Authentication logic
    function authenticate(username, password) {
        return username === "admin" && password === "password";
    }

    // Click logic
    const clickableElements = document.querySelectorAll(".white-bg, .p-text");

    clickableElements.forEach((element) => {
        element.addEventListener("click", () => {
            if (!isLoggedIn) {
                alert("Please Login");
                if (loginPage) loginPage.style.display = "block";
            } else {
                
                
            }
        });
    });
    const logOutCursor = document.querySelector(".log-out-cursor");
    const logOutPage = document.querySelector(".acount-page")
    
    logOutCursor.addEventListener("click", () => {
        localStorage.removeItem("isLoggedIn");
        localStorage.removeItem("isProfileDp"); 
        // alert("Logout Successfully");
        if (loginPage) loginPage.style.display = "block";
        if (account) account.style.display = "block";
        if (account1) account1.style.display = "none";
        if(logOutPage) logOutPage.style.display = "none";
    });
    account1.addEventListener("click",(open) => {
        logOutPage.style.display="flex";
    });
    

});

        const wishlistIcons = document.querySelectorAll('.wishlist');
            wishlistIcons.forEach((like1)=>{
        
            like1.addEventListener("click",(event) =>{
                const redFilter = "invert(1) sepia(1) saturate(10000%) hue-rotate(0deg)";
                // const redFilter ="red"
            if (event.target.style.filter===redFilter){
                
                event.target.style.filter="";
                // localStorage.setItem("imageFilter","");
            } else{
                event.target.style.filter=redFilter;
                // localStorage.setItem("imageFilter",redFilter);
            }
        
            
            });
            }); 