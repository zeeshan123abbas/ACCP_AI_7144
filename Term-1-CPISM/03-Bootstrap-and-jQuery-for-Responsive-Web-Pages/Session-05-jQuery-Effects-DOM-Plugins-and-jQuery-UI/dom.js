$(function () {

  // Helper: build one <li> for a task
  function makeTask(text) {
    const item = $("<li></li>");                     // create a new element
    item.addClass("list-group-item");
    item.text(text);                                 // .text() is safe: no HTML injection
    item.append(' <button class="btn btn-sm btn-danger float-end del">x</button>');
    return item;
  }

  // Helper: update the counter
  function updateCount() {
    $("#count").text($("#tasks li").length);
  }

  // append() = add at the END of the list
  $("#addBtn").on("click", function () {
    const text = $("#taskInput").val().trim();
    if (text === "") return;                          // ignore empty input
    const newItem = makeTask(text);
    $("#tasks").append(newItem);
    newItem.flash();                                  // our own plugin (my-plugin.js)
    $("#taskInput").val("");                          // clear the box
    updateCount();
  });

  // prepend() = add at the START of the list
  $("#topBtn").on("click", function () {
    const text = $("#taskInput").val().trim();
    if (text === "") return;
    $("#tasks").prepend(makeTask(text));
    $("#taskInput").val("");
    updateCount();
  });

  // Delete button. We use "event delegation": the listener is on #tasks,
  // so it also works for buttons that are added later.
  $("#tasks").on("click", ".del", function (event) {
    event.stopPropagation();                          // do not also trigger the <li> click
    $(this).parent().fadeOut(300, function () {
      $(this).remove();                               // remove from the DOM after fading
      updateCount();
    });
  });

  // Click a task to mark it done (toggle a Bootstrap class)
  $("#tasks").on("click", "li", function () {
    $(this).toggleClass("text-decoration-line-through");
  });

  // attr() reads or changes an attribute
  $("#swapBtn").on("click", function () {
    const oldAlt = $("#pic").attr("alt");
    $("#pic").attr("alt", "Logo of the Bootstrap framework");
    console.log("alt changed from:", oldAlt, "to:", $("#pic").attr("alt"));
  });

});
