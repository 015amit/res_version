const menu_btn = document.querySelector(".humberger");

const animation = gsap.timeline({ paused: true, reversed: true });
animation
  .to(".menu-container", {
    y: 0,
    duration: 1,
    ease: "expo.inOut",
  })
  .to(
    ".line1",
    {
      marginBottom: "-1px",
      ease: "Power2.inOut",
      duration: 0.2,
    },
    "-=0.7"
  )
  .to(
    ".line2",
    {
      marginTop: "-1px",
      ease: "Power2.inOut",
      duration: 0.2,
    },
    "-=0.7"
  )
  .to(".line2", {
    rotation: 90,
    ease: "Power2.Out",
    duration: 0.3,
  })
  .to(".humberger", {
    rotation: 45,
    ease: "Power2.Out",
    duration: 0.3,
  })
  .to(
    ".link-item",
    {
      opacity: 1,
      duration: 0.5,
      ease: "Power2.inOut",
      stagger: 0.15,
    },
    "-=0.8"
  );

menu_btn.addEventListener("click", () =>
  animation.reversed() ? animation.play() : animation.reverse()
);
