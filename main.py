function createOrder() {

    let products = document.querySelectorAll(".product");
    let orderItems = document.getElementById("orderItems");
    let total = 0;
    orderItems.innerHTML = "";
    let hasOrder = false;

    products.forEach(function(product) {

        if (product.checked) {

            hasOrder = true;

            let name = product.getAttribute("data-name");
            let price = Number(product.getAttribute("data-price"));
            let menuItem = product.closest(".menu-item");
            let quantity =
                Number(menuItem.querySelector(".quantity").value);
            let subtotal = price * quantity;
            total += subtotal;
            let item = document.createElement("div");
            item.className = "summary-item";
            item.innerHTML =
                "<span>" +
                name +
                " × " +
                quantity +
                "</span>" +
                "<span>₱" +
                subtotal +
                "</span>";

            orderItems.appendChild(item);
        }
    });


    if (!hasOrder) {

        alert("Please select at least one product.");

        return;
    }


    document.getElementById("total").textContent =
        "₱" + total.toFixed(2);


    document.getElementById("summary").style.display =
        "block";
}

function createSKU() { 
    let category = document.getElementById("category").value; 
    let productName = document.getElementById("productName").value.trim(); 
    let stockQty = document.getElementById("stockQty").value; 
    let skuItems = document.getElementById("skuItems"); 

    if (!productName || !stockQty) { 
        alert("Please enter a product name and stock quantity."); 
        return; 
    } 

    let categoryCode = category.substring(0, 3).toUpperCase(); 
    
    let nameCode = productName.substring(0, 3).toUpperCase(); 
    
    let qtyCode = String(stockQty).padStart(3, "0"); 

    let sku = categoryCode + "-" + nameCode + "-" + qtyCode; 

    let item = document.createElement("div"); 
    item.className = "sku-item"; 
    item.innerHTML = "<div>" + 
                        "<div class='sku-code'>" + sku + "</div>" + 
                        "<div class='sku-details'>" + category + " · " + productName + " · Stock: " + stockQty + "</div>" + 
                     "</div>"; 

    skuItems.prepend(item); 

    document.getElementById("summary").style.display = "block"; 
    document.getElementById("productName").value = ""; 
    document.getElementById("stockQty").value = ""; 
}
