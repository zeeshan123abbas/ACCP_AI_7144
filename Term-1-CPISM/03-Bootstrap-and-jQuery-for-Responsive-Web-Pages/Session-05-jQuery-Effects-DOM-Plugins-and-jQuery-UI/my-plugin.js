// A tiny jQuery plugin: makes any element "flash" yellow for a moment.
// Usage:  $("#title").flash();    or    $(".card").flash(1000);

// $.fn is where jQuery keeps its methods. Adding a function here
// makes it available on every selection, just like .hide() or .text().
$.fn.flash = function (duration) {
  // Default duration if none is given
  const time = duration || 600;

  // "this" = the jQuery selection. return it so chaining still works.
  return this.each(function () {
    const element = $(this);
    element.css("background-color", "yellow");

    // After "time" milliseconds, remove the colour again
    setTimeout(function () {
      element.css("background-color", "");
    }, time);
  });
};
