$(function () {

  // ---------- 1. Smooth scroll for links that start with "#" ----------
  $('a[href^="#"]').on("click", function (event) {
    const targetId = $(this).attr("href");        // e.g. "#contact"
    const target = $(targetId);
    if (target.length === 0) return;               // no such section: do nothing

    event.preventDefault();                        // stop the instant jump
    $("html, body").animate({ scrollTop: target.offset().top - 56 }, 600);

    // Close the mobile menu after a click (Bootstrap collapse API)
    $("#nav").removeClass("show");
  });

  // ---------- 2. Back-to-top button + active menu item on scroll ----------
  $(window).on("scroll", function () {
    const scrolled = $(window).scrollTop();

    // Show the button after 300px
    if (scrolled > 300) {
      $("#toTop").fadeIn();
    } else {
      $("#toTop").fadeOut();
    }

    // Find which section is on screen and highlight its link
    $("section").each(function () {
      const top = $(this).offset().top - 80;
      const bottom = top + $(this).outerHeight();
      if (scrolled >= top && scrolled < bottom) {
        const id = $(this).attr("id");
        $(".nav-link").removeClass("active");
        $('.nav-link[href="#' + id + '"]').addClass("active");
      }
    });
  });

  // ---------- 3. Form validation with jQuery + Bootstrap classes ----------
  function showResult(input, isValid) {
    // Bootstrap shows the red message when "is-invalid" is present
    input.toggleClass("is-invalid", !isValid);
    input.toggleClass("is-valid", isValid);
  }

  $("#demoForm").on("submit", function (event) {
    event.preventDefault();                        // stay on this page

    const name = $("#name").val().trim();
    const email = $("#email").val().trim();
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;   // simple email check

    const nameOk = name.length >= 3;
    const emailOk = emailPattern.test(email);

    showResult($("#name"), nameOk);
    showResult($("#email"), emailOk);

    if (nameOk && emailOk) {
      // ---------- 4. jQuery fills the text, Bootstrap opens the modal ----------
      $("#thanksName").text(name);
      const modal = bootstrap.Modal.getOrCreateInstance("#thanksModal");
      modal.show();
      this.reset();                                // clear the form
      $("#demoForm .form-control").removeClass("is-valid");
    }
  });

});
