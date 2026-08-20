document.addEventListener("DOMContentLoaded", function () {
  var cannonBtn = document.getElementById("cannon-btn");
  var scrollHint = document.getElementById("scroll-hint");

  function burst() {
    if (typeof confetti !== "function") return;
    var colors = ["#FF4F93", "#35C6F4", "#8B5CF6", "#FFC94A", "#B7E552"];
    confetti({
      particleCount: 140,
      spread: 100,
      startVelocity: 45,
      origin: { y: 0.6 },
      colors: colors,
    });
    setTimeout(function () {
      confetti({
        particleCount: 80,
        angle: 60,
        spread: 70,
        origin: { x: 0 },
        colors: colors,
      });
      confetti({
        particleCount: 80,
        angle: 120,
        spread: 70,
        origin: { x: 1 },
        colors: colors,
      });
    }, 200);
  }

  if (cannonBtn) {
    cannonBtn.addEventListener("click", function () {
      burst();
      var story = document.getElementById("story") || document.getElementById("letter");
      if (story) {
        story.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  }

  if (scrollHint) {
    scrollHint.addEventListener("click", function (e) {
      e.preventDefault();
      var target = document.querySelector(scrollHint.getAttribute("href"));
      if (target) target.scrollIntoView({ behavior: "smooth" });
    });
  }

  var envelope = document.getElementById("envelope");
  var envelopeBtn = document.getElementById("envelope-btn");
  if (envelope && envelopeBtn) {
    envelopeBtn.addEventListener("click", function () {
      envelope.classList.add("is-open");
      envelopeBtn.setAttribute("aria-expanded", "true");
      burst();
    });
  }
});
