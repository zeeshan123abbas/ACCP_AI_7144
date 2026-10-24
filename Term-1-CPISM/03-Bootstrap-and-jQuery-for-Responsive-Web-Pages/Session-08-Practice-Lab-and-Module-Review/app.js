$(function () {

  // ---------- 1. Category filter ----------
  $("#filters button").on("click", function () {
    const category = $(this).data("filter");      // reads data-filter="..."

    // Button styles: make only the clicked one dark
    $("#filters button").removeClass("btn-dark").addClass("btn-outline-dark");
    $(this).removeClass("btn-outline-dark").addClass("btn-dark");

    if (category === "all") {
      $(".item").fadeIn(200);
    } else {
      $(".item").hide();                                        // hide everything
      $('.item[data-category="' + category + '"]').fadeIn(200); // show matching
    }
  });

  // ---------- 2. Live search ----------
  $("#search").on("input", function () {
    const word = $(this).val().toLowerCase();
    let visibleCount = 0;

    $(".item").each(function () {
      const itemText = $(this).text().toLowerCase();
      if (itemText.includes(word)) {
        $(this).show();
        visibleCount++;
      } else {
        $(this).hide();
      }
    });

    // Show the message only when nothing matched
    $("#noResults").toggle(visibleCount === 0);
  });

  // ---------- 3. Counters that count up once ----------
  $(".counter").each(function () {
    const counter = $(this);
    const target = counter.data("target");        // reads data-target="..."

    // animate() can animate ANY number, not just CSS
    $({ value: 0 }).animate({ value: target }, {
      duration: 1500,
      step: function (now) {
        counter.text(Math.floor(now));            // update text on every frame
      },
      complete: function () {
        counter.text(target);                     // make sure we end on the exact number
      }
    });
  });

});
