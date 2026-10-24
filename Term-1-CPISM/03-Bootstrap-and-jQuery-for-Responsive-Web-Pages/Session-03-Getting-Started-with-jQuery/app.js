// Wait until the HTML is ready, then run our code.
// $(function () { ... }) is the short form of $(document).ready(function () { ... })
$(function () {

  // ---------- 1. Change text with a selector ----------
  // $("#title") selects the element with id="title"
  $("#title").text("Hello jQuery - it works!");

  // ---------- 2. Show, hide and toggle ----------
  $("#hideBtn").on("click", function () {
    $("#message").hide();        // make the paragraph invisible
  });

  $("#showBtn").on("click", function () {
    $("#message").show();        // make it visible again
  });

  $("#toggleBtn").on("click", function () {
    $("#message").toggle();      // hide if visible, show if hidden
  });

  // ---------- 3. Add / remove / toggle a CSS class ----------
  // "#courses li" selects every <li> inside #courses
  $("#courses li").on("click", function () {
    // $(this) = the exact <li> that was clicked
    $(this).toggleClass("highlight");
  });

  // Double-click removes the highlight from ALL items
  $("#courses").on("dblclick", function () {
    $("#courses li").removeClass("highlight");
  });

  // ---------- 4. Read an input value on every key press ----------
  $("#nameInput").on("input", function () {
    let typedName = $(this).val();          // .val() reads the input value

    if (typedName === "") {
      typedName = "guest";                  // default when the box is empty
    }

    $("#nameOut").text(typedName);          // write it into the page
  });

  // ---------- 5. Hover events ----------
  $("#title").on("mouseenter", function () {
    $(this).css("color", "#0d6efd");        // blue when the mouse is over it
  });

  $("#title").on("mouseleave", function () {
    $(this).css("color", "");               // back to normal
  });

});
