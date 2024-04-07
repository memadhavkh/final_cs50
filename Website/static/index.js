$(document).ready(function () {
  // Check for click events on the navbar burger icon
  $(".navbar-burger").click(function () {
    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
  });
});

(document.querySelectorAll(".notification .delete") || []).forEach(
  ($delete) => {
    const $notification = $delete.parentNode;

    $delete.addEventListener("click", () => {
      $notification.parentNode.removeChild($notification);
    });
  }
);
// ``- this allows us to embed a variable inside a string
function like(postId) {
  let likeCount = document.getElementById(`likes-count-${postId}`);
  const likeButton = document.getElementById(`like-button-${postId}`);

  fetch(`like-post/${postId}`, {method: "POST"})
  .then((res) => res.json()) // wait for response, and catch the response as soon as it arrives
  .then((data) => {
    likeCount.innerHTML = data['likes'];
    if(data['liked'] == false){
      likeButton.className = 'far fa-thumbs-up';
    }else{
      likeButton.className = 'fas fa-thumbs-up';
    }
  }); // for further access of the received data

}
