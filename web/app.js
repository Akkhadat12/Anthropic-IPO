(function () {
  var order = ["cover", "s1", "s2", "s3", "s4", "s5", "s6", "close"];
  var names = {
    cover: "Cover. Can growth pay for the frontier?",
    s1: "Scene 1. Two financial bases.",
    s2: "Scene 2. Customer work and paid use.",
    s3: "Scene 3. Price and compute per task.",
    s4: "Scene 4. Operating loss and adjusted signal.",
    s5: "Scene 5. Capacity and future obligations.",
    s6: "Scene 6. Four proof gates.",
    close: "Closing. Two clocks. One cash test."
  };
  var index = 0;
  var lock = false;
  var live = document.getElementById("live");
  var sources = document.getElementById("sources");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function sceneEls() {
    return Array.prototype.slice.call(document.querySelectorAll(".scene"));
  }

  function currentEl() {
    return document.querySelector('.scene[data-scene="' + order[index] + '"]');
  }

  function setLive(id) {
    live.textContent = names[id];
  }

  function finishLeave(prev) {
    prev.hidden = true;
    prev.inert = true;
    prev.classList.remove("is-current", "is-leaving");
  }

  function show(nextIndex) {
    if (nextIndex === index || lock) return;
    if (nextIndex < 0 || nextIndex >= order.length) return;
    var prev = currentEl();
    index = nextIndex;
    var next = currentEl();
    lock = true;
    if (sources.open) sources.close();

    next.hidden = false;
    next.inert = false;
    next.classList.add("is-current");
    if (prev) prev.classList.add("is-leaving");

    var release = function () {
      if (prev) finishLeave(prev);
      lock = false;
      var target = next.querySelector("[data-advance]");
      if (target) target.focus({ preventScroll: true });
      setLive(order[index]);
    };

    if (reduce) release();
    else window.setTimeout(release, 780);
  }

  function advance() {
    if (lock) return;
    if (index >= order.length - 1) return;
    show(index + 1);
  }

  function toCover() {
    if (lock) return;
    if (index === 0) {
      if (sources.open) sources.close();
      return;
    }
    show(0);
  }

  document.addEventListener("click", function (event) {
    if (event.target.closest(".sources-open, .sources")) return;
    var route = event.target.closest("[data-route]");
    if (route) {
      event.stopPropagation();
      selectRoute(route.getAttribute("data-route"));
      return;
    }
    var gate = event.target.closest("[data-gate]");
    if (gate && !gate.hasAttribute("data-advance")) {
      event.stopPropagation();
      gate.classList.add("is-lit");
      return;
    }
    if (event.target.closest("[data-advance]")) advance();
  });

  function selectRoute(name) {
    var scene = document.querySelector(".scene-2");
    scene.setAttribute("data-selected", name);
    Array.prototype.forEach.call(scene.querySelectorAll("[data-route]"), function (button) {
      var on = button.getAttribute("data-route") === name;
      button.classList.toggle("is-selected", on);
      button.setAttribute("aria-pressed", on ? "true" : "false");
    });
    var motion = document.getElementById("route-motion");
    var paths = {
      direct: "M0 160 H600",
      api: "M0 160 V236 H150 L290 160 H600",
      cloud: "M0 160 V268 C230 300 340 220 600 160"
    };
    motion.setAttribute("path", paths[name]);
    if (reduce) {
      motion.setAttribute("dur", "0.01s");
    }
    try { motion.beginElement(); } catch (err) { /* older engines still show the stroke */ }
  }

  document.addEventListener("keydown", function (event) {
    var key = event.key;
    if (key === "Escape" && sources.open) {
      sources.close();
      event.preventDefault();
      return;
    }
    if (event.metaKey || event.ctrlKey || event.altKey) return;
    if (key === " " || key === "Spacebar") {
      event.preventDefault();
      if (event.repeat || lock) return;
      if (sources.open) return;
      advance();
      return;
    }
    if (key === "r" || key === "R") {
      event.preventDefault();
      if (event.repeat || lock) return;
      toCover();
    }
  });

  document.getElementById("sources-open").addEventListener("click", function () {
    sources.showModal();
  });

  Array.prototype.forEach.call(document.querySelectorAll("[data-route]"), function (button) {
    button.setAttribute("aria-pressed", button.classList.contains("is-selected") ? "true" : "false");
  });
  document.querySelector(".scene-2").setAttribute("data-selected", "direct");

  sceneEls().forEach(function (scene) {
    var on = scene.classList.contains("is-current");
    scene.hidden = !on;
    scene.inert = !on;
  });
  setLive("cover");

})();
