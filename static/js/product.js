const addtocart_button = document.getElementById('cart-button')

console.log("burrito")

addtocart_button.addEventListener('click', (e) => {
  e.preventDefault();

  Toastify({
    text: "Added to Cart",
    duration: 1500,
    newWindow: true,
    close: true,
    gravity: "top", 
    position: "center", 
    stopOnFocus: true,
    style: {
      background: "green",
    }
  }).showToast();
})