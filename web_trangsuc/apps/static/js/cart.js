var updateBtns = document.querySelectorAll(".update-cart");

for (let i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    let productId = this.dataset.product;
    let action = this.dataset.action;

    console.log(`Product: ${productId}, Action: ${action}`);

    // Kiểm tra trạng thái đăng nhập
    if (userInfo.isAuthenticated === "false") {
      console.log("User not logged in");
    } else {
      console.log(`User logged in as: ${user_username}`);
    }
  });
}
