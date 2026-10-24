$(function () {

  // Task 1: "Details" button shows/hides the text inside ITS OWN card
  $(".more-btn").on("click", function () {
    const card = $(this).closest(".card");      // go up to the card of this button
    card.find(".details").toggle();             // toggle only that card's paragraph

    // Change the button text
    if ($(this).text() === "Details") {
      $(this).text("Hide");
    } else {
      $(this).text("Details");
    }
  });

  // Task 2: hover effect using a CSS class
  $(".service").on("mouseenter", function () {
    $(this).addClass("hovered");
  });
  $(".service").on("mouseleave", function () {
    $(this).removeClass("hovered");
  });

  // Task 3: dark mode switch
  $("#themeBtn").on("click", function () {
    $("body").toggleClass("dark");

    // hasClass() returns true or false
    if ($("body").hasClass("dark")) {
      $(this).text("Light mode");
    } else {
      $(this).text("Dark mode");
    }
  });

  // Task 4: very small phone check (11 digits starting with 03)
  $("#callBtn").on("click", function () {
    const phone = $("#phone").val().trim();     // trim() removes extra spaces

    if (phone.length === 11 && phone.startsWith("03")) {
      $("#feedback").text("Thank you! We will call you soon.")
                    .attr("class", "mt-2 text-success");
    } else {
      $("#feedback").text("Please enter an 11-digit number like 03001234567.")
                    .attr("class", "mt-2 text-danger");
    }
  });

});
