var add1 = document.querySelector("#add1");
  var add2 = document.querySelector("#add2");
  var links = document.querySelector(".all-link");
  var svg = document.querySelector(".svg-right");

  var box = document.querySelector("body");
  

  add1.addEventListener("click", () => {
    add1.style.display = "none";
    add2.style.display = "flex";
    links.style.display = "flex";
  });

  add2.addEventListener("click", () => {
    add2.style.display = "none";
    add1.style.display = "flex";
    links.style.display = "none";
  });


