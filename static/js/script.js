document.addEventListener('DOMContentLoaded',() => {

    const colour = document.querySelectorAll(".colours");
    const size = document.querySelectorAll(".card-size");
    const size1 = document.querySelector(".card-size1");
    const size2 = document.querySelectorAll(".card-size2");
    const size3 = document.querySelectorAll(".card-size3");
    const size4 = document.querySelectorAll(".card-size4");
    const allColour = document.querySelectorAll(".colours ,.colours1, .colours2, .colours3")
    const allsize = document.querySelectorAll(".card-size,.card-size1,.card-size2,.card-size3,.card-size4 ")
    function changecolor() {
        resetcolour();
        this.style.borderColor = "#3F4646";  
    }
    colour.forEach( (colour) => {
        colour.addEventListener('click',changecolor);
        
    });
    function resetcolour() {
        allColour.forEach(allcolour =>{
            allcolour.style.borderColor="#fff"
        });
    }
    // function resetstyles(){
    //     allsize.forEach(allsize  => {
    //         allsize.style.backgroundColor = "#fff";
    //         allsize.style.color = "#3C4242";
    //     });
    // }
    function resetstyles(excludeElement) {
        allsize.forEach(allsize  => {
            // Check if the current element is not the one that was clicked
            if (allsize !== excludeElement) {
                allsize.style.backgroundColor = "#fff";
                allsize.style.color = "#3C4242";
            }
        });
    }
    
    
    function handleClick(event) {

        if (event.target.classList.contains('card-size') ||
            event.target.classList.contains('card-size1') ||
            event.target.classList.contains('card-size2') ||
            event.target.classList.contains('card-size3') ||
            event.target.classList.contains('card-size4')) {
    
            resetstyles(event.target);
    
            event.target.style.backgroundColor = "black";
            event.target.style.color = "#fff";
        }
    }
    
    document.addEventListener('click',handleClick);


    const leftButton = document.querySelector(".left-arrow");
    const rightButton = document.querySelector(".right-arrow");
    const sliderContent = document.querySelector(".arrival-content");
    const visualcard = 0 ;
    let currentIndex = 0 ;
    const cardWidth = document.querySelector(".arrival-card-content").offsetWidth + 951.58 ;
    const totalcard = document.querySelectorAll(".arrival-card-content").length;
    

    leftButton.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateSlider();
            rightButton.style.display="flex";
        }else{(currentIndex === 0) 
            currentIndex++ ;
            updateSlider();
            rightButton.style.display="none";

        }
              
    });
    rightButton.addEventListener('click',() =>{
        if (currentIndex === 0) {
            currentIndex++ ;
            updateSlider();
            rightButton.style.display="none";
            
        }else {
            currentIndex=totalcard - visualcard;
            currentIndex--;
            updateSlider(); 
        }
    });
    
    function updateSlider() {
        sliderContent.style.transform =`translateX(-${ currentIndex * cardWidth }px)`;
    }
    const wishlist = document.querySelectorAll(".wishlist ");
    
    
    wishlist.forEach((like)=>{
        
        like.addEventListener("click",(event) =>{
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
       
    const wishlistIcons = document.querySelectorAll('.wishlist-icon');

    document.addEventListener('DOMContentLoaded', function() {
        const wishlistIcons = document.querySelectorAll('.wishlist-icon');
    
        // Add a click event listener to each wishlist icon
        wishlistIcons.forEach(function(icon) {
            icon.addEventListener('click', function() {
                // Toggle the "active" class on click
                this.classList.toggle('active');
            });
        });
    });
    const backgrounds = [
        'url("image/bg-1.jpg")',
        'url("image/bg-2.jpg")',
        'url("image/bg-3.jpg")'  
    ];
    
    let currentIndex1 = 0;
    const spotlight = document.getElementById('spotlight');
    
    document.querySelector('.slide-left').addEventListener('click', () => {
        currentIndex1 = (currentIndex1 === 0) ? backgrounds.length - 1 : currentIndex1 - 1;
        updateBackground();
        
    });
    
    document.querySelector('.slide-right').addEventListener('click', () => {
        currentIndex1 = (currentIndex1 === backgrounds.length - 1) ? 0 : currentIndex1 + 1;
        updateBackground();
        u
    });
    
    function updateBackground() {
        spotlight.style.backgroundImage = backgrounds[currentIndex1];
    };
    
    const explore = document.querySelectorAll(".explore");
    
    explore.forEach((button, index) => {
        button.addEventListener("click", () => {
            localStorage.setItem("selectedImageIndex", index);
            window.location.href = "product.html"; // Navigate to the single page
        });
    });


     document.querySelector(".close-icon").addEventListener("click",()=>{
        dropDown.style.display="none";
     })
    const dropDown = document.querySelector(".dropdown");
    document.querySelector(".menubar").addEventListener("click",() =>{
        dropDown.style.display="flex";
        
    })
    d
       
    
    
    
    
    
   
    

});


    




    
    